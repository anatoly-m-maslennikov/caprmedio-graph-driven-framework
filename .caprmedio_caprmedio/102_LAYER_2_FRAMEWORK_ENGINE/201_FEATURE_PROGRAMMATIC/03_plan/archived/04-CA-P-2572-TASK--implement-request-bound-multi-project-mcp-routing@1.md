---
atom_id: CA-P-2572
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 1
updated_at: "2026-10-21T19:56:58Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2568]
  depends_on: [CA-P-2570]
  relates_to: [CA-P-2562, CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Implement request-bound multi-Project MCP routing

## Objective

Add shared MCP routing from an explicit caller Project root to its canonical execution owner. Validate mounted-root containment and exact Project identity; preserve each native request and response and never select a Project globally.

## Details

One Task per file; each leaf has at most 15 minutes own work and must be decomposed before extending it. Review and update dependent Tasks after observed predecessor outcomes. Use the selected Project virtual environment, configured Project Temporary State and only broken/related checks. Do not replay uncertain effects, replace production or run the full suite.

### Definition of Done

Concurrent/interleaved two-Project calls retain correct settings, prefix, source frontier, state, output and errors; missing/outside/unsafe roots refuse without fallback.
