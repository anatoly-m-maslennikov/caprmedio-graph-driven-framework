---
subjects:
  active: Entity
  passive:
  - Entity/Property
  - CFEL <+ Relation//HAS_PROPERTY
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1259
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
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
