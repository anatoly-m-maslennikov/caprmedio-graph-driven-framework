---
atom_id: CA-R-2353
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format.Uniqueness Selection
version: 4
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Format Uniqueness Selection

## Claim

Format Uniqueness Selection identifies the comparison population for a
Property uniqueness check. It is optional and does not itself impose
uniqueness. It does not define a notation.


```CFEL
Format.Uniqueness Selection{:0..1}: [string]{:1};
Format.Uniqueness Selection.*[]{:0}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in the governing
Format Definition.
