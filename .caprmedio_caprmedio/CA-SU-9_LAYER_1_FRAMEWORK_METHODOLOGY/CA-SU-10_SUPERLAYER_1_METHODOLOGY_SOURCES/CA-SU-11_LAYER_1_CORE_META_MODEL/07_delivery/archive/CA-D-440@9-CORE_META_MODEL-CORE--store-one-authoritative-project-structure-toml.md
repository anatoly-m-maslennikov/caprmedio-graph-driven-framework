---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 9
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-R-1483
  - CA-R-862
atom_id: CA-D-440@9
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Store one authoritative Project Structure TOML

## Scope

the authoritative Project Structure Carrier.

## Claim

the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.

## Details
