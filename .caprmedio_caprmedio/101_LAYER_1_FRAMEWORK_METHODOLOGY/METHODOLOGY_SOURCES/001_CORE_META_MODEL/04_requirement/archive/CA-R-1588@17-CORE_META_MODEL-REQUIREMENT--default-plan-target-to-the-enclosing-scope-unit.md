---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Target Scope Unit'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Label'
version: 17
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-R-1574
  - CA-D-482
atom_id: CA-R-1588@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of decomposition **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
