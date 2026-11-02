---
atom_id: CA-E-565
content_role: Evaluation
type: Eval Case
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations: {}
tier: 3
---
# Summary

Verify implementation prompt context and handoff boundaries

## Scope

Integrated and Isolated prompt invocation and return behavior.

## Claim

the Implementation passes this Evaluation only when each actual Agentic dispatch uses its supplied Step context, and an Isolated dispatch has a complete under-fifteen-minute subtask handoff and fresh admission.

## Details

Missing context blocks. The returned result cannot auto-dispatch a successor, alter Workflow state, or claim that the caller accepted its handoff.
