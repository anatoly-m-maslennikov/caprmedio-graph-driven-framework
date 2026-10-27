---
atom_id: CA-P-1987
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1980
tier: 3
---
# Summary

Repair Subject Tool Operations

## Objective

Specify repeatable valid-file lookup and Subject-only preview steps while retaining the existing live-effect guards.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1982, CA-P-1983.

Exclusive files: CA-O-046 and CA-O-030. Consume CA-P-1979 and normalized metadata. Add direct field lookup and exact occurrence attribution; pinned explicit replacement, complete-file validation, unrelated-byte preservation and no-write preview. Do not turn Operations into migration orchestration. Subject-only actual changes are semantic revisions with Version N+1; illustrative preview time is not an execution receipt. Keep sealed generic update, required approval, source recheck, history/Journal and standalone apply boundaries. No MCP invocation, new adapter or raw internal live writer. Preserve Summary and increment each Version once. Output: two coherent Operations Atoms and pins.

Use the shared minimum contract in the CA-P-1979 review. A worker owns only the listed files; root owns integration, commits and Task completion. Recheck source pins after normalization. No unrelated changes, Core entity-model edits, source migration, runtime activation or release work. Ask for a concrete unresolved decision below 90% confidence. Decompose before exceeding 15 minutes.

### Local execution receipt

Completed the assigned disjoint Tool contract edits. Exact before/after pins and Version/identity/section checks are in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/task-1987.receipt.json`. Root rechecked the original Summaries, declared TOOLS ownership, each Version +1 and canonical role sections; the author checked the stated valid-file cases and retained meaningful generic constraints. No code, Core or runtime effect occurred. This completes this authoring leaf only; CA-P-1981 independently accepts the combined packet before implementation.

### Definition of Done

The Plan is **not** Done if its stated output or exact before/after evidence is missing; a file outside its exclusive scope changes; preserved claims or identity are lost; the cross-role contract conflicts; checks fail; a prerequisite is incomplete; or own work exceeds 15 minutes without decomposition.
