---
identity:
  atom_id: CA-R-2659
  ref_id: CA-R-2659@2
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//APPS
  tier: 3
state:
  status: Archived
  version: 2
  updated_at: 2026-11-08 22:18:08 +0400
destination:
  file:
    name: CA-R-2659@2-PROGRAMMATIC-SCOPE_DELEGATION--declare-apps.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
---
## Summary

Declare APPS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//APPS.ID == "CA-SU-20";

Scope Unit//APPS.Name == "APPS";

Scope Unit//APPS.Label == "FEATURE";

Scope Unit//APPS.order.ordered == false;

Scope Unit//APPS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


### Prose Claim

The additional admitted local Role/Form pairs are `Requirement/Solution` and `Requirement/Scope Delegation`; existing default admissions remain unchanged. Eligible active targets are exactly the declared model entities or declared instances resolved at following existing active Subject addresses: `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication`, `CAPRMEDIO_STRUCTURE <+ Scope Unit//GRAPH_UI`, and `CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH`. The selection contains those exact objects, not strings, type members, or descendants; an unresolved diagnostic grants none. These permissions apply only to local Atoms whose Header.Container-derived IS_CONTAINED_BY target is Scope Unit//APPS.
