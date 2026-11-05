---
atom_id: CA-P-1805
ref_id: CA-P-1805
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
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1801
  relates_to:
  - CA-C-510
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 4-CA-P-1805-TASK--repair-n12-selected-run-fixtures.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/35-CA-P-1801-TASK--repair-actual-n12-unit-failure-groups/done
work_sequence_number: 4
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Repair N12 selected Run fixtures

## Objective

repair confirmed selected-run/MCP fixture or code mismatches while preserving existing authority, source freshness and recording contracts.

## Details

- this lane owns 4 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the selected-execution suite passes 20 tests and the isolated MCP suite passes 4 tests. the fixtures copy exact bound sources into disposable Projects, allow bounded gateway cold start and correctly stop before a next Step while terminal recording is pending. independent review accepts the changes; actual all-route release proof remains separate.
