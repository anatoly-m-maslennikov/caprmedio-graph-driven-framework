---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Engineering/Autonomous Confidence Threshold
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 14
updated_at: 2026-10-24 11:42:35 +0400
relations:
  relates_to:
  - CA-M-271
  - CA-R-1044
atom_id: CA-R-1587@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Require an effective confidence threshold for Plan execution

## Scope

autonomous Plan execution decisions.

## Claim

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.

## Details
