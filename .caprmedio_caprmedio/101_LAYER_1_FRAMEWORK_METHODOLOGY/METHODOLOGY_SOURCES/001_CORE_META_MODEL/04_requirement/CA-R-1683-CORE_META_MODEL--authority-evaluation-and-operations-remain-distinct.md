---
subjects:
  active: Entity
  passive:
  - Entity/Object/Continuant/Selection
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/History
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Actor
  - Entity/Object/Continuant/History/Journal > Event Record
  - Atom/(.Role := Evaluation)
version: 45
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1683
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Authority, Evaluation, and Operations remain distinct

## Claim scope

RMED Spec authority, CAPO Change content, concrete Implementation, actual executions, Verification judgments.

## Claim

CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549@21, including specific reusable Operations definitions under CA-R-2463; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.
