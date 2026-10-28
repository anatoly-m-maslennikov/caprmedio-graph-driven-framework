---
subjects:
  governs: Subject/Graph Node/Carrier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/History
version: 21
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-377@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Eng Decision
---
# Summary

Exclude Atom metadata from Framework Instance Settings

## Scope

Atom metadata in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.

## Details
