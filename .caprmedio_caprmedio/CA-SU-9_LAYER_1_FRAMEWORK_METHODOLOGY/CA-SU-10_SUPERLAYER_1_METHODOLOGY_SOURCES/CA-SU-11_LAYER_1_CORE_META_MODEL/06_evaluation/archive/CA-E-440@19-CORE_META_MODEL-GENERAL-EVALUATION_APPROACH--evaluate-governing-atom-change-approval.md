---
version: 19
updated_at: 2026-10-23 03:06:32 +0400
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-R-1559","CA-R-1591","CA-R-1552","CA-R-1080"]}
subjects:
  governs: 'Entity/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - Entity/Node/Continuant/Atom.Author
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - 'Entity/Node/Continuant/Actor/Type: AI Agent'
  - AI Agent Confidence
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Spec
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Node/Continuant/Project
atom_id: CA-E-440@19
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
type: "Policy"
global_tier: 10
---
# Summary

Evaluate governing Atom change approval

## Scope

Governing Atom changes.

## Claim

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.

## Details
