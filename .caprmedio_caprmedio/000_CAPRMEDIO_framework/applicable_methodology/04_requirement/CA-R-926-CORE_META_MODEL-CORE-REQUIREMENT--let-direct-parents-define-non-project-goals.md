---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Scope Unit.Parent", "Entity/Node/Continuant/Scope Unit.Children"]
version: 23
updated_at: "2026-10-19 15:54:29 +0400"
relations:
  child_of:
    - CA-R-925
atom_id: "CA-R-926"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-926-CORE_META_MODEL-CORE-REQUIREMENT--let-direct-parents-define-non-project-goals.md
  source_atom_id: CA-R-926
  source_atom_revision: 23
  source_sha256: 8c00c39ecd925f1c86820119478bde4551d647feb7966ee64aee67cf7eae2ab4
  original_relations_sha256: 17da053e5a14748b4ae49b3e9ae87498700f37739d1c90477b4e8557624449be
---
# Summary
Let Direct Parents Define Non-Project Goals

## Scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.

## Details
