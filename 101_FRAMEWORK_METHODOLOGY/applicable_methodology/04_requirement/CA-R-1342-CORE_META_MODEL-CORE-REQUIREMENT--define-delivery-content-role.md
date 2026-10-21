---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Delivery"
  depends_on:
  - "Entity/Node/Continuant/Atom/Content Role"
  - "Entity/Node/Continuant/Atom.Substance"
  - Entity/Carrier
  - Entity
version: 16
updated_at: "2026-10-19 15:52:51 +0400"
relations: {}
atom_id: "CA-R-1342"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1342-CORE_META_MODEL-CORE-REQUIREMENT--define-delivery-content-role.md
  source_atom_id: CA-R-1342
  source_atom_revision: 16
  source_sha256: f27fab1d4e21f543db2328c1ee9fb900b01aceed5671e751ea96d416e5563879
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Delivery Content Role

## Scope

the Delivery Content Role.

## Claim

Delivery **means** the Content Role of an Atom Substance that specifies how an Entity is represented, serialized, stored or placed in a Carrier.

## Details

Delivery governs representation formats, contents, addresses, placement, Entity/Carrier bindings and constraints on changes to those representations. Requirement defines the Entities, their dependent properties and their classification, including Carrier kinds. A statement defining what a Carrier or property is remains a Requirement; a statement specifying how its representation is encoded or placed is Delivery. A property stored in YAML or a Markdown section does not require its own Carrier entity or separately registered binding.

