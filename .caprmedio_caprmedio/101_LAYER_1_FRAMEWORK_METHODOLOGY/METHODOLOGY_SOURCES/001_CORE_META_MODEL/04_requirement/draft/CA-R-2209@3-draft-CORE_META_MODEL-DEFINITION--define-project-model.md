---
atom_id: CA-R-2209@3-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model
version: 3
updated_at: 2026-10-28 02:55:02 +0400
relations: {}
tier: 1
---
# Summary

Define Project Model

## Scope

Project Model in the Subject model.

## Claim

Project Model **means** the vocabulary grouping that **CONTAINS** Subjects for what exists in a project: its Atoms, governing configurations, Scope Units, Actors, history, Projections, Selections, Implementation and actual execution contexts.

## Semantics

It covers Implementation as well as CAPRMEDO Atoms. It groups the vocabulary for project things; it is not another copy of those things, a folder, repository snapshot or Carrier. Subjects may name actual things or descriptions. A runtime occurrence and a record of it remain different things.

Project Model CONTAINS Actor is displayed as `Project Model > Actor`, not `Project Model / Actor`. This is containment in the Subject vocabulary, not broader-to-narrower classification. A contained Subject does not inherit properties from the containing grouping merely through that containment.
