---
identity:
  atom_id: CA-R-2654
  ref_id: CA-R-2654@3
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROGRAMMATIC
  tier: 3
  container:
    scope_unit: CA-SU-14
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-R-2654@3-FRAMEWORK_ENGINE-SCOPE_DELEGATION--declare-programmatic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/archive
---

## Summary

Declare PROGRAMMATIC

## Claim

### Prose Claim

The receiving Scope Unit is PROGRAMMATIC. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Delivery / Direct Policy;
- Evaluation / Approach Policy;
- Evaluation / Direct Policy;
- Evaluation / Solution;
- Method / Direct Policy;
- Method / Solution;
- Requirement / Direct Policy;
- Requirement / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//APPS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//CONNECTOR_TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//MCP`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOL_WORKFLOWS`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Change Readiness`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Reproducibility`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface Contracts`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code Authoring`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code Authoring/Python Code`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Configuration`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Code Hot Reload`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Failure Handling`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Outcome Reporting`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Resource Limits`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Observability/Logging`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Temporary State`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Performance/Measurement and Profiling`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Traceability`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Traceability/Provenance`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Coverage`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing/Canary Testing`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis/Python Code`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Test Design`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Temporary State`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to PROGRAMMATIC. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//PROGRAMMATIC.ID == "CA-SU-15";

Scope Unit//PROGRAMMATIC.Name == "PROGRAMMATIC";

Scope Unit//PROGRAMMATIC.Label == "FEATURE";

Scope Unit//PROGRAMMATIC.order.ordered == false;

Scope Unit//PROGRAMMATIC ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_ENGINE
```
