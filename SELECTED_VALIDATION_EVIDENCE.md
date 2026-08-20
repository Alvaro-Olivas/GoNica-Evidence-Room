# Selected Test & Evaluation Evidence

This page records selected engineering results and, just as importantly, their limits.

**Important:** most numbers below are produced by project-authored tests and evaluation logic. They are useful internal regression/CI evidence. They are **not independent third-party validation**.

For directly inspectable behavior, start with the [Auditable Operational Continuity Engine Example](auditable_example/README.md).

## 1. Publicly auditable subset

**Status:** `PUBLICLY-AUDITABLE / INTERNAL REGRESSION`

The public repository exposes three exact continuity contracts plus deterministic logic, synthetic fixtures and adversarial tests:

- `B09-01` Lifecycle Capability Contract;
- `B09-06` Identity Match != Data-Sharing Authority;
- `B09-08` Business Event Identity != Transport Attempt.

Run:

```bash
python auditable_example/evaluator.py auditable_example/fixtures/complete.json
python -m unittest auditable_example/test_evaluator.py -v
```

What this supports:

- the contract mechanism is not only prose;
- selected PASS/PARTIAL/FAIL/UNKNOWN behavior can be reproduced;
- a reviewer can modify inputs and challenge the logic directly.

What this does **not** support:

- correctness of the full private 17-contract set;
- complete coverage;
- independent validation;
- production readiness.

## 2. External adversarial review and Phase 2 correction

**Status:** `EXTERNAL SOURCE REVIEW + PRIVATE INTERNAL REMEDIATION`

The public B09-08 subset exposed a real defect: a partially populated item could previously inherit permissive defaults for missing event-attempt/side-effect evidence and incorrectly become `PASS`.

That defect was reproduced, corrected and regression-covered. The external reviewer then examined additional pasted private implementation/schema/test artifacts and found the same present-but-incomplete false-PASS class in additional private checks.

The bounded private Phase 2 remediation then recorded the following project-authored evidence on its pull-request CI path:

- active deterministic logic consolidated into one authoritative private check module;
- real Draft 2020-12 JSON Schema validation before deterministic contract evaluation;
- schema-invalid structured evidence blocked before contract checks;
- two adversarial vectors covering all 17 private contracts: explicit contradiction and present-but-incomplete evidence;
- `41/41` private Brain tests PASS on the remediation PR;
- schema-definition validation PASS;
- representative dossier schema validation PASS;
- corrected full-company R3 fixture -> `READY_FOR_BOUNDED_SYNTHETIC_TEST`;
- stress full-company R3 fixture -> `BLOCKED_BY_CONFLICT`;
- both R3 paths keep `production_authorized:false`;
- Windows Control Plane validation PASS before merge.

Correct interpretation:

This is a documented correction cycle where external scrutiny generated useful counterexamples and the project added regression protection. The external reviewer did **not** independently execute the full private engine, so this must not be described as independent third-party validation of the 17-contract implementation.

## 3. Governed GoHighLevel bridge

**Status:** `INTERNAL-TESTED / HISTORICAL`

Selected historical project-authored validation recorded:

- 28/28 governed bridge tests passed;
- synthetic acceptance: PASS;
- package/hash checks: PASS;
- secret scan: CLEAR;
- bounded historical live-read evidence exists.

Correct interpretation:

This supports that a governed bridge was implemented and exercised under defined project tests. It does not establish that every HighLevel operation is correct, that the tests are independently sufficient, or that unrestricted production writes are authorized.

## 4. Earlier Brain benchmark program

**Status:** `INTERNAL-TESTED — SYNTHETIC / SANITIZED`

Earlier project-authored benchmark results:

- 46 cases total;
- 41 PASS;
- 5 PARTIAL;
- 0 FAIL;
- 0 critical governance failures.

The five partials were preserved and used to generate corrections/regression requirements.

Correct interpretation:

These results are evidence of an internal engineering process, not an external quality score. The weighted score previously reported by the project should not be treated as independent product validation.

## 5. Operational-continuity regression history

**Status:** `INTERNAL-TESTED — SYNTHETIC / CONTROLLED`

Original executions:

- 72 total;
- 59 PASS;
- 13 PARTIAL;
- 0 FAIL.

Targeted correction regressions added afterward:

- 13 additional executions;
- 13 PASS.

The original partials were not rewritten after the corrections passed.

What this supports:

- known gaps can be turned into explicit regression conditions;
- the project preserves earlier results rather than converting history into all-green evidence.

What it does not support:

- that the contract suite is complete;
- that an outside reviewer would choose the same rules;
- that real companies will produce the same outcomes.

## 6. Private 17-contract reference engine

**Status:** `PRIVATE-ONLY / INTERNAL-TESTED`

The current private control plane records:

- 17 explicit continuity/governance contracts;
- 17 deterministic reference checks;
- structured synthetic fixtures;
- an explicit contradiction/unsafe adversarial vector across all 17 contracts;
- a present-but-incomplete/missing-evidence vector across all 17 contracts;
- a meta-regression requiring both vectors to cover the same complete registry;
- a test that prevents a supplied `PASS` from hiding a deterministic `FAIL`;
- executable transition-dossier schema validation before deterministic evaluation;
- incident-to-regression handling;
- reports and hash-verifiable evidence bundles.

Only three contracts are currently exposed as runnable public code in this Evidence Room. A reviewer should therefore distinguish:

> **private implementation claim** from **publicly auditable proof**.

## 7. Real-evidence transition corpus — August 18 + hardened rerun August 20

**Status:** `PRIVATE EVALUATION OVER PUBLIC-SOURCE INPUTS`

Seven acquired/normalized public-source evidence sets were evaluated through the private 17-contract engine.

Historical aggregate:

- 119 contract evaluations;
- 30 PARTIAL;
- 6 FAIL;
- 83 UNKNOWN;
- 0 PASS;
- 7/7 evidence bundles verified internally;
- 4 learning candidates remained unpromoted;
- historical internal Brain suite at that savepoint: 21/21 PASS;
- historical internal corpus regression suite: 9/9 PASS.

After Phase 2, the same seven sanitized dossiers were explicitly rerun through the hardened engine.

Hardened aggregate:

- 119 contract evaluations;
- 30 PARTIAL;
- 6 FAIL;
- 83 UNKNOWN;
- 0 PASS.

The aggregate was unchanged, and all seven rerun dossiers remained `production_authorized:false`.

### How to interpret `0/119 PASS`

This is **not a success metric**.

The seven inputs were not complete transition dossiers. They were public evidence sources with uneven coverage, so many contract questions had insufficient evidence and remained `UNKNOWN`.

The unchanged before/after result is narrower evidence: the known false-PASS correction did not alter this particular seven-source batch. It does not prove that the old defects were harmless for other inputs.

Calibration questions remain open:

- Are some contracts too strict?
- Is applicability modeled well enough?
- Is useful signal being lost in normalization?
- What would an independent reviewer classify differently?

## 8. Longitudinal incident-derived regressions — August 19

**Status:** `OBSERVED-SANITIZED + INTERNAL REGRESSION`

A multi-week private business-system transition produced generalized incident classes. Three were mapped to existing contracts and converted into internal regressions:

1. duplicate downstream side effects;
2. overbroad conversation/data visibility;
3. lifecycle/business-class ambiguity.

Additional gaps remain pending rather than being forced into the current contract set:

- source/destination record cardinality and lifecycle-state parity;
- whole-company stakeholder/department readiness before rollout;
- task work-method parity beyond task-object existence.

See [Longitudinal Business-System Transition Evidence](LONGITUDINAL_TRANSITION_EVIDENCE.md).

Because the underlying company evidence is private and sanitized, an outside reviewer cannot independently reconstruct the incidents from this repo alone. The public value is the generalized rule and the disclosed limitation, not a claim of customer validation.

## 9. Production boundary

A project rule remains:

```text
PASSING AN INTERNAL TEST != PRODUCTION AUTHORIZATION
```

Current public evidence does not prove:

- external-customer production outcomes;
- broad live cross-system continuity;
- independent contract calibration;
- independent execution of the full private remediation;
- independent security/compliance certification;
- completed enterprise deployment.

## What stronger evidence should look like next

The next evidence tier is not a larger internal pass count. It is stronger external challenge and bounded proof:

- independent execution/code review where privacy permits;
- reviewer-authored adversarial cases;
- fuzz/property-based testing where appropriate;
- applicability/calibration review of the contract model;
- bounded live proofs with measurable outcomes;
- eventually external pilot/customer evidence.

That is the standard against which future Evidence Room updates should be judged.
