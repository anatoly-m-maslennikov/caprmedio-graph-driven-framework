---
subjects:
  governs: "Entity/Node/Continuant/Project.Structure"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Scope Unit.Parent", "Entity/Node/Continuant/Scope Unit.Children", "Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Navigational Order Number", "Entity/Carrier"]
version: 9
updated_at: "2026-10-19 11:40:27 +0000"
relations: {}
atom_id: "CA-R-1485@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Preserve consistent structural readability fields

## Scope

derived structural readability representations retained by a Project Structure.

## Claim

Project Structure **may** retain derived structural representations for readability **only** **when** their authoritative inputs **and** consistency constraints are explicit. retained Structural Level **must** **`=`** declared parent depth from Project level **`0`**; a retained authority path **must** satisfy applicable Carrier naming **and** placement rules, including admitted exceptions. inconsistent representations **must** produce a reported conflict **without** an automatic choice of a new Name, parent, order, **or** binding. readability does **not** establish another source of authority.

## Details
