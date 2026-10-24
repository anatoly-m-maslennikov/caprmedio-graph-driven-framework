---
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Step Run
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Subject/Domain/Node/Occurrent/Execution/Step Run.Execution Context
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
version: 9
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1519
  - CA-R-1520
  - CA-R-1525
  - CA-R-1527
atom_id: CA-R-1791
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep Invocation delivery distinct from Step completion

## Scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.

## Details
