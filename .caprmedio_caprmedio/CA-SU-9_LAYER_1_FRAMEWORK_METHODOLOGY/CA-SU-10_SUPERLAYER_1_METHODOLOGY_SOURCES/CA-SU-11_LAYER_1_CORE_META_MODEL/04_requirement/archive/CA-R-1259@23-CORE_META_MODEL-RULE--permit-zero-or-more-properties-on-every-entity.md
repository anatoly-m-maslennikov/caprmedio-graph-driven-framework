---
subjects:
  governs: Entity
  depends_on:
  - Entity/Property
  - Entity/Graph Syntax <+ Relation//HAS_PROPERTY
version: 23
updated_at: 2026-10-30 17:41:00 +0400
relations: {}
atom_id: CA-R-1259@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Permit Zero or More Properties on Every Entity

## Claim scope

Property occurrences borne by every Entity.

## Claim

**every** Entity **may** bear **`>=0`** Property occurrences.

### Formal claim

```text
Entity {0+}((HAS_PROPERTY)){1} Property
```
