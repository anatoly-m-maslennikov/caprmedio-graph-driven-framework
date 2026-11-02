---
atom_id: CA-P-2574@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 4
updated_at: 2026-10-24 10:35:14 +0400
subjects:
  governs: Subject/Engineering/MCP.selected Workflow capability routes
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2576
  depends_on:
  - CA-P-2569
  - CA-P-2571
  - CA-P-2572
  - CA-P-2573
  relates_to:
  - CA-P-2562
  - CA-M-396
  - CA-M-397
  - CA-M-398
  - CA-M-399
  - CA-M-400
tier: 3
---
# Summary

Verify one MCP two-Project functional routing

## Objective

Exercise the selected shared MCP boundary with two isolated valid Projects and interleaved calls. Keep fixture support consistent and errors deliberately isolated; prove no cross-Project fallback or effects and no production port use.

## Details

One Task per file; each leaf has at most 15 minutes own work and must be decomposed before extending it. Review and update dependent Tasks after observed predecessor outcomes. Use the selected Project virtual environment, configured Project Temporary State and only broken/related checks. Do not replay uncertain effects, replace production or run the full suite.

### Definition of Done

Retain exact focused commands/results, same-endpoint evidence and declared image/source limits; no full-suite rerun or stronger isolation claim than demonstrated.
