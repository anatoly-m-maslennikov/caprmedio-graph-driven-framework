---
atom_id: CA-P-2375
content_role: Plan
type: Plan
label: Task
work_sequence_number: 53
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 10:00:19 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  depends_on: [CA-P-2374]
---
# Summary

Complete bounded Subject lookup reader

## Objective

Reuse the existing Subject reader and matcher for exact, prefix, suffix and contains. Validate selected logical scope and source freshness without forcing unrelated C/A or missing-Type migration. Preserve the CLI and use existing bounded read utilities.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Definition of Done

Focused reader tests cover matching, real grammar pins, logical scope, selected-ID ambiguity, stale sources and unrelated malformed C/A. Independent review passes.

