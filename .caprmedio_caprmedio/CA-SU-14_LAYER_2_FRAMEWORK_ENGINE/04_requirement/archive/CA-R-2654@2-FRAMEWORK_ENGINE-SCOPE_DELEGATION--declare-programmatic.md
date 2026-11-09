---
identity:
  atom_id: CA-R-2654@2
  ref_id: CA-R-2654@2
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
  version: 2
  updated_at: 2026-11-08 22:18:08 +0400
destination:
  file:
    name: CA-R-2654@2-FRAMEWORK_ENGINE-SCOPE_DELEGATION--declare-programmatic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/archive
---
## Summary

Declare PROGRAMMATIC

## Claim

### Prose Claim

PROGRAMMATIC admits the following local Role/Form pairs, in addition to existing default admissions:

- Delivery / Decision;
- Delivery / Direct Policy;
- Evaluation / Direct Policy;
- Evaluation / Eval Case;
- Method / Decision;
- Method / Direct Policy;
- Requirement / Direct Policy;
- Requirement / Scope Delegation;
- Requirement / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared model entities or declared instances resolved at these existing active Subject addresses:

- `CAPRMEDIO_STRUCTURE <+ Scope Unit//APPS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//CONNECTOR_TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//MCP`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOLS`;
- `CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOL_WORKFLOWS`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python Code`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis/Python Code`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Test Design`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings.Temporary State`;

Each entry selects that one endpoint object, not the address string, other members of its type, or descendants. An unresolved entry remains a diagnostic and grants no admission. These permissions apply only to Atoms whose Header.Container-derived IS_CONTAINED_BY target is Scope Unit//PROGRAMMATIC.

### Formal Claim

```CFEL
# instances
Scope Unit//PROGRAMMATIC.ID == "CA-SU-15";

Scope Unit//PROGRAMMATIC.Name == "PROGRAMMATIC";

Scope Unit//PROGRAMMATIC.Label == "FEATURE";

Scope Unit//PROGRAMMATIC.order.ordered == false;

Scope Unit//PROGRAMMATIC ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_ENGINE
```

