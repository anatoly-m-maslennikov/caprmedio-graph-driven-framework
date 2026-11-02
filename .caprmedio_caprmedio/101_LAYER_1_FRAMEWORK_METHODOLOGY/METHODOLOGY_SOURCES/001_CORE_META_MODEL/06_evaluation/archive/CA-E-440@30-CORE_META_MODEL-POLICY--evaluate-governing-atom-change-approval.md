---
version: 30
updated_at: 2026-10-29 07:17:23 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1559
  - CA-R-1591
  - CA-R-1552
  - CA-R-1080
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Author
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Entity/Object/Continuant/Governing Objects/Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
atom_id: CA-E-440@30
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 4
---
# Summary

Evaluate governing Atom change approval

## Scope

Governing Atom changes.

## Claim

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.

## Details
