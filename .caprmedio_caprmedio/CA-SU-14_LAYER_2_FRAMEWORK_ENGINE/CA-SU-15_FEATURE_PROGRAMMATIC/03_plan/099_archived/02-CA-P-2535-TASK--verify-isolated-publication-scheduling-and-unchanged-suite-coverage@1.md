---
atom_id: CA-P-2535
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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

Verify isolated publication scheduling and unchanged suite coverage

## Objective

Remove the full suite's own interference from its crash-publication check without weakening coverage.

## Details

Exclusive edit PROJECT_TOOLS/tests/test_full_test_suite_parallel.py only. Use actual scheduler/pools with disposable module fixtures and controlled external execution. Prove exact-once isolated critical-module execution with no other worker active; remaining pools still2ordinary+2Docker; all output/count/skip accounting and serial launcher preserved; critical failure still permits later modules and fails summary; cancellation cancels queued work. Preserve30/1800second deadlines. Do not edit source owner, sharedfixture or other files, Atoms/Git/Docker/MCP/release. At most15minutes own work, respect current compact M/E/D and source-size ratchet; run focused source-scheduler tests after owner freeze.
