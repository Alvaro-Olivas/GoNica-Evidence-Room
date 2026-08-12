# GoNica Brain Architecture

## Corrected model

- **GoNica Brain** = reasoning, decision, documentation, governance, and business-memory layer.
- **GoHighLevel** = CRM and execution environment.
- **API / webhook bridge** = controlled connection between reasoning and execution.
- **Knowledge base** = structured company memory.
- **Tool registry** = approved actions the Brain may perform.
- **Evaluation system** = tests that prove behavior and preserve failures.
- **Snapshot / deployment package** = reusable installation output built from approved company data and rules.

## Why the separation matters

1. The company model is not locked to a single CRM.
2. Execution tools can change without rebuilding the Brain.
3. Uncertain decisions can stop for human review instead of being guessed.
4. Implementations can be tested, documented, audited, and rolled back.

## Company-transition use case

A company changing systems should not lose the operating knowledge surrounding its records.

The intended flow is:

1. ingest company files, CRM exports, and discovery material
2. profile schemas and identify the company's operating structure
3. preserve raw and important historical information
4. map data into a canonical company model
5. identify workflows, pain points, goals, exceptions, and unresolved decisions
6. produce a migration and implementation blueprint
7. compile approved fields, tags, pipelines, workflows, knowledge, and human-handoff rules
8. execute only approved actions through a controlled integration layer
9. validate the result and preserve audit evidence

The project is early-stage. Some of these capabilities are already implemented and tested in bounded environments; others remain incomplete or owner-gated.
