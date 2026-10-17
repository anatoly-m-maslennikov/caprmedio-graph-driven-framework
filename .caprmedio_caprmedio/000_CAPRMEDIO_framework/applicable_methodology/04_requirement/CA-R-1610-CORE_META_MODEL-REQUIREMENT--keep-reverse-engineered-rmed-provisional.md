---
atom_id: CA-R-1610
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Entity/Continuant/Object/Atom.Status"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Implementation", "Entity/Continuant/Projection", "Single Source of Truth", "Spec Content Roles"]
version: 6
updated_at: "2026-10-15 18:45:02 +0000"
relations:
  relates_to:
    - CA-R-1470
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1610-CORE_META_MODEL-REQUIREMENT--keep-reverse-engineered-rmed-provisional.md
  source_atom_id: CA-R-1610
  source_atom_revision: 6
  source_sha256: 39c7420f4a3b70c124f848c16991bbd9c3880883e08e2453fc103f3bfd506d1c
  original_relations_sha256: 98b573c3081158134b84ff5bb7f4dc41ac192decc52b2d93acab69de0b27cc5c
---
# Summary

Keep reverse-engineered RMED provisional

## Scope

RMED Claims reconstructed from existing Implementation or its Projections.

## Claim

RMED Claims reconstructed from existing Implementation **or** its Projections **must** remain proposed Draft Claims **until** accepted through the applicable Atom acceptance authority.

- extraction **or** inference alone does **not** establish Active authority.
- the accepted RMED, **not** the legacy Implementation **or** its Projection, governs subsequent refactoring **and** Evaluation of the result.

## Details
