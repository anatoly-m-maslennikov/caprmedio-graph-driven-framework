---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Demand'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 25
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-923
  - CA-R-924
  - CA-R-1576
  - CA-R-1588
atom_id: CA-E-425@25
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 5
---
# Summary

Validate Relational Atom Classifications

## Scope

Relational Atom classifications.

## Claim

the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.

## Details
