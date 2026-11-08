---
identity:
  atom_id: CA-R-2730
  ref_id: CA-R-2730
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Active
  version: 2
  updated_at: 2026-11-08 22:18:08 +0400
destination:
  file:
    name: CA-R-2730-APPS-SCOPE_DELEGATION--declare-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
---
## Summary

Declare WORKBENCH

## Claim

The additional admitted local Role/Form pairs are exactly: Requirement/Solution, Requirement/Direct Policy, Method/Direct Policy and Delivery/Solution. Existing default admissions under CA-R-3008 continue to apply.

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared model entities or declared instances resolved at these existing active Subject addresses:

- CAPRMEDIO_MODEL <+ Projection
- CAPRMEDIO_MODEL <+ Project
- CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_BACKEND
- CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_FRONTEND
- CAPRMEDIO_STRUCTURE <+ Scope Unit//CODEX_EXTENSION
- Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure

Each entry selects that single endpoint object. It does not select the address string, other members of its type, or descendants. An unresolved entry remains a diagnostic and grants no admission.

These permissions apply only to Atoms whose Header.Container-derived IS_CONTAINED_BY target is WORKBENCH.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH.ID == "CA-SU-43";

Scope Unit//WORKBENCH.Name == "WORKBENCH";

Scope Unit//WORKBENCH.Label == "APP";

Scope Unit//WORKBENCH.order.ordered == false;

Scope Unit//WORKBENCH ((IS_CONTAINED_BY)) Scope Unit//APPS
```
