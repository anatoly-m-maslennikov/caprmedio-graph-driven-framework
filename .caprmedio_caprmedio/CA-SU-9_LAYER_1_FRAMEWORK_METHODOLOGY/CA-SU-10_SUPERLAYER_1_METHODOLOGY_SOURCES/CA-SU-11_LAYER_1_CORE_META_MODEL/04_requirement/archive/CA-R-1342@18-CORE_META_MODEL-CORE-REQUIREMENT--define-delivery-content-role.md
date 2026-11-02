---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Entity/Node/Continuant/Atom.Substance
  - Subject/Engineering/Carrier
  - Entity
version: 18
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1342@18
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Delivery Content Role

## Scope

the Delivery Content Role.

## Claim

Delivery **means** the Content Role of an Atom Substance that specifies how an Entity is represented, serialized, stored or placed in a Carrier.

## Details

Delivery governs representation formats, contents, addresses, placement, Entity/Carrier bindings and constraints on changes to those representations. Requirement defines the Entities, their dependent properties and their classification, including Carrier kinds. A statement defining what a Carrier or property is remains a Requirement; a statement specifying how its representation is encoded or placed is Delivery. A property stored in YAML or a Markdown section does not require its own Carrier entity or separately registered binding.

