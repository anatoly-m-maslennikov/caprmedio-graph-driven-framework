---
atom_id: CA-E-565@2
content_role: Evaluation
type: QA Case
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Implementation prompt context and handoff
  depends_on:
  - Prompt
  - Agent
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
relations:
  relates_to:
  - CA-R-1845
---
# Summary

Verify implementation prompt context and handoff boundaries

## Scope

Integrated and Isolated prompt invocation and return behavior.

## Claim

the Implementation passes this Evaluation only when each actual Agentic dispatch uses its supplied Step context, and an Isolated dispatch has a complete under-fifteen-minute subtask handoff and fresh admission.

## Details

Missing context blocks. The returned result cannot auto-dispatch a successor, alter Workflow state, or claim that the caller accepted its handoff.
