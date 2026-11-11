---
version: 36
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1559
  - CA-R-1591
  - CA-R-1552
  - CA-R-1080@29
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Atom
  - Atom/(.Role := Evaluation)
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Atom/(.Role := Requirement)
  - Atom/(.Role := Method)
  - Atom/(.Role := Delivery)
  - Project
atom_id: CA-E-440
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
---
## Summary

Evaluate governing Atom change approval

## Claim scope

Governing Atom changes.

## Claim

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.
