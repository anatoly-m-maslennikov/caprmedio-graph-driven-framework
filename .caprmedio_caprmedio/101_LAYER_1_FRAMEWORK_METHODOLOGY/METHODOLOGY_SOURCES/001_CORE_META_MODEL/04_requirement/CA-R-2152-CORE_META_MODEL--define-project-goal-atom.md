---
atom_id: CA-R-2152
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
version: 4
updated_at: 2026-10-25 17:32:27 +0400
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations: {}
---
# Summary

Define Project Goal Atom

## Scope

Requirement Atoms whose desired result targets the Project.

## Claim

A Project Goal Atom **means** a Requirement Atom of Type Project Goal whose Substance states one desired result for the Project and whose current/local owner is its Operator Actor. This is the exception to ordinary Local Scope Unit ownership. A Goal targeting a non-Project Scope Unit uses Type Goal and ordinary Scope Unit ownership instead.

## Semantics

The target is the Project; the owner is the Operator. The Operator is not a Scope Unit. Storage at Project level alone does not make a Requirement a Project Goal. Tier admission is specified by CA-R-2132.

The Project Goal retains its Operator Actor owner. CA-D-637 uses its Target Project only as the derived ordering context; ordinary Goal ownership and Scope ordering are unchanged.
