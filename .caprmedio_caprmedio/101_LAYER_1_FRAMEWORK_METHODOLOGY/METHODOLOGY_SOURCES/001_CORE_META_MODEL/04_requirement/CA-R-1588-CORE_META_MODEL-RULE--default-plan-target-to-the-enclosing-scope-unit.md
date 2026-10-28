---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Target Scope Unit'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Label'
version: 22
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1588
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Default Plan target to the enclosing Scope Unit

## Scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of Plan containment **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
