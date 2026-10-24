---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Demand'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 20
updated_at: 2026-10-23 03:06:32 +0400
relations:
  evaluation_for:
  - CA-R-923
  - CA-R-924
  - CA-R-1576
  - CA-R-1588
atom_id: CA-E-425@20
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: QA Case
global_tier: 11
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
