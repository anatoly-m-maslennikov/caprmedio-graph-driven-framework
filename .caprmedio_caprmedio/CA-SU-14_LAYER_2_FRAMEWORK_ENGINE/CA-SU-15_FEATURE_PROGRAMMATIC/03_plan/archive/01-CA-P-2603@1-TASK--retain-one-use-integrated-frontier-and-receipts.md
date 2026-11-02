---
atom_id: CA-P-2603@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 1
updated_at: '2026-10-22T16:08:22Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2596
  depends_on:
  - CA-P-2579
  - CA-P-2595
  relates_to:
  - CA-R-1527
  - CA-M-405
  - CA-M-422
  - CA-M-430
  - CA-O-016
---
# Summary

Retain one-use Integrated frontier and receipts

## Objective

Persist exact Project/Run/source/packet bindings and immutable consumed receipts under one Run lock.

## Details

At most 15 minutes of own work; split before expanding. One Task per file. Review/update the next dependent Task after actual acceptance. Reuse current PROGRAMMATIC M/E/D, locked uv and canonical source/state owners. Preserve unrelated edits, exact predecessors and business-only Journal semantics. No production MCP traffic, full-suite run, release/deployment, uncertain replay or commit.

Accepted: selected_integrated_frontier.py, selected_integrated_frontier_records.py and selected_integrated_frontier_state.py; 14 root-run focused checks, producer Ruff/format/strict typing and independent targeted PASS. Canonical Project-root admission, strict closed state shapes, payload/response digests, bounded no-follow reads and lock cleanup verified. Exact duplicates return retained receipts; conflicting submissions and copied cross-Project state are refused. No native MCP claim.

### Definition of Done

Retain exact bounded paths and focused functional/type/lint evidence; distinguish storage acceptance from graph/MCP execution and runtime admission.
