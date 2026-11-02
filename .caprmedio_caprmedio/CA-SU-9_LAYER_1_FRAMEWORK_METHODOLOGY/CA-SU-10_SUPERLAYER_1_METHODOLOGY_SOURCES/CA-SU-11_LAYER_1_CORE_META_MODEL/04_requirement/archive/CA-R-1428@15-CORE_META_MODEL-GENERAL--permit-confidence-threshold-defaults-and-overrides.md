---
subjects:
  governs: Confidence Threshold.Source
  depends_on:
  - Confidence Threshold
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Hub Atom
  - Property
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 15
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-R-1427
atom_id: CA-R-1428@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Summary

Permit confidence-threshold defaults and overrides

## Scope

the source of a Confidence Threshold value.

## Claim

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Hub chain follows `IS_DECOMPOSITION_OF`, **not** Label spelling.

## Details
