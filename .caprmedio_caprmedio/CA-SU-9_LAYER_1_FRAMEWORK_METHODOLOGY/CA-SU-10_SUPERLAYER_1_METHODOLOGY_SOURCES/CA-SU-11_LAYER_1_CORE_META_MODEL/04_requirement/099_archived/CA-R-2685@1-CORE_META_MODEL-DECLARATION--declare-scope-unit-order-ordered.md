---
atom_id: CA-R-2685
ref_id: CA-R-2685@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order
  - CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 19:17:40 +0400
destination:
  file:
    name: CA-R-2685@1-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Declare Scope Unit.order.ordered

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.order.ordered:: [bool]{::1};

Scope Unit.order.ordered.*[]{::0}
```

