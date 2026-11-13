---
atom_id: CA-R-2537
ref_id: CA-R-2537@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.ID
tier: 3
status: archived
version: 3
updated_at: 2026-11-04 07:51:19 +0400
carrier_destination:
  file:
    name: CA-R-2537@3-CORE_META_MODEL-DECLARATION--declare-projection-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection.ID

## Claim

### Formal Claim

```CFEL
# model
Projection.ID{::1}:: [string]{::1};

Projection.ID.*[]{::0};

# instances
DETERMINES(Projection//$projection, (.Form, .Scope Unit), (.ID));

DETERMINES(Projection//$projection_2, (.ID), (.Form, .Scope Unit))
```

