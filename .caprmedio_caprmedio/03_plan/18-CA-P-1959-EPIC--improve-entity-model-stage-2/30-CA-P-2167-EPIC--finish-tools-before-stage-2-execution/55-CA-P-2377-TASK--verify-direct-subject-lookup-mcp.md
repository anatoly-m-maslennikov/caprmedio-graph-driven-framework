---
atom_id: CA-P-2377
content_role: Plan
type: Plan
label: Task
work_sequence_number: 55
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
  depends_on: [CA-P-2376]
---
# Summary

Verify direct Subject lookup MCP

## Objective

Independently test the registered provider through a real MCP transport with actual source fixtures and no fabricated freshness. Check selected PRMEDO behavior, currentness and no writes. Record installed-runtime verification separately.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Definition of Done

Real tools/list and tools/call pass with truthful pins and no Session/Journal effects on success and refusal. Report unavailable installed activation rather than claiming it.

