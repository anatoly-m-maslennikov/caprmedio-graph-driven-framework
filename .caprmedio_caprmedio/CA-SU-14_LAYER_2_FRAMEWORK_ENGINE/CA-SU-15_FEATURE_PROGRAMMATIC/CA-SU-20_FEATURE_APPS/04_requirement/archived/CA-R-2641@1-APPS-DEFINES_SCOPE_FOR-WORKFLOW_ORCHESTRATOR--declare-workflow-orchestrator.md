---
atom_id: CA-R-2641
ref_id: CA-R-2641@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_ORCHESTRATOR
tier: 3
status: Archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
destination:
  file:
    name: CA-R-2641@1-APPS-DEFINES_SCOPE_FOR-WORKFLOW_ORCHESTRATOR--declare-workflow-orchestrator.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archived
---
## Summary

Declare WORKFLOW_ORCHESTRATOR

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_ORCHESTRATOR.ID == "CA-SU-2";

Scope Unit//WORKFLOW_ORCHESTRATOR.Name == "WORKFLOW_ORCHESTRATOR";

Scope Unit//WORKFLOW_ORCHESTRATOR.Label == "APP";

Scope Unit//WORKFLOW_ORCHESTRATOR.order.ordered == false;

Scope Unit//WORKFLOW_ORCHESTRATOR ((IS_CONTAINED_BY)) Scope Unit//APPS
```

