---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Label
  depends_on:
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Term//Property
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom.Type
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Label'
version: 10
updated_at: 2026-10-24 00:51:05 +0400
relations: {}
atom_id: CA-R-1594@10
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define Label

## Scope

Labels of Atoms.

## Claim

a Label **means** an Operator-controlled, mutable word **or** phrase used as a Property of an Atom **to** aid navigation **and** understanding, **without** determining that Atom's identity, Type, Subtype, structure, authority, **or** behavior. The effective Label is the explicitly carried Label value when present; otherwise it is the Atom's Type name. The fallback is derived, is not a second stored Property, and does not change Atom identity or Type.

## Details
