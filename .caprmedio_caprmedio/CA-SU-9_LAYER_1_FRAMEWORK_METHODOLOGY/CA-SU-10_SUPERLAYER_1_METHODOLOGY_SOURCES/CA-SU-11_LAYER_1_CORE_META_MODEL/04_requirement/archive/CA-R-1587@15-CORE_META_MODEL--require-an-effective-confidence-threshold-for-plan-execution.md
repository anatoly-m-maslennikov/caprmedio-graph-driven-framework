---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Engineering/Autonomous Confidence Threshold
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-M-271
  - CA-R-1044
atom_id: CA-R-1587@15
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
