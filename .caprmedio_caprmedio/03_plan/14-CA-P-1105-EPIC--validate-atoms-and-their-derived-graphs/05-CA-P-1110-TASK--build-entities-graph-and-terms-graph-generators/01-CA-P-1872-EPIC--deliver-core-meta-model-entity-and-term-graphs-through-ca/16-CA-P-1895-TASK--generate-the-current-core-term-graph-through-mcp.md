---
atom_id: CA-P-1895
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on:
    - Entity
    - Term
    - Atom
    - Property
    - Scope Unit
    - Tool
    - MCP
    - Workflow
    - Action
    - Journal
    - Plan
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1896
---
# Summary

Generate the current Core term graph through MCP

## Objective

Generate the current Core term graph through MCP.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 10 minutes.

Inputs: CA-P-1893; same sealed source selection.

Required Plan prerequisites: [CA-P-1893](14-CA-P-1893-TASK--verify-selected-live-graph-runtime-readiness.md).

Output: Generate the current Core term graph through MCP with source-backed evidence retained in this Task's work record.

Acceptance check: Actual term output and required Workflow/Action/Journal receipts; honest outcome.

Exclusive edit/effect scope: The admitted term graph route and its separate configured JSON destination for the same sealed Core selection; required actual receipts only.

Use exactly the same sealed source snapshot as the entity graph. Retain actual term output, implementation identity and required Workflow/Action/Journal receipts. Do not confuse a file/queue/reload with completion.

Inherit the main Epic's boundaries and the Operator's explicit 90% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Generate the current Core term graph through MCP" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
