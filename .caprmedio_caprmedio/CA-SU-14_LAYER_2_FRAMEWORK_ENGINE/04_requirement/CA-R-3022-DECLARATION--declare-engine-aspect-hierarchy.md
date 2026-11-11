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
  version: 3
  updated_at: '2026-11-11T16:56:16+04:00'
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

Frontend Engineering covers frontend construction. Libraries and Frameworks covers library, framework and build-tool choices; Component Authoring covers Svelte components and TypeScript; Code Style covers source organization, formatting and responsibility boundaries. Visual Design, query authoring and interface contracts retain their distinct topics.

### Formal Claim

```CFEL
# instances
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Change Readiness;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Reproducibility;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ API;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring <+ Python Code;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Controlled English;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Code Style;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Component Authoring;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Libraries and Frameworks;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Configuration;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Code Hot Reload;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Outcome Reporting;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Recovery;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Resource Limits;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability <+ Provenance;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing <+ Canary Testing;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis <+ Python Code;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Data <+ Golden Corpora;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Product;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Guidance;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Accessibility;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision;
PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status Presentation;

(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Change Readiness) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Reproducibility) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ API) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring <+ Python Code) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Controlled English) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Code Style) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Component Authoring) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Libraries and Frameworks) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Configuration) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Code Hot Reload) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Outcome Reporting) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Recovery) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Resource Limits) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability <+ Provenance) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing <+ Canary Testing) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis <+ Python Code) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Data) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Data <+ Golden Corpora) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Product) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Guidance) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Accessibility) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision) ((INSTANCE_OF)) Aspect;
(PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status Presentation) ((INSTANCE_OF)) Aspect;
```
