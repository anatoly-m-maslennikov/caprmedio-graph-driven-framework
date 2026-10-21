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
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-21T00:33:42Z"
---
# Summary

Render the same-port MCP health page

## Objective

Serve an escaped browser health/history view from the existing MCP HTTP listener.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2508; coordinate the snapshot interface with P2509. Preserve default/JSON /health ready boolean and existing status semantics for machines; explicit HTML Accept renders health checks, recent Tool calls, Workflow status and safe errors. Reuse loopback Host/Origin protection. Show unavailable or unobserved capability/worker/Workflow status as unknown, never healthy by inference. Acceptance: browser and machine compatibility, escaping, bounded output, no effects or secret leakage.

### Dependency review before implementation

P2508 contract review is complete; R2007/E640/D639 are Active. Own health_page.py, http_server.py and MCP README only. Build from existing generation/task/tools and gateway.health_observations.snapshot(); do not reach DBOS/Docker/providers/Journals. Preserve old machine JSON and 200/503 behavior. Explicit browser HTML must show safe recent calls, Workflow scheduler versus actual outcome, coverage and errors; unknown remains unknown. No automatic runtime adoption or release before verification.

### Verified checkpoint and dependent review

Implemented explicit browser HTML on the existing /health listener, preserving default JSON readiness and loopback Host/Origin protection. Read-only escaped page exposes bounded recent calls, Workflow actual/scheduler state and safe errors; it labels generation-only readiness and unprobed provider/worker state. Independent HTTP/security review APPROVE and final18 health plus7 existing HTTP checks pass with stable hashes. P2511 was reviewed against these frozen inputs before acceptance; no deployment is claimed.
