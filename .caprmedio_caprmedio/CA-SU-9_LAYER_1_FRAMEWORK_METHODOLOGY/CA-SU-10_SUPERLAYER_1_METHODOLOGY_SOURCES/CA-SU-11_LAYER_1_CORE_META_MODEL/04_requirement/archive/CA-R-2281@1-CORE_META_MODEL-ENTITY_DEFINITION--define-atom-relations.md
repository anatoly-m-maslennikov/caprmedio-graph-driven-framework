---
atom_id: CA-R-2281@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Relations
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Relations

## Claim scope

The Atom.Relations grouping and its direct child properties.

## Claim

Atom.Relations **means** the grouping of an Atom's declared relation child properties. It has zero direct values; each child property has its own independent count, and a child value does not count as a value of Atom.Relations. Rules governing a particular relation occurrence constrain that child occurrence and do not define this grouping.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Relations{0}
```
