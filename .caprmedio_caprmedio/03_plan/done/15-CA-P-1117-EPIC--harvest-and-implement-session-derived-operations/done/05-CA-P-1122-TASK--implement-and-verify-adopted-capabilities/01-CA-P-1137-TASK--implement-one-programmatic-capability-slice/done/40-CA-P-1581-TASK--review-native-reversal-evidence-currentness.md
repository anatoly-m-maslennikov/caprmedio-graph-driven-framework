---
atom_id: CA-P-1581
content_role: Plan
type: Plan
label: Task
work_sequence_number: 40
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Revert Changes/Admission and Result Evaluation
  depends_on:
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1137
tier: 3
---
# Summary

Review native reversal evidence currentness

## Objective

Within <=15 minutes, independently check P1574's saved native evidence implementation against accepted D536@2 and its actual disposable proof.

## Details

- Read only native_revert_provider.py, directly bound current sources and focused native/provider tests. Do not edit files, Plans, Journal, source authority or implementation.
- Review configured roots, safe bounded evidence pins and canonical Event serialization, selected/history/before/after/affected consistency, governing Atom identity/revision and exact approved ordered effect payloads.
- Check actual decision, executor and capability revocation before each effect. Interrupted partial effects preserve completed versus unattempted facts rather than infer rollback or completion.
- Coordinate final saved implementation with its author. Focused disposable tests are permitted; no live Project effects, paid Agent, commits, FPF, harvesting or broad audits. Inherit 90%.
- Actual independent result: ACCEPT for the bounded native provider slice. Docker native suite passed 13/13; actual current decision payload, executor and per-capability grants revalidate before start and each effect, with revoked remaining effects blocked truthfully. No file changes by reviewer. Shared recording, MCP/queue, fixture and immutable-image proof remain separate gates.

## Definition of Done

An exact saved-byte ACCEPT or concrete bounded REJECT gates native reversal completion without claiming an image run.
