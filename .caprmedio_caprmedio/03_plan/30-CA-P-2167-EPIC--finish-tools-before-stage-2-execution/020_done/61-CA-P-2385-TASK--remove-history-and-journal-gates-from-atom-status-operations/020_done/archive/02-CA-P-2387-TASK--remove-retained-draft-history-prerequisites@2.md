---
atom_id: CA-P-2387
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, "Atom/Status", Journal, Workflow, Operator]
version: 2
updated_at: "2026-10-15 20:33:37 +0000"
relations:
  is_decomposition_of: [CA-P-2385]
---
# Summary

Remove retained Draft-history prerequisites

## Objective

The ordinary affected execution path accepts manual Draft promotion without a retained-history directory or records. Existing retained records are optional evidence, not permission; actual failures and partial effects remain truthful.

## Details

### Current checkpoint — 2026-10-16

A native concurrency review found that two simultaneous ID-free Draft promotions could both apply the same fresh ID to different carriers. Preserve ordinary identity/collision safety without reinstating a retained-history or Journal gate. The discovered bounded safety work is [CA-P-2400 — Exclude concurrent native identity publication](02-CA-P-2387-TASK--remove-retained-draft-history-prerequisites/01-CA-P-2400-TASK--exclude-concurrent-native-identity-publication.md), estimated at most 15 minutes. Its implementation and independent final verification remain pending acceptance; this Plan stays Active.

Remove trusted-head, never-identified/demotion lineage and consuming-successor prerequisites from the affected lifecycle and MCP/Workflow adapters. A valid manually authored Draft with no retained-history records must be promotable through the ordinary interface. Reuse existing identity/collision and source-write safety behavior; do not require retrospective registration, invent provenance or delete real history.

Estimated own work: at most 15 minutes; split further before execution if needed. After completion, review/update the next dependent task. A blocked leaf is postponed with a truthful Problem/Question Concern as appropriate; independent ready work continues.

## Definition of Done

The ordinary affected execution path accepts manual Draft promotion without a retained-history directory or records. Existing retained records are optional evidence, not permission; actual failures and partial effects remain truthful.
