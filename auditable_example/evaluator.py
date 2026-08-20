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
    missing = [item for item in items if not item.get("company_stage") or not item.get("capability_id")]

    if forced:
        return _result(
            "FAIL",
            "At least one company lifecycle label is being forced as universal vocabulary.",
            "Map company-specific stages to reusable lifecycle capabilities instead of forcing labels.",
            _refs(items),
        )
    if missing:
        return _result(
            "PARTIAL",
            "Lifecycle bindings exist but one or more lack company-stage or reusable-capability identity.",
            "Complete the company-stage to capability mapping.",
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
        if item.get("identity_matched") is True and item.get("data_shared") is True and item.get("authorized") is not True:
            unauthorized.append(item)
        if item.get("data_shared") is True and (not item.get("purpose") or not item.get("scope")):
            incomplete.append(item)

    if unauthorized:
        return _result(
            "FAIL",
            "Identity matching was treated as authority to share data.",
            "Block sharing until purpose, scope and authorization are explicit.",
            _refs(items),
        )
    if incomplete:
        return _result(
            "PARTIAL",
            "Data sharing may be authorized, but purpose/scope evidence is incomplete.",
            "Record the approved business purpose and disclosure scope.",
            _refs(items),
        )
    return _result(
        "PASS",
        "Identity matching and data-sharing authority are evaluated separately.",
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
    for item in items:
        attempts = int(item.get("transport_attempts", 1) or 1)
        side_effect_count = int(item.get("side_effect_count", 0) or 0)
        if side_effect_count > 1:
            duplicate_outcome.append(item)
        if attempts > 1 and not item.get("idempotency_key"):
            incomplete.append(item)

    if duplicate_outcome:
        return _result(
            "FAIL",
            "Multiple transport attempts produced duplicate business side effects.",
            "Use a stable business-event identity/idempotency key and reconcile retries to one outcome.",
            _refs(items),
        )
    if incomplete:
        return _result(
            "PARTIAL",
            "Retries occurred without explicit idempotency evidence.",
            "Define stable business-event identity and idempotency behavior.",
            _refs(items),
        )
    return _result(
        "PASS",
        "Business-event identity is separated from transport attempts and duplicate side effects are prevented.",
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
