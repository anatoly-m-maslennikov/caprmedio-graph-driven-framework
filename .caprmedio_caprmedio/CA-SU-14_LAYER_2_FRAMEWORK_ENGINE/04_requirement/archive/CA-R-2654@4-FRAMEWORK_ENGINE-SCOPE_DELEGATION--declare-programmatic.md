---
identity:
  atom_id: CA-R-2654
  ref_id: CA-R-2654
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROGRAMMATIC
  tier: 3
  container:
    scope_unit: CA-SU-14
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2654-FRAMEWORK_ENGINE-SCOPE_DELEGATION--declare-programmatic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare PROGRAMMATIC

## Claim

### Prose Claim

The receiving Scope Unit is PROGRAMMATIC. The additional local Role/Form pairs are exactly:

- Delivery / Direct Policy;
- Evaluation / Approach Policy;
- Evaluation / Direct Policy;
- Evaluation / Solution;
- Method / Direct Policy;
- Method / Solution;
- Requirement / Direct Policy;
- Requirement / Goal;
- Requirement / Solution;

- Delivery / Solution;

- Concern / Question;
- Requirement / Rule;

- Concern / Problem;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `MODEL//CAPRMEDIO <+ Scope Unit`;

- `MODEL//CAPRMEDIO <+ Atom`;
- `MODEL//CAPRMEDIO <+ Projection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_HOOK`;


- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CONNECTOR_TOOLS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//MCP`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROJECT_TOOLS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOL_WORKFLOWS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Change Readiness`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Reproducibility`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring <+ Python Code`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Configuration`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Code Hot Reload`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Outcome Reporting`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Resource Limits`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability <+ Provenance`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing <+ Canary Testing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis <+ Python Code`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status Presentation`;
- `MODEL//CAPRMEDIO <+ Project.Settings.Temporary State`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging`;

### Formal Claim

```CFEL
# instances
Scope Unit//PROGRAMMATIC.ID == "CA-SU-15";

Scope Unit//PROGRAMMATIC.Name == "PROGRAMMATIC";

Scope Unit//PROGRAMMATIC.Label == "FEATURE";

Scope Unit//PROGRAMMATIC.order.ordered == false;

Scope Unit//PROGRAMMATIC ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_ENGINE
```
