---
identity:
  atom_id: CA-R-3022
  ref_id: CA-R-3022
context:
  container:
    scope_unit: CA-SU-14
  role: Requirement
  form: Declaration
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO
    dependencies:
    - MODEL//CAPRMEDIO <+ Aspect
  tier: 1
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-3022-DECLARATION--declare-engine-aspect-hierarchy.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare Engine Aspect hierarchy

## Claim scope

Engineering, UX, Documentation and Product topics used by the CAPRMEDIO Engine.

## Claim

### Prose Claim

CAPRMEDIO's Project Structure contains the following project-local Aspect hierarchy. Aspects is its grouping container; the other named nodes are concrete instances of Aspect. Each indentation is direct containment, not narrowing or automatic policy inheritance. An address begins with `PROJECT STRUCTURE//CAPRMEDIO  <+  Aspects` and continues with ` <+ ` and the names along that branch.

```text
Aspects
  Documentation
    Traceability
  Engineering
    Delivery
      Change Readiness
      Packaging
      Reproducibility
    Development
      Architecture
        Communication
          API
          Interface Contracts
        Component Structure
      Authoring
        Code Authoring
          Python Code
        Controlled English
        Prompt Authoring
        Query Authoring
          SQL
      Frontend Engineering
        Code Style
        Component Authoring
        Libraries and Frameworks
    Operation
      Data Handling
        Configuration
        Data Validation
        Indexing
        Output Publication
        Query Processing
        Schema
        Serialization
        Source Retrieval
        Source Selection
        State Synchronization
      Execution Control
        Code Hot Reload
        Effect Authorization
        Failure Handling
        Outcome Reporting
        Recovery
        Resource Limits
      Observability
        Logging
      Storage
        Directory Layout
        Temporary State
    Quality
      Performance
        Measurement and Profiling
      Traceability
        Provenance
      Verification
        Coverage
        Dynamic Testing
          Canary Testing
        Static Analysis
          Python Code
        Test Data
          Golden Corpora
        Test Design
  Product
  UX
    Discovery and Navigation
    Entry
    Guidance
    Interaction
      Accessibility
      Decision
    Result and Status Presentation
```

Frontend Engineering covers frontend construction. Libraries and Frameworks covers library, framework and build-tool choices; Component Authoring covers Svelte components and TypeScript; Code Style covers source organization, formatting and responsibility boundaries. Visual Design, query authoring and interface contracts retain their distinct topics.
