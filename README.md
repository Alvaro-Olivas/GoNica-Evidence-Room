# GoNica Evidence Room

**Public technical inspection surface for GoNica Brain.**

This repository should not require a reviewer to trust a product description. Its purpose is to expose enough concrete material to inspect what exists, reproduce selected behavior, see what remains private, and distinguish internal testing from independent validation.

## Technical reviewer: start here

### 1. Run an actual subset of the Operational Continuity Engine

[**Open the Auditable Operational Continuity Engine Example →**](auditable_example/README.md)

The public subset includes:

- 3 exact contract definitions;
- deterministic evaluation code;
- a passing synthetic dossier;
- 3 adversarial cases;
- executable regression tests;
- a public GitHub Actions workflow that reruns the subset.

From the repository root:

```bash
python auditable_example/evaluator.py auditable_example/fixtures/complete.json
python -m unittest auditable_example/test_evaluator.py -v
```

The exposed contracts are:

- `B09-01` — Lifecycle Capability Contract;
- `B09-06` — Identity Match != Data-Sharing Authority;
- `B09-08` — Business Event Identity != Transport Attempt.

The current private reference engine contains a broader 17-contract set. **This public repository does not ask a reviewer to treat the unexposed 14 contracts as independently verified.** The public subset exists so the mechanism itself can be inspected and challenged.

## What the Operational Continuity Engine is

**Operational Continuity Engine** — a deterministic evidence-evaluation component that tests business-system transition evidence against explicit continuity contracts.

The current reference implementation is written in Python. Python is an implementation detail, not the identity of the component.

A contract defines a required behavior/evidence condition and resolves evidence into one of:

```text
PASS
PARTIAL
FAIL
UNKNOWN
NOT_APPLICABLE
```

Missing evidence is not allowed to silently become `PASS`.

## Evidence you can inspect publicly

| Artifact | What you can inspect directly |
|---|---|
| [Auditable engine subset](auditable_example/README.md) | Exact contract text, code, fixtures, adversarial cases and tests. |
| [Technical Evidence Index](TECHNICAL_EVIDENCE_INDEX.md) | Claim-to-artifact map and which claims are public vs private-only. |
| [Selected Test & Evaluation Evidence](SELECTED_VALIDATION_EVIDENCE.md) | Internal benchmark/regression results with explicit limits. |
| [Longitudinal Transition Evidence](LONGITUDINAL_TRANSITION_EVIDENCE.md) | Sanitized real-world incident patterns and how they became regression candidates. |
| [CRM Migration Case Study](CRM_MIGRATION_PRESERVATION_CASE_STUDY.md) | Synthetic/sanitized transition method and preservation logic. |
| [Current State](CURRENT_STATE.md) | What is actually implemented, what is only tested, and what remains unproven. |
| [Failures and Lessons](FAILURES_AND_LESSONS.md) | Recorded failures, partials, corrections and no-repeat lessons. |

## Important distinction: internal tests are not independent validation

The project has internal benchmark, regression and CI results. Those are useful for reproducibility and preventing known failures from returning, but they are **self-authored engineering evidence**, not independent certification.

For example, private test counts such as `21/21 PASS` or `9/9 PASS` mean the current implementation satisfies the tests currently defined by the project. They do **not** prove that the tests are complete, correctly calibrated, or resistant to every external challenge.

That is why this public room now exposes a runnable subset: a reviewer can modify the inputs, add adversarial cases, and try to break the behavior directly.

## Real-evidence corpus result: how to read 0/119 PASS

Seven public-source evidence sets were evaluated against the broader private 17-contract engine. The aggregate was:

- 119 contract evaluations;
- 30 `PARTIAL`;
- 6 `FAIL`;
- 83 `UNKNOWN`;
- 0 `PASS`.

This is **not presented as a success rate** and should not be read as proof that the engine is well calibrated. The source documents were not complete migration dossiers, so many contracts lacked enough evidence to pass. The engine deliberately kept missing facts as `UNKNOWN`.

At the same time, `0/119 PASS` is a legitimate calibration question for external reviewers: are the contracts appropriately strict, are the evidence requirements practical, and does the engine distinguish useful signal from missing context? That question remains open to challenge rather than being explained away as automatically positive.

## What remains private

The private GoNica control plane contains:

- the full current 17-contract registry;
- the complete deterministic reference implementation;
- broader synthetic/adversarial fixtures;
- private transition evidence;
- internal CI, manifests, reports and evidence bundles;
- credentials, private operating records and other material that cannot responsibly be public.

Private existence is **not** the same thing as public independent verification. Where a claim depends on private-only artifacts, this repository labels that limitation instead of asking a reviewer to infer proof from narrative.

## Current bounded technical claims

The project can currently support these limited statements:

- an explicit contract-based evidence evaluation mechanism exists;
- a public executable subset exposes 3 real contract checks and adversarial behavior;
- the private reference implementation currently contains 17 explicit contract checks;
- internal regression/CI programs exist and preserve failures/partials rather than rewriting them;
- real public-source evidence and sanitized real-world transition incidents have been used to challenge the rules;
- some incident classes have become regression-backed candidates while other gaps remain explicitly unpromoted;
- production deployment and external-customer outcomes are not proven by these artifacts.

## Context, architecture and story

These pages provide context. They are **not substitutes for technical evidence**:

- [Architecture](ARCHITECTURE.md)
- [Conceptual Map](CONCEPTUAL_MAP.md)
- [Project Map](PROJECT_MAP.md)
- [Founder Story](FOUNDER_STORY.md)
- [Local AI Lab](LOCAL_AI_LAB.md)

## Public operating surface

GoNica Marketing has a live public website at **https://gonicamarketing.com/** and is exploring pilot relationships around operational continuity for acquisitions and complex business-system transitions.

This is business-development activity, not proof of production customers, revenue, or enterprise deployment.

## Evidence discipline

This repository distinguishes:

- **BUILT** — implemented in some form;
- **INTERNAL-TESTED** — exercised against project-authored tests;
- **PUBLICLY-AUDITABLE** — enough artifact/code is exposed for an outside reviewer to inspect or reproduce selected behavior;
- **OBSERVED** — supported by sanitized real-world evidence without implying GoNica production deployment;
- **OWNER-ACCEPTED** — explicitly accepted by the owner;
- **PRODUCTION-READY** — separately authorized for live production use.

A passing internal test is not independent validation. A sanitized case is not a customer claim. A public explanation is not evidence unless the underlying artifact can also be inspected or its limitation is stated.

## Why this repository exists

It is for engineers, technical reviewers, potential co-founders, accelerators, partners, mentors and pilot partners who want to examine the project without receiving the private control plane.

The standard for this repository is now simple:

> **Show the artifact when it can be shown. State the limitation when it cannot. Do not replace missing evidence with narrative.**
