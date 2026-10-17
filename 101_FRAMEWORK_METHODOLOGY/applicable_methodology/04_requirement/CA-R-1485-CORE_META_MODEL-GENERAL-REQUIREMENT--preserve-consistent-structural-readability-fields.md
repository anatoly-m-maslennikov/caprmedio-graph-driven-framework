---
subjects:
  governs: "Entity/Continuant/Object/Project.Structure"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children", "Entity/Continuant/Object/Scope Unit.Structural Level", "Entity/Continuant/Object/Scope Unit.Navigational Order Number", "Entity/Carrier"]
version: 7
updated_at: "2026-10-16 12:08:27 +0000"
relations: {}
atom_id: "CA-R-1485"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1485-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-consistent-structural-readability-fields.md
  source_atom_id: CA-R-1485
  source_atom_revision: 7
  source_sha256: 65474f9490ebbc31deb837bdb3605f61372a8e26ec5717d9b91667445e143dde
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Preserve consistent structural readability fields

## Scope

derived structural readability representations retained by a Project Structure.

## Claim

Project Structure **may** retain derived structural representations for readability **only** **when** their authoritative inputs **and** consistency constraints are explicit. retained Structural Level **must** **`=`** declared parent depth from Project level **`0`**; a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.

## Details
