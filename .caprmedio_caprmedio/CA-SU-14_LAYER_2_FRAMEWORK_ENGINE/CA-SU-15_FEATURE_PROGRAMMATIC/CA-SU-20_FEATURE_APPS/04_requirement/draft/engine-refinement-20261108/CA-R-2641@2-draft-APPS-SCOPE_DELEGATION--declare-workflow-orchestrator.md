---
identity:
  atom_id: CA-R-2641
  ref_id: CA-R-2641@2-draft
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKFLOW_ORCHESTRATOR
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Draft
  version: 2
  updated_at: 2026-11-08 20:11:06 +0400
destination:
  file:
    name: CA-R-2641@2-draft-APPS-SCOPE_DELEGATION--declare-workflow-orchestrator.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/draft/engine-refinement-20261108
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

