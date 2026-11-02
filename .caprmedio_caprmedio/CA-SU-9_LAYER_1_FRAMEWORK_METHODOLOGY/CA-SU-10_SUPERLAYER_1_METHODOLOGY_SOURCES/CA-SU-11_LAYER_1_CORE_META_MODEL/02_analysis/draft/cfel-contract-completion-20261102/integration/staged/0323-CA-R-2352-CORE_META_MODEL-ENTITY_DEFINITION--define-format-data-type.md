---
atom_id: CA-R-2352
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format.Data Type
version: 4
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Format Data Type

## Claim

Format Data Type names the admissible value domain of a direct Property value.
It is separate from cardinality. The initial vocabulary is provisional; list,
map and reference semantics remain with the governing Format definition.


```CFEL
Format.Data Type{:1}: [string]{:1};
Format.Data Type.*[]{:0}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in the governing
Format Definition.
