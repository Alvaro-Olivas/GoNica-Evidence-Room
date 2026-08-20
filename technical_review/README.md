# GoNica Technical Review Surface

This branch exposes a substantially broader, sanitized technical-review surface for adversarial engineering review.

Purpose: enable bottom-up inspection of the current GoNica Operational Continuity Engine and supporting evidence mechanics without publishing third-party private operational data, credentials, customer PII, or employer-confidential material.

## Review order

1. `registry/contract_registry.json`
2. `engine/engine.py`
3. `engine/strict_contract_checks.py`
4. `schemas/transition_dossier.schema.json`
5. `tests/`
6. `audit/PASS_PATH_COMPLETENESS_AUDIT.md`

## Review standard

Do not trust claims because they are documented. Trace:

`CONTRACT TEXT <-> REGISTRY <-> SCHEMA <-> CHECK <-> FIXTURE <-> REGRESSION`

For each contract, attack the PASS path:

- evidence family absent
- family present but empty
- item present but incomplete
- complete safe item
- explicit unsafe item
- false vs 0 vs empty vs absent vs UNKNOWN

Classify findings as logic bug, coverage gap, schema mismatch, implementation/contract mismatch, architecture weakness, documentation overclaim, maintainability issue, or security/privacy issue.

## Important boundary

This is not the raw private Control Plane. Private third-party evidence and secrets are intentionally excluded. If a claim cannot be verified from this review surface, mark it `NOT VERIFIED` and identify the missing artifact.

`production_authorized:false`
