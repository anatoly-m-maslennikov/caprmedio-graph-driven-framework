---
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
version: 22
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-377
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
