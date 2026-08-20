from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

VALID_STATES = {"PASS", "PARTIAL", "FAIL", "UNKNOWN", "NOT_APPLICABLE"}
CONTRACT_IDS = ("B09-01", "B09-06", "B09-08")


def _result(
    state: str,
    finding: str,
    required_action: str = "",
    evidence_refs: Optional[List[str]] = None,
) -> Dict[str, Any]:
    if state not in VALID_STATES:
        raise ValueError(f"invalid state: {state}")
    return {
        "evaluation_state": state,
        "finding": finding,
        "required_action": required_action,
        "evidence_refs": evidence_refs or [],
        "evaluation_source": "DETERMINISTIC",
    }


def _refs(items: List[Dict[str, Any]]) -> List[str]:
    refs: List[str] = []
    for item in items:
        for ref in item.get("evidence_refs", []) or []:
            if ref not in refs:
                refs.append(ref)
    return refs


def check_b09_01(dossier: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Lifecycle Capability Contract."""
    items = dossier.get("lifecycle_bindings")
    if items is None:
        return None
    if not items:
        return _result("UNKNOWN", "Lifecycle binding evidence was supplied as an empty set.")

    forced = [item for item in items if item.get("forced_universal_vocabulary") is True]
    incomplete = [
        item
        for item in items
        if not item.get("company_stage")
        or not item.get("capability_id")
        or "forced_universal_vocabulary" not in item
    ]

    if forced:
        return _result(
            "FAIL",
            "At least one company lifecycle label is being forced as universal vocabulary.",
            "Map company-specific stages to reusable lifecycle capabilities instead of forcing labels.",
            _refs(items),
        )
    if incomplete:
        return _result(
            "PARTIAL",
            "Lifecycle bindings exist but required semantic evidence is incomplete.",
            "Provide company stage, capability identity, and an explicit forced-universal-vocabulary decision.",
            _refs(items),
        )
    return _result(
        "PASS",
        "Lifecycle vocabulary is bound to reusable capabilities without forced universal labels.",
        evidence_refs=_refs(items),
    )


def check_b09_06(dossier: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Identity Match != Data-Sharing Authority."""
    items = dossier.get("data_sharing")
    if items is None:
        return None
    if not items:
        return _result("UNKNOWN", "Data-sharing authority evidence was supplied as an empty set.")

    unauthorized = []
    incomplete = []
    for item in items:
        required_flags_present = all(
            key in item for key in ("identity_matched", "data_shared", "authorized")
        )
        if not required_flags_present:
            incomplete.append(item)
            continue

        if item.get("data_shared") is True and item.get("authorized") is False:
            unauthorized.append(item)
        if item.get("data_shared") is True and (
            not item.get("purpose") or not item.get("scope")
        ):
            incomplete.append(item)

    if unauthorized:
        return _result(
            "FAIL",
            "Data was shared despite explicit lack of sharing authority.",
            "Block sharing until purpose, scope and authorization are explicit.",
            _refs(items),
        )
    if incomplete:
        return _result(
            "PARTIAL",
            "Data-sharing evidence exists but authority/purpose/scope evidence is incomplete.",
            "Record identity-match state, sharing state, authority, and any applicable purpose/scope evidence.",
            _refs(items),
        )
    return _result(
        "PASS",
        "Identity matching and data-sharing authority are evaluated separately with explicit evidence.",
        evidence_refs=_refs(items),
    )


def check_b09_08(dossier: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Business Event Identity != Transport Attempt."""
    items = dossier.get("business_events")
    if items is None:
        return None
    if not items:
        return _result("UNKNOWN", "Business-event evidence was supplied as an empty set.")

    duplicate_outcome = []
    incomplete = []
    invalid_numeric = []

    required_fields = {
        "business_event_id",
        "transport_attempts",
        "side_effect_count",
        "idempotency_key",
    }

    for item in items:
        if any(key not in item for key in required_fields):
            incomplete.append(item)
            continue

        try:
            attempts = int(item["transport_attempts"])
            side_effect_count = int(item["side_effect_count"])
        except (TypeError, ValueError):
            invalid_numeric.append(item)
            continue

        if attempts < 1 or side_effect_count < 0:
            invalid_numeric.append(item)
            continue

        if side_effect_count > 1:
            duplicate_outcome.append(item)
        if attempts > 1 and not item.get("idempotency_key"):
            incomplete.append(item)
        if not item.get("business_event_id") or not item.get("idempotency_key"):
            incomplete.append(item)

    if duplicate_outcome:
        return _result(
            "FAIL",
            "Multiple transport attempts produced duplicate business side effects.",
            "Use a stable business-event identity/idempotency key and reconcile retries to one outcome.",
            _refs(items),
        )
    if invalid_numeric:
        return _result(
            "PARTIAL",
            "Business-event evidence contains invalid transport-attempt or side-effect counts.",
            "Provide explicit non-negative side-effect counts and transport-attempt counts of at least one.",
            _refs(items),
        )
    if incomplete:
        return _result(
            "PARTIAL",
            "Business-event evidence is present but required event/retry/side-effect evidence is incomplete.",
            "Provide business event identity, transport attempts, side-effect count, and idempotency evidence explicitly.",
            _refs(items),
        )
    return _result(
        "PASS",
        "Business-event identity, transport attempts, idempotency, and side-effect evidence are explicit and consistent.",
        evidence_refs=_refs(items),
    )


CHECKS = {
    "B09-01": check_b09_01,
    "B09-06": check_b09_06,
    "B09-08": check_b09_08,
}


def evaluate_dossier(dossier: Dict[str, Any]) -> Dict[str, Any]:
    evaluations = []
    for contract_id in CONTRACT_IDS:
        result = CHECKS[contract_id](dossier)
        if result is None:
            result = _result(
                "UNKNOWN",
                "No structured evidence was supplied for this contract.",
                "Provide evidence or explicitly justify NOT_APPLICABLE; absence never becomes PASS.",
            )
        evaluations.append({"contract_id": contract_id, **result})

    states = [item["evaluation_state"] for item in evaluations]
    if "FAIL" in states:
        readiness = "BLOCKED_BY_CONFLICT"
    elif "PARTIAL" in states or "UNKNOWN" in states:
        readiness = "EVIDENCE_INCOMPLETE"
    else:
        readiness = "SUBSET_CHECKS_PASS"

    return {
        "component": "Operational Continuity Engine",
        "public_subset": True,
        "production_authorized": False,
        "readiness": readiness,
        "contract_evaluations": evaluations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the public auditable Operational Continuity Engine subset.")
    parser.add_argument("dossier", help="Path to a JSON evidence dossier")
    args = parser.parse_args()

    dossier = json.loads(Path(args.dossier).read_text(encoding="utf-8"))
    print(json.dumps(evaluate_dossier(dossier), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
