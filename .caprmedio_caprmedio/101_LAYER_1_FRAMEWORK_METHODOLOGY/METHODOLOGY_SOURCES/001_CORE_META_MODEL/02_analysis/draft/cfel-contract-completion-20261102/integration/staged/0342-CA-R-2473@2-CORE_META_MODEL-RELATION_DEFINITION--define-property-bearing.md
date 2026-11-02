---
atom_id: CA-R-2473@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL <+ Relation//IS_PROPERTY_OF
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Relation Definition
---
## Summary

Define Property bearing and its inverse

## Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

```CFEL
((Node, Node/**, .**) >| Independence = Property) {:1}((IS_PROPERTY_OF)) (Node, Node/**, .**);
IS_PROPERTY_OF ((HAS_INVERSE)) HAS_PROPERTY
```
