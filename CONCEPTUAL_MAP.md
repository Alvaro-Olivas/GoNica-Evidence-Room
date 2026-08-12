# GoNica Conceptual Map

This is the lightweight conceptual view of the project. It is intentionally rendered in Mermaid so it can be inspected directly in GitHub without image files.

```mermaid
flowchart TD
    A[Founder / Owner\nDefines goals and approves consequential actions] --> B[GoNica Brain\nGovernance + business memory + evidence + reasoning]

    I[Company reality\nCRM exports\nfiles\nnotes\nworkflows\ncustomer history\noperating rules] --> B

    B --> C[Understand\nMap the company\nPreserve relationships\nIdentify missing decisions]
    B --> D[Plan\nMigration maps\nfield/tag registries\nworkflow plans\nimplementation blueprint]
    B --> E[Govern\npermissions\nhuman approval\ntests\naudit trail\nrollback boundaries]
    B --> F[Coordinate controlled execution\nGoHighLevel / APIs / tools]

    C --> G[GoNica Marketing\nReusable implementation + onboarding + packaging]
    D --> G
    E --> G
    F --> G

    G --> H[Client / operating company deployment]
    H --> J[GoNica Tours\nFirst operating proof environment]

    B --> K[Local AI Lab\nModel experiments + hardware constraints]

    L[Evidence Room\nPublic sanitized inspection surface] --- B
    L --- G
    L --- J
    L --- K
```

## The problem in one line

A company can move its contacts to a new system and still lose how the company actually works.

## The GoNica thesis

The useful unit of migration is not only the record. It is the record **plus its context, relationships, operating rules, history, workflow logic, exceptions, approvals, and evidence**.

## The three-layer operating model

```mermaid
flowchart LR
    B[GoNica Brain\nUnderstand + govern + remember] --> M[GoNica Marketing\nAssemble + implement + reuse]
    M --> T[GoNica Tours\nFirst real operating proof]
```

- **GoNica Brain** is the intelligence, governance, evidence, continuity, and decision layer.
- **GoNica Marketing** turns proven structures into repeatable implementations and deployment packages.
- **GoNica Tours** is the first real company environment used to prove, break, correct, and improve the system.

## Company-transition flow

```mermaid
flowchart LR
    S[Existing company / legacy systems] --> R[Discovery + data intake]
    R --> P[Preserve raw information]
    P --> M[Map fields, relationships, rules, workflows]
    M --> Q[Identify gaps + owner decisions]
    Q --> T[Test target structure]
    T --> A[Owner approval]
    A --> X[Controlled execution]
    X --> V[Validate + document + preserve evidence]
```

The objective is not unrestricted AI automation. The objective is **controlled leverage**: use AI to understand, prepare, classify, compare, and suggest while preserving a clear owner-approval boundary for consequential actions.
