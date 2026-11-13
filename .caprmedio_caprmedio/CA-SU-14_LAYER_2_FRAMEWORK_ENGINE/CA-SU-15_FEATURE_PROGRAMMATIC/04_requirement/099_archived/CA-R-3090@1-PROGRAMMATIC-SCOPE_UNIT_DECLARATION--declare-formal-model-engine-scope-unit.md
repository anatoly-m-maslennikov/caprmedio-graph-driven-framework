---
identity:
  atom_id: CA-R-3090
  ref_id: CA-R-3090@1
context:
  role: requirement
  form: scope_unit_declaration
  tier: 3
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T12:51:34.463530+00:00'
destination:
  file:
    name: CA-R-3090@1-PROGRAMMATIC-SCOPE_UNIT_DECLARATION--declare-formal-model-engine-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/099_archived
---
## Summary

Declare FORMAL MODEL ENGINE Scope Unit

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//FORMAL_MODEL_ENGINE.ID == "CA-SU-50";

Scope Unit//FORMAL_MODEL_ENGINE.Name == "FORMAL_MODEL_ENGINE";

Scope Unit//FORMAL_MODEL_ENGINE.Label == "FEATURE";

Scope Unit//FORMAL_MODEL_ENGINE.order.ordered == false;

Scope Unit//FORMAL_MODEL_ENGINE ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```
