---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Target Scope Unit'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1588
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Default Plan target to the enclosing Scope Unit

## Claim scope

Plans with no separately selected Claim Target Scope Unit during authoring.

## Claim

during authoring, a Plan with no separately selected Claim Target Scope Unit **must** select its owning Scope Unit as the target, independently of Plan containment **or** Label; a Hub does **not** become that default target. carry the resolved target under CA-D-482.
