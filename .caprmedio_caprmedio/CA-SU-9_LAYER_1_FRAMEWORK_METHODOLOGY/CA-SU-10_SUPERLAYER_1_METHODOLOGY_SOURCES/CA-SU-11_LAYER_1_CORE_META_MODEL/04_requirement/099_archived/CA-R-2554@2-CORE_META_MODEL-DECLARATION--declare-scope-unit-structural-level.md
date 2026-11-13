---
atom_id: CA-R-2554
ref_id: CA-R-2554@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.structural_level
tier: 3
status: archived
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2554@2-CORE_META_MODEL-DECLARATION--declare-scope-unit-structural-level.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Scope Unit.structural_level

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.structural_level{::1}:: [int]{::1};

Scope Unit.structural_level.*[]{::0};

Scope Unit.structural_level >= 0;

# instances
Scope Unit/Project//$project.structural_level = 0;

IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```

