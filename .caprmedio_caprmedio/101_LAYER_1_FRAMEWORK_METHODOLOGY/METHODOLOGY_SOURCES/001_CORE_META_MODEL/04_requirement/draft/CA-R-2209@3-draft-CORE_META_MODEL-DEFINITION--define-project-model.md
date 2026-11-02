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
updated_at: 2026-10-28 16:27:23 +0400
relations: {}
tier: 1
---
# Summary

Define Project Model

## Scope

Project Model in the Subject model.

## Claim

Project Model **means** the vocabulary grouping that **groups** Subjects for what exists in a project: its Atoms, governing configurations, Scope Units, Actors, history, Projections, Selections, Implementation and actual execution contexts.

## Semantics

It covers Implementation as well as CAPRMEDO Atoms. It groups the vocabulary for project things; it is not another copy of those things, a folder, repository snapshot or Carrier. Subjects may name actual things or descriptions. A runtime occurrence and a record of it remain different things.

Project Model membership is displayed as `Project Model::Actor`. This is organizational membership, not structural containment (`>`) or broader-to-narrower classification (`/`). Membership supplies no property inheritance and does not create another canonical Subject target. `Actor/AI Agent` and `Actor/Operator` remain actual specializations with applicable Actor-property inheritance.

### Existing-target reference marker

Organizational membership may refer to an existing kind with `::@`; it does not declare another copy of that kind. The `@` modifier and its identity constraints are defined by the common Subject grammar. This does not itself settle whether an independent structural option has been declared.
