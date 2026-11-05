---
atom_id: CA-P-1802
ref_id: CA-P-1802
container:
  atom: CA-P-1801
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Evaluation Implementation
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation Implementation
  - Subject/Graph Node/Engineering/Continuant/Carrier
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1801
  relates_to:
  - CA-C-507
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-1802-TASK--repair-n12-golden-receipt-fixtures.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/35-CA-P-1801-TASK--repair-actual-n12-unit-failure-groups/done
work_sequence_number: 1
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Repair N12 golden receipt fixtures

## Objective

repair the source-complete golden fixture and affected tests without weakening actual receipt, currentness or Full Gate checks.

## Details

- this lane owns 17 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the fixture now writes the exact context-derived unit-deadline.json snapshot consumed by the real reader. independent review accepts the two-line fixture change. four focused tests have retained exit-0 terminal results: two retained-fixture cases, the E2E fixed-command/bound-receipt case and the Full Gate exact-partition/unchanged-bytes case. the long combined run has no retained aggregate verdict and is not claimed passing; the fresh complete Unit and later release gates remain with the parent Plan.
