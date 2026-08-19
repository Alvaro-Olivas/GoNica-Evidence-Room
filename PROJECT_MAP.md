# Project Map

GoNica is not one application. It is a layered operating architecture built around one central idea: **understand and preserve the company before automating it.**

## Core structure

```mermaid
flowchart TD
    B[GoNica Brain] --> M[GoNica Marketing]
    M --> T[GoNica Tours]
    B --> E[Execution tools\nGoHighLevel / APIs / services]
    B --> K[Knowledge + evidence]
    B --> V[Validation + approvals]
    R[Real / public / sanitized evidence] --> K
    K --> B
```

## GoNica Brain

The Brain is the reasoning, governance, continuity, and evidence layer. Its job is to keep track of what the company is, how it works, what information is authoritative, what has been tested, what failed, what the owner approved, and what actions are permitted.

Representative responsibilities include:

- company-data intake and profiling;
- CRM field and relationship mapping;
- preservation of important customer information;
- migration and transition planning;
- workflow and implementation planning;
- identification of missing information and unresolved decisions;
- knowledge organization;
- tool permissions and safety boundaries;
- test and evaluation records;
- incident-to-regression learning;
- decision and continuity records.

## GoNica Marketing

GoNica Marketing is the reusable implementation and business-development layer. Its purpose is to turn proven structures into repeatable company deployments rather than rebuilding every client from zero.

The working direction includes:

- discovery and onboarding;
- CRM cleanup and migration;
- operational-continuity assessment;
- controlled field, tag, pipeline, workflow and cross-system structures;
- reusable deployment packages;
- automation and AI-assisted operations;
- validation before launch;
- documentation and handoff;
- exploratory pilot recruitment.

Public operating surface: **https://gonicamarketing.com/**

The public website and pilot-recruitment activity are business-development milestones, not production-customer claims.

## GoNica Tours

GoNica Tours is the first owner-controlled operating proof environment. It gives the project a real company against which to test website systems, CRM structures, contacts, campaigns, supplier workflows, content, operational rules, and automation.

It is not the Brain itself. It is the first company being built and operated with the broader GoNica approach.

## Execution environment

GoHighLevel and other connected tools are execution systems. They can store contacts, fields, tags, opportunities, workflows, tasks, notes, campaigns, documents, calendars and other operational objects.

The architectural principle is:

**Brain governs; tools act.**

That separation matters because the company model, rules, and evidence should not disappear if a CRM or execution platform changes.

## Evidence and learning layers

The private control plane now draws from several evidence classes:

- synthetic/control fixtures;
- selected historical live-read evidence;
- public-source transition corpus evidence;
- sanitized longitudinal real-world transition evidence;
- owner decisions, failures and corrections.

Evidence is not automatically promoted into permanent Brain rules. The intended learning path requires structured incidents, generalization, falsifiable requirements and regression evidence before promotion.

## Local AI Lab

The local-AI work is an experiment and capability layer, not the identity of GoNica. It tests what can be run locally, where hardware constraints appear, and where external compute or better hardware would create practical leverage.

## Evidence Room

This repository is the public review surface. It contains only deliberately selected and sanitized material so outside reviewers can understand the project without being given access to the private control plane.

The Evidence Room intentionally excludes raw customer/employer data, credentials, private implementation-vendor communications and unrestricted operational source material.
