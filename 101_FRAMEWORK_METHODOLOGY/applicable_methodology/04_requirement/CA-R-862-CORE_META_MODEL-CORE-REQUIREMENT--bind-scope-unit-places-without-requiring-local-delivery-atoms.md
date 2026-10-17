---
subjects:
  governs: "Entity/Continuant/Object/Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Project.Structure", "Implementation Folder", "Entity/Carrier", "Entity/Continuant/Object/Atom/Content Role: Delivery"]
version: 17
updated_at: "2026-10-15 18:46:41 +0000"
relations:
  child_of:
    - CA-R-1484
atom_id: "CA-R-862"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-862-CORE_META_MODEL-CORE-REQUIREMENT--bind-scope-unit-places-without-requiring-local-delivery-atoms.md
  source_atom_id: CA-R-862
  source_atom_revision: 17
  source_sha256: c08695fe4e361855731f9ccf795b96b1a4450f37250cbd421e726c8196fe033f
  original_relations_sha256: e97103b9de4ee47dfbc03a240fd5f7d67efe5c3a843e2d7604a54112d1133c11
---
# Summary

Bind Scope Unit Places **without** Requiring Local Delivery Atoms

## Scope

non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have its authority place **and** Implementation Folder bound by its authoritative Project Structure declaration. concrete bindings **must not** be independently maintained **in** Delivery Atoms; applicable Delivery authority governs the representation, placement, **and** general Carrier conventions rather than repeating a unit's selected paths.

## Details
