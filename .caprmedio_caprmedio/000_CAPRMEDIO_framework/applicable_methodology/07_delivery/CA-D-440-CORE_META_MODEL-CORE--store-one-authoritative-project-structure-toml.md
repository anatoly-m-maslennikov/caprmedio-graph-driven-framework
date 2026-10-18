---
subjects:
  governs: "Entity/Continuant/Node/Project.Structure"
  depends_on:
    ["Entity/Continuant/Node/Project.Settings", "Entity/Carrier", "Entity/Continuant/Node/Scope Unit"]
version: 7
updated_at: "2026-10-18 03:34:47 +0400"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-862"
atom_id: "CA-D-440"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-440-CORE_META_MODEL-CORE--store-one-authoritative-project-structure-toml.md
  source_atom_id: CA-D-440
  source_atom_revision: 7
  source_sha256: b2178dae0bfb6d28b45e5c6deaa26972c4b657e2ce5fe11a3780ca2095260a9a
  original_relations_sha256: 966790aed439082bc112a837c866f12d7b99b17679663bf5b164a38efeab0818
---
# Summary

Store one authoritative Project Structure TOML

## Scope

the authoritative Project Structure Carrier.

## Claim

the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.

## Details
