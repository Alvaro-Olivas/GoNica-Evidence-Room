# Selected Validation Evidence

This page exposes a small set of concrete, sanitized validation results from the private GoNica evidence base.

The numbers below are not a claim that GoNica is finished or production-ready. They show that selected components have been exercised under defined conditions and that test state is kept separate from production authorization.

## 1. Governed GoHighLevel bridge

**Status:** `TESTED`

Selected historical validation:
- **28 / 28** governed bridge tests passed.
- synthetic acceptance test: **PASS**;
- package / hash checks: **PASS**;
- secret scan: **CLEAR**;
- live evidence used a **read-only** path before any bounded synthetic-write authorization.

What this supports:
- the bridge exists as more than a design concept;
- governance controls were exercised;
- read-only-first behavior is part of the operating method.

What this does **not** support:
- unrestricted production write access;
- autonomous customer changes;
- a claim that every HighLevel operation has been validated;
- a claim that the currently prepared R3.5 live-validation package has already been executed.

## 2. Earlier GoNica Brain benchmark program

**Status:** `TESTED — SYNTHETIC / SANITIZED`

An earlier structured benchmark program executed **46** synthetic or sanitized cases, including preflight.

Results:
- **41 PASS**
- **5 PARTIAL**
- **0 FAIL**
- **0 critical governance failures**
- approximate weighted result: **96.2 / 100**

The benchmark deliberately tested more than answer quality. Cases included unknown/conflict handling, unsafe owner requests, budget and workload constraints, dependency drift, consent boundaries, identity conflicts, recovery behavior, reusable-system separation and evidence provenance.

The five partial results were not discarded. They were converted into design corrections and regression requirements.

## 3. Operational-continuity regression program

**Status:** `TESTED — SYNTHETIC / CONTROLLED`

A later operational-continuity program focused on what a business can lose when people, records, tasks, documents, calendars, notifications and multiple systems must continue to work together.

Original controlled executions:
- **72 total**
- **59 PASS**
- **13 PARTIAL**
- **0 FAIL**

Seven correction contracts were then defined around discovered gaps, covering identity history, naming/locator continuity, time-based obligations, notification routing, calendar meaning, actor/sender provenance, and cross-system process reconciliation.

Targeted correction regressions:
- **13 additional executions**
- **13 PASS**
- **0 PARTIAL**
- **0 FAIL**

Cumulative evidence history:
- **85 controlled executions**
- original results remain unchanged;
- targeted correction results are recorded separately.

What this supports:
- the project can discover operational-continuity gaps, formalize corrections, and retest them;
- GoNica treats relationships, time, identity, routing and human/system handoffs as business requirements rather than merely fields to copy;
- evidence history is preserved instead of rewritten after a correction.

## 4. Current Brain reference engine — R3/R3.5

**Status:** `BUILT + TESTED — OFFLINE / SYNTHETIC OR SANITIZED`

The current private reference implementation includes:
- a canonical registry of **17 operational-continuity and governance contracts**;
- all **17 provider-neutral deterministic reference checks**;
- structured synthetic company fixtures, including corrected and conflict/stress cases;
- a controlled incident-to-regression learning path;
- human-readable analysis reporting;
- hash-verifiable evidence bundles;
- a one-command candidate-review demo;
- sanitized templates prepared for future live evidence capture, adapter comparison and owner decisions.

Brain unit tests are included in the standard private Control Plane validation workflow before manifest reconciliation.

The R3.5 live-evidence templates begin in `NOT_RUN` or `PENDING` states. Their existence does not mean a current live session or production approval has occurred.

## 5. Real-evidence transition corpus — August 18

**Status:** `EVALUATED — PUBLIC SOURCE EVIDENCE / OFFLINE`

The private control plane evaluated seven acquired/normalized public-source datasets through the existing 17-contract engine.

Sanitized aggregate:

- **7 sources** acquired and normalized;
- **119 contract evaluations**;
- **0 PASS**;
- **30 PARTIAL**;
- **6 FAIL**;
- **83 UNKNOWN**;
- **7/7 evidence bundles verified**;
- **4 governed learning candidates**, all unpromoted;
- existing Brain test suite: **21/21 PASS**;
- corpus regression suite: **9/9 PASS**;
- Brain architecture/canonical contract set changed: **no**;
- training/fine-tuning: **none**.

Why `0 PASS` in the source evaluations is not a system failure:

The public sources were not complete migration dossiers. The engine evaluates whether evidence proves each contract. Missing facts remain `UNKNOWN`, partial support remains `PARTIAL`, and explicit conflicts can become `FAIL`. The evaluation therefore demonstrates conservative evidence handling rather than a tendency to fabricate success.

What this supports:
- the same contract engine can be applied to real public evidence rather than only handcrafted fixtures;
- incomplete evidence stays incomplete;
- learning candidates can emerge without changing architecture or granting production authority.

What this does **not** support:
- proof that the source organizations completed successful migrations;
- proof of live enforcement inside those organizations;
- proof of GoNica production deployment.

## 6. Incident-derived longitudinal regressions — August 19

**Status:** `REGRESSION-BACKED VALIDATED RULE CANDIDATES`

A separate sanitized, real-world transition evidence stream spanning multiple weeks generated three new regressions against the existing Brain contracts.

Validated incident classes:

1. **Duplicate downstream business/storage side effects** — a repeated, renamed or non-qualifying event must not create additional persistent business outcomes.
2. **Overbroad conversation/data visibility** — unresolved assignment or known identity must not silently authorize broader access.
3. **Lifecycle/business-class ambiguity** — discoverable records with missing business-state meaning are not a completed transition.

The regressions passed the private repository's standard Control Plane validation path. They are therefore treated as regression-backed rule candidates under existing contracts, not as new permanent contracts.

The same evidence exposed additional gap candidates that remain pending:

- source/destination record cardinality + lifecycle-state parity;
- whole-company stakeholder/department readiness before rollout;
- task work-method parity beyond task-object existence.

See [Longitudinal Business-System Transition Evidence](LONGITUDINAL_TRANSITION_EVIDENCE.md).

## 7. CRM migration / preservation validation — one use case

**Status:** `TESTED — SELECTED OFFLINE CASES + SANITIZED OBSERVATIONAL LEARNING`

Selected validation demonstrated that CRM transition work was treated as more than contact transfer. Tests covered preservation/mapping behavior and field disposition in defined offline cases, while later observational evidence added real failure patterns around identity, business state, automation side effects, access, tasks and cross-system relationships.

The core validation question is:

> Can the target operating model preserve the information, relationships and work behavior needed to continue the company, rather than merely producing a smaller contact file?

This work supports a broader GoNica principle:

**DATA MIGRATION IS NOT THE SAME AS OPERATIONAL MIGRATION.**

## 8. Production gate discipline

A recurring GoNica rule is:

```text
PASSING TEST != PRODUCTION AUTHORIZATION
```

Components can remain intentionally blocked after successful technical testing because production use requires a separate owner decision, credentials/scopes, privacy checks, tenant boundaries, rollback readiness or business approval.

## Why numerical evidence is being released selectively

The private control plane contains substantially more detailed logs, fixtures and operational records. Public evidence is deliberately reduced so reviewers can inspect the engineering discipline without exposing customer information, private CRM data, credentials, internal access paths, employer-confidential material or unrestricted operational strategy.
