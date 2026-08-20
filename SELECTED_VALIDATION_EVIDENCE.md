# Selected Test & Evaluation Evidence

This page records selected engineering results and, just as importantly, their limits.

**Important:** most numbers below are produced by project-authored tests and evaluation logic. They are useful internal regression/CI evidence. They are **not independent third-party validation**.

For directly inspectable behavior, start with the [Auditable Operational Continuity Engine Example](auditable_example/README.md).

## 1. Publicly auditable subset

**Status:** `PUBLICLY-AUDITABLE / INTERNAL REGRESSION`

The public repository now exposes three exact continuity contracts plus deterministic logic, synthetic fixtures and adversarial tests:

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

## 2. Governed GoHighLevel bridge

**Status:** `INTERNAL-TESTED / HISTORICAL`

Selected historical project-authored validation recorded:

- 28/28 governed bridge tests passed;
- synthetic acceptance: PASS;
- package/hash checks: PASS;
- secret scan: CLEAR;
- bounded historical live-read evidence exists.

Correct interpretation:

This supports that a governed bridge was implemented and exercised under defined project tests. It does not establish that every HighLevel operation is correct, that the tests are independently sufficient, or that unrestricted production writes are authorized.

## 3. Earlier Brain benchmark program

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

## 4. Operational-continuity regression history

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

## 5. Private 17-contract reference engine

**Status:** `PRIVATE-ONLY / INTERNAL-TESTED`

The current private control plane records:

- 17 explicit continuity/governance contracts;
- 17 deterministic reference checks;
- structured synthetic fixtures;
- 17 adversarial contract cases in the private suite;
- a test that prevents a supplied `PASS` from hiding a deterministic `FAIL`;
- incident-to-regression handling;
- reports and hash-verifiable evidence bundles.

Only three of those contracts are currently exposed as runnable public code in this Evidence Room. A reviewer should therefore distinguish:

> **private implementation claim** from **publicly auditable proof**.

## 6. Real-evidence transition corpus — August 18

**Status:** `PRIVATE EVALUATION OVER PUBLIC-SOURCE INPUTS`

Seven acquired/normalized public-source evidence sets were evaluated through the private 17-contract engine.

Aggregate:

- 119 contract evaluations;
- 30 PARTIAL;
- 6 FAIL;
- 83 UNKNOWN;
- 0 PASS;
- 7/7 evidence bundles verified internally;
- 4 learning candidates remained unpromoted;
- internal Brain suite: 21/21 PASS;
- internal corpus regression suite: 9/9 PASS.

### How to interpret `0/119 PASS`

This is **not a success metric**.

The seven inputs were not complete transition dossiers. They were public evidence sources with uneven coverage, so many contract questions had insufficient evidence and remained `UNKNOWN`.

The result does demonstrate that the evaluator does not automatically turn absence into PASS. But it also creates a legitimate engineering question that remains open:

- Are some contracts too strict?
- Is applicability modeled well enough?
- Is useful signal being lost in normalization?
- What would an independent reviewer classify differently?

The Evidence Room should not frame `0/119 PASS` as automatically positive. It is a calibration signal that should be challenged.

## 7. Longitudinal incident-derived regressions — August 19

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

## 8. Production boundary

A project rule remains:

```text
PASSING AN INTERNAL TEST != PRODUCTION AUTHORIZATION
```

Current public evidence does not prove:

- external-customer production outcomes;
- broad live cross-system continuity;
- independent contract calibration;
- independent security/compliance certification;
- completed enterprise deployment.

## What stronger evidence should look like next

The next evidence tier is not a larger internal pass count. It is external challenge:

- outside code review;
- reviewer-authored adversarial cases;
- fuzz/property-based testing where appropriate;
- applicability/calibration review of the contract model;
- bounded live proofs with measurable outcomes;
- eventually external pilot/customer evidence.

That is the standard against which future Evidence Room updates should be judged.
