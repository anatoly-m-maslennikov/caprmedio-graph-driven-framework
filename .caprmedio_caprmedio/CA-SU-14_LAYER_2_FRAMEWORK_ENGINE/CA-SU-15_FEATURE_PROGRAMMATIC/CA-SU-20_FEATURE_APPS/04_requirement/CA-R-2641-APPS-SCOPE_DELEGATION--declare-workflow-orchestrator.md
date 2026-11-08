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
  version: 2
  updated_at: 2026-11-08 23:18:49 +0400
destination:
  file:
    name: CA-R-2641-APPS-SCOPE_DELEGATION--declare-workflow-orchestrator.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
---
## Summary

Declare WORKFLOW_ORCHESTRATOR

## Claim

Within this delegation, the admitted local Role/Form pairs used by the reviewed current local RMEDO are exactly: Evaluation/Eval Case, already globally admitted by CA-R-3008. No additional Role/Form pair is admitted.

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared model entities or declared instances resolved at these existing active Subject addresses:

- Subject/CAPRMEDIO/Carrier
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
- Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
- Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Coverage
- Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit

Each entry selects that single endpoint object. It does not select the address string, other members of its type, or descendants. An unresolved entry remains a diagnostic and grants no admission.

These permissions apply only to Atoms whose Header.Container-derived IS_CONTAINED_BY target is WORKFLOW_ORCHESTRATOR.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_ORCHESTRATOR.ID == "CA-SU-2";

Scope Unit//WORKFLOW_ORCHESTRATOR.Name == "WORKFLOW_ORCHESTRATOR";

Scope Unit//WORKFLOW_ORCHESTRATOR.Label == "APP";

Scope Unit//WORKFLOW_ORCHESTRATOR.order.ordered == false;

Scope Unit//WORKFLOW_ORCHESTRATOR ((IS_CONTAINED_BY)) Scope Unit//APPS
```

