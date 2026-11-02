---
atom_id: CA-P-2510
content_role: Plan
type: Plan
label: Task
work_sequence_number: 70
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

Render the same-port MCP health page

## Objective

Serve an escaped browser health/history view from the existing MCP HTTP listener.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2508; coordinate the snapshot interface with P2509. Preserve default/JSON /health ready boolean and existing status semantics for machines; explicit HTML Accept renders health checks, recent Tool calls, Workflow status and safe errors. Reuse loopback Host/Origin protection. Show unavailable or unobserved capability/worker/Workflow status as unknown, never healthy by inference. Acceptance: browser and machine compatibility, escaping, bounded output, no effects or secret leakage.
