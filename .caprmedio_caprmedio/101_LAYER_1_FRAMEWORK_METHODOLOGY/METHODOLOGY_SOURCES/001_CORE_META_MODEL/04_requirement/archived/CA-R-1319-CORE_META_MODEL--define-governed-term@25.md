---
subjects:
  governs: Entity/Object/Continuant/Term
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
  - Entity/Object/Continuant/Term
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 25
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1319
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Governed Term

## Claim scope

Reusable lexical Terms whose Project-specific meanings are owned by active dedicated Term Definition Requirement Atoms.

## Claim

a Governed Term **means** a reusable Term whose approved Project-specific meaning is owned by **`=1`** active Requirement Atom of Type Term Definition.

## Details

The Operator confirmed exactly one dedicated authoritative Requirement Atom for a reusable Term's meaning and the distinct Requirement Type Term Definition. Entity Definition Atoms, authored Semantics or Details, consistent use, and derived views do not become a second lexical meaning owner. Duplicate active Term Definitions are an authority conflict even when their wording agrees.

This changes the lexical meaning-owner Type only. Reusable `Package`, `Unit`, and `ID` do not become unique complete entity names merely by being Terms. `atom.id` and `projection.id` remain distinct complete qualified property names; `ID` keeps its approved meaning across them. No dictionary Projection, extractor, lookup, entity renaming, or parser inference is required.

CA-R-1279's canonical GOVERNS obligation remains applicable. A defining Claim may explicitly introduce its lexical Term target using Current authority under CA-R-1194 and CA-R-1931; lexical composition alone does not create one. Optional terminology consumers must follow this dedicated meaning-owner selection without becoming prerequisites of Term meaning or implementing the deferred Terms Graph.
