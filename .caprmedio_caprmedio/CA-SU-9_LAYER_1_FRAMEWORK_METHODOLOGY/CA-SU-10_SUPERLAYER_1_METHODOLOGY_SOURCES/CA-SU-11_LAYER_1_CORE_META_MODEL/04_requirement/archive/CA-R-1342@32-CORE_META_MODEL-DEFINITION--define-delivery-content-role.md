---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Carrier
  - Entity
version: 32
updated_at: 2026-10-29 17:09:48 +0400
relations: {}
atom_id: CA-R-1342@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Delivery Content Role

## Claim scope

the Delivery Content Role.

## Claim

A Delivery Atom is an Atom with Content Role Delivery. Its Claim specifies how an Entity is represented, serialized, stored or placed in a Carrier. Common Atom meaning, properties and constraints are inherited.

## Details

Delivery governs representation formats, contents, addresses, placement, Entity/Carrier bindings and constraints on changes to those representations. Requirement defines the Entities, their dependent properties and their classification, including Carrier kinds. A statement defining what a Carrier or property is remains a Requirement; a statement specifying how its representation is encoded or placed is Delivery. A property stored in YAML or a Markdown section does not require its own Carrier entity or separately registered binding.
