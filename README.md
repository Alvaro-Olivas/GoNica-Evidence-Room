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

## External adversarial review and correction cycle — August 19-20, 2026

The public subset did what an evidence room is supposed to do: it gave an outside reviewer enough implementation detail to find a real defect.

In the first public B09-08 implementation, a partially populated business-event item could inherit permissive defaults for missing attempt/side-effect evidence and incorrectly reach `PASS`. That violated the project doctrine:

`MISSING EVIDENCE != PASS`

The public evaluator was corrected and regression-covered. The review then expanded against pasted/private source artifacts and found the same **present-but-incomplete evidence** risk in additional private checks.

A bounded private remediation followed. Project-authored CI on the remediation pull request recorded:

- one authoritative deterministic check path for all 17 private checks;
- actual Draft 2020-12 JSON Schema validation before deterministic evaluation;
- two adversarial vectors across the 17-contract private registry: explicit contradiction and present-but-incomplete evidence;
- `41/41` private Brain tests passing on the remediation PR;
- corrected/stress R3 fixtures preserving their expected bounded states;
- `production_authorized:false` throughout.

The seven sanitized public-source dossiers were also rerun under the hardened private engine. The aggregate remained unchanged:

`119 = 0 PASS / 30 PARTIAL / 6 FAIL / 83 UNKNOWN / 0 NOT_APPLICABLE`

That unchanged result is useful because it shows the known false-PASS class did not alter this particular historical batch. It does **not** prove the defect was harmless for other inputs.

Important boundary: the external reviewer performed adversarial source review from artifacts supplied in text. That is meaningful external scrutiny, but it is **not** independent third-party execution of the full private engine.

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

Historical private counts such as `21/21 PASS` or `9/9 PASS`, and the later remediation-PR count `41/41 PASS`, mean the implementation satisfied the tests defined at those respective savepoints. They do **not** prove that the tests are complete, correctly calibrated, or resistant to every external challenge.

That distinction is not theoretical: an outside reviewer found a real missing-evidence defect despite earlier green internal suites. The correction cycle is therefore evidence for the value of external challenge, not evidence that green CI alone proves correctness.

## Real-evidence corpus result: how to read 0/119 PASS

Seven public-source evidence sets were evaluated against the broader private 17-contract engine. The aggregate was:

- 119 contract evaluations;
- 30 `PARTIAL`;
- 6 `FAIL`;
- 83 `UNKNOWN`;
- 0 `PASS`.

The same seven sanitized dossiers were rerun after the August 20 missing-evidence/schema remediation and produced the same aggregate.

This is **not presented as a success rate** and should not be read as proof that the engine is well calibrated. The source documents were not complete migration dossiers, so many contracts lacked enough evidence to pass. The engine kept missing facts as `UNKNOWN`.

At the same time, `0/119 PASS` remains a legitimate calibration question for external reviewers: are the contracts appropriately strict, are the evidence requirements practical, and does the engine distinguish useful signal from missing context? That question remains open to challenge rather than being explained away as automatically positive.

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
- the private reference implementation contains 17 explicit deterministic contract checks;
- an external adversarial review found a real missing-evidence defect and triggered a bounded correction cycle;
- the private remediation added systematic present-but-incomplete regressions and real schema enforcement, with project-authored CI green on the remediation PR;
- the seven-source sanitized corpus rerun was unchanged after that remediation;
- internal regression/CI programs preserve failures/partials rather than rewriting them;
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

GoNica Marketing has a live public website at **https://gonicamarketing.com/** and is exploring pilot relationships around operational continuity for business-system transitions.

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

The standard for this repository is simple:

> **Show the artifact when it can be shown. State the limitation when it cannot. Do not replace missing evidence with narrative.**
