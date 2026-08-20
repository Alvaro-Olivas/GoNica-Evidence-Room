# Auditable Operational Continuity Engine Example

This folder is a **public, executable subset** of the current GoNica Operational Continuity Engine.

It exists so a technical reviewer does not have to trust narrative claims about the engine. The reviewer can inspect three contract definitions, read the deterministic evaluation logic, run a passing synthetic dossier, run adversarial cases, and challenge how incomplete evidence is classified.

The current private engine contains a broader 17-contract set. This public subset exposes only three contracts chosen because they are easy to understand and directly tied to recurring transition failures.

## What is exposed

1. [`contracts.json`](contracts.json) — public definitions for three contracts.
2. [`evaluator.py`](evaluator.py) — deterministic evaluation logic for those contracts.
3. [`fixtures/complete.json`](fixtures/complete.json) — one synthetic dossier expected to pass all three.
4. [`fixtures/adversarial_cases.json`](fixtures/adversarial_cases.json) — three deliberately unsafe cases.
5. [`test_evaluator.py`](test_evaluator.py) — executable regression tests, including partial-item missing-evidence cases.

## The three contracts

### B09-01 — Lifecycle Capability Contract

A destination record is not considered semantically complete merely because it exists. Company-specific lifecycle vocabulary must map to reusable lifecycle capability without forcing one company's exact labels into a universal schema.

### B09-06 — Identity Match != Data-Sharing Authority

Knowing that two records identify the same person or company does not itself authorize disclosure or reuse of all associated data. Identity and sharing authority are separate decisions.

### B09-08 — Business Event Identity != Transport Attempt

Webhook/API/queue retries must not create duplicate business outcomes. A stable business-event identity and idempotent behavior are required when an action can be replayed.

The Required / Prohibited / Evidence / Regression definitions are in [`contracts.json`](contracts.json).

## Run it

From the repository root:

```bash
python auditable_example/evaluator.py auditable_example/fixtures/complete.json
python -m unittest auditable_example/test_evaluator.py -v
```

The code uses only the Python standard library.

Current regression coverage includes:

```text
complete synthetic dossier -> all three PASS
three explicit adversarial cases -> intended contract FAIL
missing evidence family -> UNKNOWN, never PASS
B09-08 item present but side-effect/retry evidence missing -> PARTIAL
B09-08 retry without idempotency evidence -> PARTIAL
B09-01 item missing explicit universal-vocabulary decision -> PARTIAL
B09-06 item missing sharing-authority evidence -> PARTIAL
```

The important point is not the number of tests. These are **internal deterministic regression tests**, not independent third-party validation. Their purpose is to make the evaluation behavior inspectable and falsifiable.

## External-review correction — partial item evidence

An external technical review found a real defect in the first public version of `B09-08`.

The original evaluator used permissive defaults:

```python
transport_attempts -> default 1
side_effect_count  -> default 0
```

That meant this incomplete item could incorrectly reach `PASS`:

```json
{
  "business_events": [
    {"idempotency_key": "abc"}
  ]
}
```

The problem was not merely missing test coverage. The evaluator was converting **absence of evidence** into apparently safe values.

The current evaluator no longer does that. For `B09-08`, required event/retry/side-effect fields must be explicitly present before the item can pass. The exact counterexample above is now a regression test and must resolve to `PARTIAL`.

The same review pattern was applied to the other two public contracts:

- `B09-01` now requires an explicit `forced_universal_vocabulary` decision rather than treating an absent flag as `false`;
- `B09-06` now requires explicit identity-match, sharing-state, and authorization evidence rather than treating absent fields as safe.

This correction is intentionally visible because an Evidence Room should preserve discovered weaknesses and their fixes, not silently rewrite the history.

## Try to break it

A reviewer can edit the JSON fixtures or create a new dossier.

Examples:

- remove `capability_id` from a lifecycle binding: the result should become `PARTIAL`, not `PASS`;
- omit `forced_universal_vocabulary`: `B09-01` should become `PARTIAL`;
- set `forced_universal_vocabulary` to `true`: `B09-01` should `FAIL`;
- supply only `identity_matched=true` with no sharing/authority state: `B09-06` should become `PARTIAL`;
- set `data_shared=true` and `authorized=false`: `B09-06` should `FAIL`;
- supply only an `idempotency_key` with no retry/side-effect evidence: `B09-08` should become `PARTIAL`;
- make `side_effect_count` greater than 1: `B09-08` should `FAIL`;
- remove an entire evidence family: the affected contract should become `UNKNOWN`, never silently `PASS`.

## What this is — and is not

**This is:**

- real executable logic from the current engineering approach;
- a public inspection subset;
- deterministic rule evaluation over structured evidence;
- synthetic/adversarial regression material;
- a way for an external engineer to challenge the mechanism directly.

**This is not:**

- the complete private 17-contract engine;
- proof that all 17 contracts are correctly calibrated;
- independent validation;
- a production deployment;
- evidence that GoNica was deployed inside the private company whose transition informed later regressions;
- permission to infer confidential company or customer information.

## Component definition

**Operational Continuity Engine** — a deterministic evidence-evaluation component that tests business-system transition evidence against explicit continuity contracts.

The current reference implementation is written in Python. Python is an implementation detail, not the definition of the component.

## Why only three contracts are public here

The goal is not to maximize disclosure. The goal is to provide enough real substance for a reviewer to answer basic engineering questions:

- What is a contract?
- What input does it examine?
- What makes it PASS, PARTIAL, FAIL, or UNKNOWN?
- Can missing evidence accidentally become PASS?
- Can an unsafe case be reproduced?
- Can the reviewer change the input and challenge the output?

If this subset cannot survive that level of inspection, larger claims about the system should not be trusted either.
