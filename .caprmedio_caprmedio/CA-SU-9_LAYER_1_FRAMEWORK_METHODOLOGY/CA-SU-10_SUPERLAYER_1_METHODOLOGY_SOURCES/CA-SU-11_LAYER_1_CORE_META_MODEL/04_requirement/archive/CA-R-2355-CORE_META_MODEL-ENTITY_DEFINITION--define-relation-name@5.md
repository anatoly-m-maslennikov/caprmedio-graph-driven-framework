---
atom_id: CA-R-2355
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Name
version: 5
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
---
## Summary

Define Relation Name

## Claim

### Formal Claim

```CFEL
# model
Relation.Name{:1}: [string]{:1};

Relation.Name.*[]{:0}
```

### Prose Claim


Relation Name is the canonical name of a reusable Relation Type. The named
Type can connect many endpoint pairs. An actual edge remains the
source/Type/target tuple and does not create a separate Relation ID.



