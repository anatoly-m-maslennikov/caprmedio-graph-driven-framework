---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Target Scope Unit'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
version: 24
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1588@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Default Plan target to the enclosing Scope Unit

## Claim scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of Plan containment **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.

## Details
