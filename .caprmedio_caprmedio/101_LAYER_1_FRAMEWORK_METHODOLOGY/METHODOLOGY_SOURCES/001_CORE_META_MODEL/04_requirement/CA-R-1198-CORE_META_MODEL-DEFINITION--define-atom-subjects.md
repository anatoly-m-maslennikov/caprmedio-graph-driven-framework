---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Subjects
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - 'Subject/Graph Relation/Type: GOVERNS'
  - 'Subject/Graph Relation/Type: DEPENDS_ON'
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1198
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define Atom Subjects

## Scope

the Atom Subjects Property.

## Claim

the Atom Subjects Property **means** the optional Atom Property that records zero **or** one direct GOVERNS Subject Relation **and** any number of direct DEPENDS_ON Subject Relations **to** canonical Subject Targets. it preserves target identities **without** storing copies of the targets **or** introducing a separately identified Subject object **or** a nested Entity **or** Reference Property for **every** link.

## Details
