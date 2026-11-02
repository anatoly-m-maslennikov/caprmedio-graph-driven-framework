---
atom_id: CA-R-2229@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
version: 2
relations: {}
tier: 1
updated_at: 2026-10-29 14:12:43 +0400
---
## Summary

Define Requirement Type Term Definition

## Claim scope

The Term Definition value in the qualified Requirement Type domain and the lexical meaning owned by an Atom of that Type.

## Claim

Term Definition **means** the dedicated Requirement Type whose Claim states the authoritative meaning of **`=1`** reusable lexical Term. It is distinct from Entity Definition, which defines an Entity or property structure and constraints. The Term Definition Type has the shared Requirement Claim contract; this Type declaration does not create actual Term Definition Atoms.

## Details

The Operator confirmed exactly one dedicated authoritative Requirement Atom for a reusable Term's meaning, authoring procedure in M, and well-formedness and conflicts in E. This refines the existing Type reservation under CA-R-2229 rather than registering a second Type. The meaning-owner condition is carried by CA-R-1319. Authored Semantics, Details, repetition, inferred composition, and derived views do not become another lexical meaning owner.

Reusable `Package`, `Unit`, and `ID` retain approved meanings across complete names. The lexical Term `ID` is distinct from the qualified property entity `atom.id`; a Term Definition is not an entity-ID definition merely because its word is used in a property name.

CA-R-1279's exact canonical GOVERNS obligation remains applicable. The Term kind is declared by CA-R-1318; CA-R-1194 and CA-R-1931 permit a defining Atom to introduce its governed target, and CA-R-2002 supplies the named-instance path family. An explicit lexical definition may introduce `Entity/Object/Continuant/Term//ID`; its occurrence in an entity name or parser output cannot do so. This does not introduce synthetic domain entities or implement the deferred Terms Graph.

No dictionary Projection, extractor, lookup service, or mandatory derived-definition layer is required. Optional terminology consumers select the dedicated Term Definition authority when selecting Governed Terms; their selected-source traces remain separate from lexical authority.
