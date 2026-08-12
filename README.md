# GoNica Technical Evidence Room

This repository is a sanitized, read-only technical review package for **GoNica Brain**.

GoNica Brain is an early-stage business intelligence and automation architecture designed to help companies preserve how they operate when they change systems, especially during CRM transitions. It is built to organize messy company information, preserve important customer history and relationships, map data into a controlled target structure, generate migration and implementation plans, and coordinate safe, auditable execution with human approval.

## Start here

- [Project Map](PROJECT_MAP.md)
- [Architecture](ARCHITECTURE.md)
- [Validation Summary](VALIDATION_SUMMARY.md)
- [Failures and Lessons](FAILURES_AND_LESSONS.md)
- [Local AI Lab](LOCAL_AI_LAB.md)
- [Current State](CURRENT_STATE.md)

## What this repository is

This is not the private GoNica control plane. It is a deliberately reduced review surface intended for technical reviewers, accelerators, partners, hardware companies, and other people evaluating whether deeper diligence is justified.

## What is deliberately excluded

No credentials, OAuth secrets, production tokens, unrestricted private repository content, raw customer PII, private CRM databases, contact lists, or unrelated employer data are included.

## Status language

GoNica deliberately separates these states:

- **BUILT** — implemented in some form.
- **TESTED** — exercised against defined test cases.
- **OWNER-ACCEPTED** — reviewed and accepted by the owner.
- **PRODUCTION-READY** — separately authorized for live use.

A passing test is not automatically represented as production readiness.
