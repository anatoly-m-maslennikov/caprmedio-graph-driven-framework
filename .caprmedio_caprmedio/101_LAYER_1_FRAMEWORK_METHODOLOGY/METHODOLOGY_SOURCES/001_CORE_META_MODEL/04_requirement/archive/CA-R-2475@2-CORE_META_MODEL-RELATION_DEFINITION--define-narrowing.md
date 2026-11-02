---
atom_id: CA-R-2475@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL <+ Relation//NARROWER_THAN
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Relation Definition
---
## Summary

Define NARROWER_THAN

## Claim

The narrower Node inherits applicable Relation and Property constraints without cloning declarations or instance facts.

```CFEL
((Node, Node/**, .**) >| Independence = Primary Node) ((NARROWER_THAN)) ((Node, Node/**, .**) >| Independence = Primary Node);
NARROWER_THAN ((HAS_INVERSE)) HAS_NARROWER
```
