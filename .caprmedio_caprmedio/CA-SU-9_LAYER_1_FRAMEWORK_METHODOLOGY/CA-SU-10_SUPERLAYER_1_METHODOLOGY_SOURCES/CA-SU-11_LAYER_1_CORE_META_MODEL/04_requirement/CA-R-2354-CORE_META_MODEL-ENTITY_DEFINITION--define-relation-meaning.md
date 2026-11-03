---
atom_id: CA-R-2354
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Meaning
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Relation Meaning

## Claim

Relation Meaning is the canonical meaning of a reusable Relation Type.
Direction and transitivity describe the Type. An optional derived inverse is a
view of the direct tuple, not another authored edge. Actual source and target
endpoints remain tuple facts.


```CFEL
Relation.Meaning{:1}: [string]{:1};
Relation.Meaning.*[]{:0}
```

## Details

Source meaning: CA-R-2247. Scope-specific constraints remain in the governing
Relation Declarations.
