---
atom_id: CA-P-2511
content_role: Plan
type: Plan
label: Task
work_sequence_number: 71
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-21 04:06:25 +0400"
---
# Summary

Verify MCP health and history in isolated fixtures

## Objective

Independently accept the health/history behavior without using the production MCP endpoint for tests.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2509/P2510; test preparation may proceed after P2508. Own synthetic fixtures and functional/negative checks only. Cover real Gateway/HTTP routing, JSON/HTML readiness and 503, hostile Host/Origin refusal, recent successful/rejected/failed/uncertain observations, Workflow scheduler SUCCESS versus actual interrupted_pending, bounded retention, redaction/escaping and no redispatch. Use distinct fixture roots/state/locks and nonproduction listener if network is needed; no mutable live-Atom corpus. Acceptance: fresh bound focused tests and independent review; update release Task before execution.
