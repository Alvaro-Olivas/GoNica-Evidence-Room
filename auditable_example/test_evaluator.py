import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / "fixtures"
sys.path.insert(0, str(ROOT))

from evaluator import evaluate_dossier  # noqa: E402


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def evaluation_for(result, contract_id):
    return next(item for item in result["contract_evaluations"] if item["contract_id"] == contract_id)


class PublicOperationalContinuitySubsetTests(unittest.TestCase):
    def test_complete_synthetic_dossier_passes_all_three_contracts(self):
        dossier = load_json(FIXTURES / "complete.json")
        result = evaluate_dossier(dossier)

        self.assertEqual(result["readiness"], "SUBSET_CHECKS_PASS")
        self.assertFalse(result["production_authorized"])
        self.assertEqual(len(result["contract_evaluations"]), 3)
        self.assertTrue(
            all(item["evaluation_state"] == "PASS" for item in result["contract_evaluations"])
        )

    def test_all_adversarial_cases_fail_the_intended_contract(self):
        cases = load_json(FIXTURES / "adversarial_cases.json")["cases"]
        self.assertEqual(len(cases), 3)

        for case in cases:
            with self.subTest(case=case["id"]):
                result = evaluate_dossier(case["dossier"])
                evaluation = evaluation_for(result, case["expected_contract"])
                self.assertEqual(evaluation["evaluation_state"], case["expected_state"])
                self.assertEqual(result["readiness"], "BLOCKED_BY_CONFLICT")
                self.assertFalse(result["production_authorized"])

    def test_missing_evidence_family_never_becomes_pass(self):
        result = evaluate_dossier({})
        self.assertEqual(result["readiness"], "EVIDENCE_INCOMPLETE")
        self.assertTrue(
            all(item["evaluation_state"] == "UNKNOWN" for item in result["contract_evaluations"])
        )
        self.assertFalse(result["production_authorized"])

    def test_item_present_without_side_effect_evidence_is_not_pass(self):
        dossier = {"business_events": [{"idempotency_key": "abc"}]}
        result = evaluate_dossier(dossier)
        evaluation = evaluation_for(result, "B09-08")
        self.assertEqual(evaluation["evaluation_state"], "PARTIAL")
        self.assertEqual(result["readiness"], "EVIDENCE_INCOMPLETE")

    def test_retry_without_idempotency_evidence_is_partial(self):
        dossier = {
            "business_events": [
                {
                    "business_event_id": "SYN-RETRY-01",
                    "transport_attempts": 2,
                    "side_effect_count": 1,
                    "evidence_refs": ["SYN-RETRY-EVIDENCE"],
                }
            ]
        }
        result = evaluate_dossier(dossier)
        evaluation = evaluation_for(result, "B09-08")
        self.assertEqual(evaluation["evaluation_state"], "PARTIAL")
        self.assertEqual(result["readiness"], "EVIDENCE_INCOMPLETE")

    def test_lifecycle_item_missing_explicit_universal_vocabulary_decision_is_partial(self):
        dossier = {
            "lifecycle_bindings": [
                {
                    "company_stage": "Qualified",
                    "capability_id": "QUALIFICATION",
                }
            ]
        }
        result = evaluate_dossier(dossier)
        evaluation = evaluation_for(result, "B09-01")
        self.assertEqual(evaluation["evaluation_state"], "PARTIAL")
        self.assertEqual(result["readiness"], "EVIDENCE_INCOMPLETE")

    def test_data_sharing_item_missing_authority_evidence_is_partial(self):
        dossier = {
            "data_sharing": [
                {
                    "identity_matched": True,
                }
            ]
        }
        result = evaluate_dossier(dossier)
        evaluation = evaluation_for(result, "B09-06")
        self.assertEqual(evaluation["evaluation_state"], "PARTIAL")
        self.assertEqual(result["readiness"], "EVIDENCE_INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
