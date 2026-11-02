---
subjects:
  governs: Entity/Carrier
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/History
version: 25
updated_at: 2026-10-29 10:13:50 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-377@25
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Decision
---
## Summary

Exclude Atom metadata from Framework Instance Settings

## Claim scope

Atom metadata in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
