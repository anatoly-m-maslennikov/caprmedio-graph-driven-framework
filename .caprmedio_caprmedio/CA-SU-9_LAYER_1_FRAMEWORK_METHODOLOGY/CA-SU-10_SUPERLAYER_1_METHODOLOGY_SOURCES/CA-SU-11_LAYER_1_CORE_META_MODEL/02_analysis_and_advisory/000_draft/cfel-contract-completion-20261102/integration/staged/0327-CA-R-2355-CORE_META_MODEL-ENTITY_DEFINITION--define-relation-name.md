---
atom_id: CA-R-2355
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation.Name
version: 4
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Relation Name

## Claim

Relation Name is the canonical name of a reusable Relation Type. The named
Type can connect many endpoint pairs. An actual edge remains the
source/Type/target tuple and does not create a separate Relation ID.


```CFEL
Relation.Name{:1}: [string]{:1};
Relation.Name.*[]{:0}
```

## Details

Source meaning: CA-R-2247. Scope-specific constraints remain in the governing
Relation Declarations.
