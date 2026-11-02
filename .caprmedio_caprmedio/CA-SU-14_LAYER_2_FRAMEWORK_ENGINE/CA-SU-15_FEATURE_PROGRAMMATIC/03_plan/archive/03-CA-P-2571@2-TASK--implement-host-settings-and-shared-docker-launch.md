---
atom_id: CA-P-2571@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: '2026-10-21T20:06:28Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2576
  depends_on:
  - CA-P-2570
  relates_to:
  - CA-P-2562
  - CA-M-396
  - CA-M-397
  - CA-M-398
  - CA-M-399
  - CA-M-400
---
# Summary

Implement host settings and shared Docker launch

## Objective

Implement the shared host settings reader and Docker launch material with a configurable My_Repos mount outside any Project. Keep machine-local settings out of repository authority and preserve existing settings rather than overwriting them.

## Details

One Task per file; each leaf has at most 15 minutes own work and must be decomposed before extending it. Review and update dependent Tasks after observed predecessor outcomes. Use the selected Project virtual environment, configured Project Temporary State and only broken/related checks. Do not replay uncertain effects, replace production or run the full suite.

### Definition of Done

Focused temporary-config and Compose/launch checks prove explicit validated roots, correct bind mount and endpoint parameters without touching production.
