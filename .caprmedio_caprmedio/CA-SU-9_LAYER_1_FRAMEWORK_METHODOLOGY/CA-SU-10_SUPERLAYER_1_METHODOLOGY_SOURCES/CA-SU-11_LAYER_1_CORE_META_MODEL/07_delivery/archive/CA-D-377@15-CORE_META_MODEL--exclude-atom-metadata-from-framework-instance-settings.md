---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Atom
  - Artifact/Revision
version: 15
updated_at: 2026-10-24 00:51:05 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-377@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Exclude Atom metadata from Framework Instance Settings

## Scope

Atom metadata in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.

## Details
