---
atom_id: CA-P-1804@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 5
updated_at: 2026-10-24 19:58:06 +0400
subjects:
  governs: Repair N12 sealed suite fixtures
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Engineering/Evaluation Implementation
  - Subject/Engineering/Carrier
relations:
  is_decomposition_of:
  - CA-P-1801
  relates_to:
  - CA-C-509
tier: 3
---
# Summary

Repair N12 sealed suite fixtures

## Objective

repair source-sealed graph-state and suite fixtures without adding Git metadata to runtime packages or weakening repository/currentness checks.

## Details

- this lane owns 2 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the sealed graph fixture passes 14 tests without synthetic Git metadata; the specific sealed-workspace mutation test passes in 58.093 seconds and asserts that no .git exists. independent review accepts both test-only changes. no whole-suite or actual release pass is inferred.
