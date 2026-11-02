---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Content
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery.Content.Claim'
version: 23
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1269@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Claim

## Scope

Claim fields in the role-specific Content of R/M/E/D Atoms.

## Claim

A Claim **means** one independently replaceable statement owned by exactly
one Atom. It is the Content.Claim of the applicable RMED Role/Type, not a
generic Substance property required of every Content Role.

## Semantics

A Requirement Claim specifies the required outcome; a Method Claim specifies
how it is achieved; an Evaluation Claim specifies a check and its expected
result; a Delivery Claim specifies delivery or representation. P uses
Objective, O Operation, C Concern, and A Question/Analysis under their own
content contracts. A formal Graph Rule has operative YAML rather than a
Claim field. The common word Claim does not create a separate definition
layer or require every Atom to carry the same primary content label.

## Details
