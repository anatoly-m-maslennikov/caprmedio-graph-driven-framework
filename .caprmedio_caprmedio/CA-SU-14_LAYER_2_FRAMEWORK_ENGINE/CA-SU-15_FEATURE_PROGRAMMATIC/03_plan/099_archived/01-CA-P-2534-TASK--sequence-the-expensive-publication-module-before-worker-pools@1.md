---
atom_id: CA-P-2534
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2533]
version: 1
updated_at: "2026-10-21T11:36:18Z"
---
# Summary

Sequence the expensive publication module before worker pools

## Objective

Remove the full suite's own interference from its crash-publication check without weakening coverage.

## Details

Exclusive edit PROJECT_TOOLS/run_full_test_suite.py only. Inspect callers and preserve existing signature, environment, exact-once discovery/accounting,2+2remaining worker bounds, later-module execution after failure, launcher order and KeyboardInterrupt cancellation. Keep minimal coherent change at canonical shared Local/Public suite owner. Do not edit tests/Atoms/Git/README, run Docker/MCP/release, alter deadlines or production validation. At most15minutes own work. Run static/pinned Ruff baseline checks and cooperate with test owner; report exact measures and any conformance debt rather than waiving E539.
