---
subjects:
  governs: "Owned Atoms"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Scope Unit", "Entity/Carrier"]
version: 10
updated_at: "2026-10-15 18:43:10 +0000"
relations: {}
atom_id: "CA-R-1447"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1447-CORE_META_MODEL-GENERAL--define-owned-atoms.md
  source_atom_id: CA-R-1447
  source_atom_revision: 10
  source_sha256: 4b0fde74b25faedc66359e70415174f8de1b2de0f58ed74a4363484d0eb8e246
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Owned Atoms

## Scope

the ownership of Atoms by Scope Units.

## Claim

Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.

## Details
