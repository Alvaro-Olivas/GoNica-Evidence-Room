# Technical Evidence Index

This page maps public claims to the artifacts a reviewer can actually inspect.

The purpose is not to summarize GoNica. The purpose is to answer: **what can I verify here, what is only internally tested, and what is still unproven?**

## Evidence-status vocabulary

| Status | Meaning |
|---|---|
| **PUBLICLY-AUDITABLE** | Code/data/test artifact is exposed here and can be inspected or rerun. |
| **INTERNAL-TESTED** | Supported by project-authored tests in the private control plane; not independent validation. |
| **OBSERVED-SANITIZED** | Derived from real-world evidence that has been sanitized; underlying private source is not public. |
| **PRIVATE-ONLY** | Artifact exists in the private control plane but is not exposed here. |
| **UNPROVEN** | The project does not currently have sufficient evidence for the claim. |

## Claim-to-artifact map

| Claim | Public artifact | Status | What a reviewer can verify |
|---|---|---|---|
| A deterministic contract-evaluation mechanism exists | [Auditable Operational Continuity Engine Example](auditable_example/README.md) | **PUBLICLY-AUDITABLE** | Exact definitions, evaluator code, fixtures, adversarial cases and tests for 3 contracts. |
| Missing evidence does not automatically become PASS in the public subset | [`test_evaluator.py`](auditable_example/test_evaluator.py) | **PUBLICLY-AUDITABLE** | Run the test or modify the dossier; omitted evidence resolves to `UNKNOWN`. |
| Replay can be rejected when it creates duplicate business outcomes | [`B09-08` code + adversarial fixture](auditable_example/evaluator.py) | **PUBLICLY-AUDITABLE** | Set `side_effect_count > 1` and reproduce `FAIL`. |
| Identity match is separate from data-sharing authority | [`B09-06` code + adversarial fixture](auditable_example/evaluator.py) | **PUBLICLY-AUDITABLE** | `identity_matched=true`, `data_shared=true`, `authorized=false` produces `FAIL`. |
| Lifecycle semantics are evaluated separately from record existence | [`B09-01` contract and code](auditable_example/contracts.json) | **PUBLICLY-AUDITABLE** | Forced universal vocabulary fails; incomplete mapping is partial. |
| The current private engine contains 17 explicit contract checks | Public subset + [Current State](CURRENT_STATE.md) | **PRIVATE-ONLY / PARTIAL PUBLIC PROOF** | 3 are directly inspectable here; the other 14 remain private and should not be treated as independently verified from this repo. |
| Internal adversarial/regression suites exist | [Selected Test & Evaluation Evidence](SELECTED_VALIDATION_EVIDENCE.md) | **INTERNAL-TESTED** | Counts and boundaries are public; most underlying private tests are not exposed. |
| Multi-week transition incidents influenced regression design | [Longitudinal Transition Evidence](LONGITUDINAL_TRANSITION_EVIDENCE.md) | **OBSERVED-SANITIZED** | Generalized incident classes and resulting rules are visible; private source messages/identities are not. |
| Real public-source evidence was evaluated through the private engine | [Selected Test & Evaluation Evidence](SELECTED_VALIDATION_EVIDENCE.md) | **INTERNAL-TESTED / PUBLIC-SOURCE INPUT** | Aggregate results and limits are public; full private evaluation implementation is not. |
| GoNica has proven external-customer production outcomes | None | **UNPROVEN** | This repository makes no such claim. |
| GoNica has proven broad live cross-system continuity | None | **UNPROVEN** | This remains a future validation gate. |

## Public auditable subset

The most important new artifact is:

[**auditable_example/**](auditable_example/README.md)

It exposes three contracts from the current engineering approach:

- `B09-01` Lifecycle Capability Contract;
- `B09-06` Identity Match != Data-Sharing Authority;
- `B09-08` Business Event Identity != Transport Attempt.

The public subset is deliberately small enough to inspect completely. It is not presented as proof that the private 17-contract set is complete or correctly calibrated.

## Internal test results: correct interpretation

Numbers such as:

- `21/21 PASS`;
- `9/9 PASS`;
- `13/13 targeted regressions PASS`;

are **internal regression/CI results**. They establish that the current implementation satisfies the current project-authored tests. They do not establish that an independent engineer agrees with the contract design, test coverage, or calibration.

The correct next form of evidence is external challenge: new adversarial inputs, code review, fuzz/property-based testing where appropriate, and eventually bounded live outcomes.

## Real-evidence corpus: correct interpretation

Seven public-source evidence sets produced 119 private-engine contract evaluations:

- 30 `PARTIAL`;
- 6 `FAIL`;
- 83 `UNKNOWN`;
- 0 `PASS`.

This number is not used as a quality score. The source material was incomplete relative to the full contract set, so many states remained unknown.

At the same time, **0/119 PASS is a calibration signal worth challenging**. A reviewer is justified in asking whether the contracts are too strict, whether the source-to-contract applicability model needs improvement, or whether the evidence normalization loses useful signal. The project does not treat that question as closed.

## Sanitized observational evidence

The longitudinal transition page shows generalized patterns from a private real-world system transition. Examples include:

- duplicate downstream side effects;
- overbroad data/conversation visibility;
- lifecycle meaning loss;
- record cardinality/state parity gaps;
- stakeholder readiness gaps;
- task work-method gaps.

The public page intentionally excludes company/provider names, customer/employee PII and raw private messages. Therefore it is useful as **observational design input**, but it cannot be independently reconstructed from the public repo alone.

## Context pages

These provide orientation but are not themselves technical proof:

- [Architecture](ARCHITECTURE.md)
- [Conceptual Map](CONCEPTUAL_MAP.md)
- [Project Map](PROJECT_MAP.md)
- [Founder Story](FOUNDER_STORY.md)
- [Local AI Lab](LOCAL_AI_LAB.md)

## Publication rule

A public technical claim should now satisfy one of two conditions:

1. **Expose the artifact** so a reviewer can inspect it; or
2. **State explicitly that the artifact remains private and limit the claim accordingly.**

Narrative alone is not treated as evidence.
