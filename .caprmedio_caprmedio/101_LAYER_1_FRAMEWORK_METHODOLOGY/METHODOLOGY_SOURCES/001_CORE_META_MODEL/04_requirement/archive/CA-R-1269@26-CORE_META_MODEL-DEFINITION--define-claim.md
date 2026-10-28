---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery.Content.Claim'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Graph Rule'
version: 26
updated_at: 2026-10-26 06:07:29 +0400
relations: {}
atom_id: CA-R-1269@26
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

The logical Claims of Requirement, Method, Evaluation, and Delivery Atoms.

## Claim

A Claim **means** one independently replaceable statement owned by exactly
one RMED Atom. It governs Atom broadly, rather than Atom.Content, because
Claim representation varies. Every RMED Atom has one logical Claim, but Claim
has no universal representation carrier. A natural-language Claim uses
`atom.content.claim`. A fully formal Claim uses `atom.claim.*` or Governing
Configuration. Claim is not a generic Substance property required of every
Content Role.

## Semantics

A Requirement Claim specifies the required outcome; a Method Claim specifies
how it is achieved; an Evaluation Claim specifies a check and its expected
result; a Delivery Claim specifies delivery or representation. A formal Graph
Rule carries its fully formal Claim in its operative YAML `claim.*` mapping,
rather than in `atom.content.claim`. P uses Objective, O Operation, C
Concern, and A Question/Analysis under their own content contracts. The common
word Claim does not create a separate definition layer or require every Atom
to carry the same primary content label.

## Details
