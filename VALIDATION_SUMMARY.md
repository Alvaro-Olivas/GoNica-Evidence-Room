# Test & Validation Summary

**Updated:** August 19, 2026

GoNica separates implementation, internal testing, public auditability, observation and production use.

The project has substantial **internal** test history. Most of those tests were written by the same project that implements the system. They are useful for regression control, but they are not independent validation.

For directly reproducible public evidence, start with the [Auditable Operational Continuity Engine Example](auditable_example/README.md).

## Evidence levels used here

```text
DESCRIBED
→ BUILT
→ INTERNAL-TESTED
→ PUBLICLY-AUDITABLE (when artifact can be exposed)
→ EXTERNALLY-CHALLENGED
→ BOUNDED LIVE PROOF
→ PRODUCTION AUTHORIZATION
```

A component can stop at any of these levels. They are not interchangeable.

## Publicly auditable evidence

The Evidence Room currently exposes a runnable subset of the Operational Continuity Engine with:

- 3 exact contracts;
- deterministic code;
- synthetic input;
- adversarial cases;
- regression tests;
- public GitHub Actions CI.

This is the strongest public evidence in the repository because a reviewer can modify the inputs and challenge the behavior directly.

It still does not constitute independent approval of the design.

## Internal regression history

### Operational-continuity program

Original project-authored executions:

- 72 total;
- 59 PASS;
- 13 PARTIAL;
- 0 FAIL.

Later targeted correction regressions:

- 13 additional executions;
- 13 PASS.

The earlier partial results were preserved rather than rewritten after corrections passed.

### Current private reference engine

The private control plane records:

- 17 explicit continuity/governance contracts;
- 17 deterministic checks;
- synthetic and adversarial fixtures;
- internal tests preventing selected unsafe conditions from passing;
- incident-to-regression handling;
- reports and evidence bundles.

Only 3 contracts are currently exposed publicly as executable code. The remaining private implementation is a project claim supported by private artifacts, not something this public repository independently proves.

## Real-evidence corpus

Seven public-source evidence sets were evaluated through the private engine.

Aggregate:

- 119 evaluations;
- 30 PARTIAL;
- 6 FAIL;
- 83 UNKNOWN;
- 0 PASS.

This is not a GoNica quality score.

The input sources were incomplete relative to the full contract set, so many questions could not be answered. Preserving `UNKNOWN` instead of inventing `PASS` is intentional.

However, the `0/119 PASS` result also creates an unresolved calibration question. External reviewers are justified in asking whether:

- the contracts are too strict;
- applicability is modeled well enough;
- evidence normalization discards useful signal;
- the source set is unsuitable for the questions being asked.

The project does not treat those questions as settled merely because the current engine behaved consistently with its own rules.

## Internal suite counts

Private records currently include results such as:

- Brain suite: 21/21 PASS;
- corpus regression suite: 9/9 PASS;
- targeted correction regressions: 13/13 PASS.

Correct interpretation:

> The current implementation satisfies the current project-authored tests.

Incorrect interpretation:

> The system has been independently proven correct.

The second statement is not supported.

## Longitudinal observational evidence

A private multi-week business-system transition record was sanitized and generalized into incident classes.

Three incident classes currently have internal regression coverage under existing contracts:

1. duplicate downstream side effects;
2. unauthorized/overbroad data visibility;
3. lifecycle/business-class ambiguity.

Other gaps remain deliberately unpromoted, including object/state parity, whole-company readiness and task work-method continuity.

Because the original company evidence is private, this public repository exposes the generalized lesson and its limits, not an independently reconstructable customer case.

## Correction discipline

Earlier results are not rewritten after later corrections.

```text
ORIGINAL RESULT
→ GAP IDENTIFIED
→ REQUIREMENT / CORRECTION
→ REGRESSION
→ NEW RESULT
```

That preserves the history of what actually failed or remained incomplete.

## What stronger validation requires next

The next tier should not be more self-authored green tests. It should include some combination of:

- independent code review;
- reviewer-authored adversarial cases;
- fuzz/property-based testing where appropriate;
- independent contract-calibration review;
- bounded live trials with measurable outcomes;
- external pilot/customer evidence.

## Current boundary

Public evidence supports an early-stage technical system with inspectable selected logic and a disciplined internal regression process.

It does **not** establish:

- broad production readiness;
- independent correctness of the 17-contract model;
- external-customer outcomes;
- enterprise-scale deployment;
- security/compliance certification;
- broad live cross-system continuity.
