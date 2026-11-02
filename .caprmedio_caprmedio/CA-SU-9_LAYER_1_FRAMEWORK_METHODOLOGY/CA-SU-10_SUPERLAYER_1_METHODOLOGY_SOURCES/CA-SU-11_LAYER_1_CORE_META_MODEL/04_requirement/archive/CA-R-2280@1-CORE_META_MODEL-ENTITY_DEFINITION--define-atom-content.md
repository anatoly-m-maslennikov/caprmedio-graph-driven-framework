---
atom_id: CA-R-2280@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom Content

## Claim scope

The Atom.Content grouping and its direct child properties.

## Claim

Atom.Content **means** the grouping of an Atom's role-specific content child properties. It has zero direct values; each child property has its own independent count, and a child value does not count as a value of Atom.Content. For RMED, the child properties use the registered `atom.content.*` logical paths and their Markdown sections remain governed by Delivery authority.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Content{0}
```
