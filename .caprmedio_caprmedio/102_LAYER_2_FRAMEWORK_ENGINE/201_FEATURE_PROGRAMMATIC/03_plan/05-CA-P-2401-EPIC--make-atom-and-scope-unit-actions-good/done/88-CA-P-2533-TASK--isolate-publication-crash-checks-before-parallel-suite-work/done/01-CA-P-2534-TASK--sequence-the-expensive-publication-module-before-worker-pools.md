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
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2533]
version: 2
updated_at: "2026-10-21T11:43:21Z"
---
# Summary

Sequence the expensive publication module before worker pools

## Objective

Remove the full suite's own interference from its crash-publication check without weakening coverage.

## Details

Exclusive edit PROJECT_TOOLS/run_full_test_suite.py only. Inspect callers and preserve existing signature, environment, exact-once discovery/accounting,2+2remaining worker bounds, later-module execution after failure, launcher order and KeyboardInterrupt cancellation. Keep minimal coherent change at canonical shared Local/Public suite owner. Do not edit tests/Atoms/Git/README, run Docker/MCP/release, alter deadlines or production validation. At most15minutes own work. Run static/pinned Ruff baseline checks and cooperate with test owner; report exact measures and any conformance debt rather than waiving E539.

### Acceptance

Source frozen and independently APPROVED. Canonical module runs once and completes reporting before remaining2ordinary+2Docker worker submissions. Existing accounting, failed-module continuation, cancellation and30/1800/1980second deadlines unchanged. Root focused scheduler17/17 pass0.807s, adjacent image/process14/14 pass2.588s; pinned Ruff and diff check pass. No real release/runtime acceptance yet. Runner245physical lines versus219, C564 tracks conformance debt without a waiver.
