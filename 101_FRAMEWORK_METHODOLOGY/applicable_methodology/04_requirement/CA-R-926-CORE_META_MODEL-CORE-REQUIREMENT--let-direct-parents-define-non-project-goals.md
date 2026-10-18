---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Project.Structure", "Entity/Continuant/Node/Atom.Substance", "Entity/Continuant/Node/Scope Unit.Parent", "Entity/Continuant/Node/Scope Unit.Children"]
version: 22
updated_at: "2026-10-18 03:34:13 +0400"
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
  source_atom_revision: 22
  source_sha256: f9998c6b84c9b296bba192b91f5d26bb0529eda8d7fdf3b5387c212a1d25e7bd
  original_relations_sha256: 17da053e5a14748b4ae49b3e9ae87498700f37739d1c90477b4e8557624449be
---
# Summary
Let Direct Parents Define Non-Project Goals

## Scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.

## Details
