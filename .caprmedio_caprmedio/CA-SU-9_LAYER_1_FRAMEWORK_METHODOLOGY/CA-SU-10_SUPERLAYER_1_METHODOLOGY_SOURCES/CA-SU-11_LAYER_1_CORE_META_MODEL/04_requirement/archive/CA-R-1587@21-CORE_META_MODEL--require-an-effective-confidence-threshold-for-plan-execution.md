---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 21
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1587@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Require an effective confidence threshold for Plan execution

## Claim scope

autonomous Plan execution decisions.

## Claim

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.
