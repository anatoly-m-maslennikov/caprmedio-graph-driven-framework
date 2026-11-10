---
atom_id: CA-R-2650
ref_id: CA-R-2650@1
role: Requirement
form: Scope Unit Declaration
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
tier: 3
status: Archived
version: 1
updated_at: 2026-11-02 19:07:49 +0400
carrier_destination:
  file:
    name: CA-R-2650@1-METHODOLOGY_SOURCES-DEFINES_SCOPE_FOR-CORE_META_MODEL--declare-core-meta-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/04_requirement/archive
---
## Summary

Declare CORE_META_MODEL

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//CORE_META_MODEL.ID == "CA-SU-11";

Scope Unit//CORE_META_MODEL.Name == "CORE_META_MODEL";

Scope Unit//CORE_META_MODEL.Label == "LAYER";

Scope Unit//CORE_META_MODEL.order.ordered == true;

Scope Unit//CORE_META_MODEL.order.number == 1;

Scope Unit//CORE_META_MODEL ((IS_CONTAINED_BY)) Scope Unit//METHODOLOGY_SOURCES
```

