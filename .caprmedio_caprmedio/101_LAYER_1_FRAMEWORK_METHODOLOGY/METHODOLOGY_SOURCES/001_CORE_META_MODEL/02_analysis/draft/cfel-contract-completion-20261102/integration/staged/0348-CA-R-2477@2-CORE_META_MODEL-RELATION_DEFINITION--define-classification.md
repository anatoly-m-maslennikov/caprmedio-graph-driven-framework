---
atom_id: CA-R-2477@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL <+ Relation//HAS_CLASSIFICATION
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Relation Definition
---
## Summary

Define classification and its written reverse

## Claim

HAS_CLASSIFICATION relates a Node to an applicable classification axis. `Node >| Axis` and `Axis |< Node` are opposite written views of the same fact. An axis is distinct from its value case.

```CFEL
(Node, Node/**, .**) >| Axis
```
