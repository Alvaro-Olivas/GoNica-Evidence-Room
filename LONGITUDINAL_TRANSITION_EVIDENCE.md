# Longitudinal Business-System Transition Evidence

**Public status:** SANITIZED OBSERVATIONAL EVIDENCE + REGRESSION-DERIVED LEARNING  
**Evidence window:** June–August 2026  
**Production claim:** NONE

This page describes a sanitized real-world evidence stream that has become one of the most useful inputs to GoNica Brain.

The underlying private evidence follows a service company moving from a legacy CRM into a new operating platform with document, calendar, storage, communications and other connected systems. The public version intentionally removes company names, implementation-vendor names, employee/customer identities, phone numbers, email addresses, credentials and raw private messages.

The purpose is not to criticize an implementation provider. The purpose is to study **how operational continuity actually breaks and gets repaired over time**.

## Why longitudinal evidence matters

A one-time migration screenshot can show a bug. A multi-week transition record can show something more valuable:

```text
EARLY ACCESS
→ ROLLOUT DECISION
→ COMPANY USE
→ OPERATIONAL GAPS
→ REMEDIATION
→ NEW REQUIREMENTS
→ LATER AUTOMATION / AI EXPANSION
```

The private evidence currently spans early access, company rollout, continuing user reports, remediation work and later capability expansion.

That makes it possible to distinguish:

- migration defects;
- unfinished implementation work;
- source-data problems;
- destination-platform limitations;
- integration behavior;
- user-interface/work-surface differences;
- ordinary post-cutover optimization;
- genuinely new business requirements.

## Three incident classes already converted into regression-backed learning

### 1. Duplicate downstream storage side effects

Observed pattern:

A document-signing workflow could create a second customer/project folder structure or duplicate subfolders when the intended business outcome was a single persistent structure created only under the correct qualifying event.

Generalized lesson:

**AUTOMATION FIRES != AUTOMATION IS OPERATIONALLY CORRECT**

Existing Brain controls already cover the relevant dimensions:

- business-event identity versus retry/transport attempt;
- stable naming/locator identity;
- cross-system process reconciliation and idempotency.

A sanitized regression now verifies that duplicate business side effects are treated as a failure condition rather than a successful automation run.

### 2. Overbroad conversation / data visibility

Observed pattern:

During unresolved assignment/access conditions, users could see communications that were not relevant to their role.

Generalized lesson:

**UNASSIGNED OR AMBIGUOUS OWNERSHIP MUST NOT SILENTLY BROADEN DATA ACCESS.**

A sanitized regression now verifies that known identity or record presence does not itself authorize data exposure.

### 3. Lifecycle/business-class ambiguity

Observed pattern:

Users could find records but could not reliably distinguish the operational meaning of lead, active customer, lost record or related lifecycle state after the move into a broader contact surface.

Generalized lesson:

**CONTACT EXISTS != BUSINESS LIFECYCLE MEANING PRESERVED**

A sanitized regression now verifies that an incomplete lifecycle mapping cannot be treated as a completed transition.

## Three important coverage gaps discovered by the same evidence

The correct response to new evidence is not to invent a new permanent rule every time something looks interesting. The current Brain learning pipeline therefore keeps several findings in `REGRESSION_PENDING` state.

### A. Source-to-destination record cardinality and state parity

Observed pattern:

Multiple source business objects could be represented by the wrong number or wrong surviving destination objects, with lifecycle state also differing.

Candidate requirement:

For each material object family, reconcile:

- source count;
- destination count;
- canonical identity;
- merge/split decisions;
- excluded-record disposition;
- source lifecycle state;
- destination lifecycle state.

Status: **coverage-gap candidate — not yet a canonical Brain contract.**

### B. Whole-company stakeholder coverage before rollout

Observed pattern:

A system can appear ready around sales while production/admin or other departments still lack critical work surfaces, documents, tasks, payments, permits, inspections, project updates or other capabilities.

Candidate rule:

**SALES WORKFLOW READY != WHOLE COMPANY READY**

Status: **readiness-gate/contract candidate — not yet promoted.**

### C. Employee task work-method parity

Observed pattern:

The destination platform can have a task object while the employee's relied-upon categories, statuses, filters, ownership views and personal work organization are still missing.

Candidate rule:

**TASK OBJECT EXISTS != TASK WORK METHOD PRESERVED**

Status: **partial current coverage; dedicated regression design still pending.**

## What this changed in GoNica Brain

The evidence was not copied into model weights and was not treated as free-form memory.

The governed learning path remains:

```text
PRIVATE EVIDENCE
→ STRUCTURED INCIDENT
→ ROOT CAUSE
→ GENERALIZED RULE
→ MIGRATION REQUIREMENT
→ REGRESSION TEST
→ VALIDATED CANDIDATE
→ OPTIONAL OWNER/GOVERNANCE PROMOTION
```

Three sanitized incident-derived regressions have passed the private Control Plane validation gate under existing contracts. Three broader gap candidates remain unpromoted.

## What this evidence does not prove

It does not prove:

- that every observed problem was caused by the implementation provider;
- that the destination platform itself was at fault in every case;
- that GoNica Brain was deployed in production for this transition;
- that GoNica repaired the live company's systems;
- that the observed company is a GoNica customer;
- that the pending gap candidates should automatically become permanent contracts.

Some incidents may reflect source data, incomplete work, platform limitations, third-party behavior, user workflow, or later requirements. That distinction is deliberately preserved.

## Why this matters

The most important product lesson is increasingly concrete:

> **The migration unit is not the database. It is the operating business process.**

Operational continuity requires preserving and testing identity, relationships, work methods, ownership, time, documents, storage, calendars, communications, permissions, business events, human handoffs and downstream effects together.

That is the problem GoNica Brain is being built to inspect and govern.

---

Return to the [CRM Migration Case Study](CRM_MIGRATION_PRESERVATION_CASE_STUDY.md), [Selected Validation Evidence](SELECTED_VALIDATION_EVIDENCE.md), or [main Evidence Room](README.md).
