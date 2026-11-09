---
identity:
  atom_id: CA-R-2641
  ref_id: CA-R-2641
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_ORCHESTRATOR
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Active
  version: 4
  updated_at: 2026-11-09 17:00:18 +0400
destination:
  file:
    name: CA-R-2641-APPS-SCOPE_DELEGATION--declare-workflow-orchestrator.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
---

## Summary

Declare WORKFLOW_ORCHESTRATOR

## Claim


### Prose Claim

The receiving Scope Unit is WORKFLOW_ORCHESTRATOR. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Method / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `Subject/CAPRMEDIO/Carrier`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to WORKFLOW_ORCHESTRATOR. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_ORCHESTRATOR.ID == "CA-SU-2";

Scope Unit//WORKFLOW_ORCHESTRATOR.Name == "WORKFLOW_ORCHESTRATOR";

Scope Unit//WORKFLOW_ORCHESTRATOR.Label == "APP";

Scope Unit//WORKFLOW_ORCHESTRATOR.order.ordered == false;

Scope Unit//WORKFLOW_ORCHESTRATOR ((IS_CONTAINED_BY)) Scope Unit//APPS
```
