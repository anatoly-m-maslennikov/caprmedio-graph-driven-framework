---
atom_id: CA-P-2376
content_role: Plan
type: Plan
label: Task
work_sequence_number: 54
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

Expose direct Subject lookup through MCP

## Objective

Extend the existing ATOM_SEARCH provider with the accepted closed request/result and root-bound read-only adapter. Use normal registry discovery and applicable source pins. Do not create Session, Run, Journal, staging or authorization records.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Definition of Done

Provider/registry tests pass for the accepted schema, actual source hashes, empty and refusal outcomes; Session behavior is preserved. Installed activation remains separate.

