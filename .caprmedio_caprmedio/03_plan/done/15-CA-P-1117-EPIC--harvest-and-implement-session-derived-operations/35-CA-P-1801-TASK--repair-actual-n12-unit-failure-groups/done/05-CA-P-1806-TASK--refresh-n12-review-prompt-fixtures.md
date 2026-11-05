---
atom_id: CA-P-1806
ref_id: CA-P-1806
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
  - CA-C-511
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 5-CA-P-1806-TASK--refresh-n12-review-prompt-fixtures.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/35-CA-P-1801-TASK--repair-actual-n12-unit-failure-groups/done
work_sequence_number: 5
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Refresh N12 review prompt fixtures

## Objective

refresh the exact prompt settings pin and correct the sealed authority fixture, retaining all substantive authorization and no-forcing checks.

## Details

- this lane owns 2 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the capability-authority suite passes 6 tests and the RMED prompt contracts pass 17 tests. the exact current default-settings SHA is bound by the prompt manifest and D580 v5, without an unavailable legacy Project-file assertion. independent review preserves substantive Operator authorization and no-forcing checks.
