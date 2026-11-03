---
atom_id: CA-R-2554
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.structural_level
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Scope Unit.structural_level

## Claim

```CFEL
Scope Unit.structural_level{:1}: [int]{:1};
Scope Unit.structural_level.*[]{:0};
Scope Unit.structural_level >= 0;
Scope Unit/Project//$project.structural_level = 0;
IF (Scope Unit//$contained ((IS_CONTAINED_BY)) Scope Unit//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```
