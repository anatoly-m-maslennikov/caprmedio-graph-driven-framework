---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 17
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-440
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Eng Decision
---
# Summary

Store one authoritative Project Structure TOML

## Scope

the authoritative Project Structure Carrier.

## Claim

the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.

## Details
