---
atom_id: CA-P-1590@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 47
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Implementation Evaluation
  depends_on:
  - Subject/Engineering/Workflow
  - Subject/Engineering/Action
  - Subject/Engineering/Implementation
  - Subject/Engineering/Implementation Evaluation
  - Subject/Domain/Node/Continuant/History/Journal
version: 8
updated_at: 2026-10-25 02:38:20 +0400
relations:
  is_decomposition_of:
  - CA-P-1137
  blocks:
  - CA-P-1519
tier: 3
---
# Summary

Prove native selected Implementation route

## Objective

Within <=15 minutes, prove W09's full selected graph through the admitted executable mock and actual shared recorder.

## Details

- Own only a new test_selected_native_implementation_route.py. Use current GoldenProject, actual preview/freeze/dispatch, explicit ImplementationMockAgent selected-root binding and four declared O091 visits. Verify real test-first baseline failure, candidate creation and assertion pass plus exact Workflow/Step/Action sealed facts/current source bindings. Mark mock-not-live-llm and keep invalid source/permission denial separate. Do not edit production, fixture, source, Plans, Journal, code outside the test, or commits. Docker development-worker proof is not image/MCP/queue proof. No FPF, harvesting, paid call or live effects; apply patch, preserve others and inherit 90%.

## Saved result

Saved test_selected_native_implementation_route.py. Focused local and development-worker runs passed 3/3. Actual W09 preview/freeze/dispatch with the bounded mock traversed four O091 visits, baseline failure, candidate creation and passing assertions, with exact source bindings and shared Run facts. Permission and stale-source cases remain separate; this is not immutable-image or live-Agent proof.

## Definition of Done

Strict full native W09 mocked functional proof is saved, or an exact protected native/runtime/input remainder is retained.
