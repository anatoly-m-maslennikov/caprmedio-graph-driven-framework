---
atom_id: CA-P-1790
ref_id: CA-P-1790
container:
  atom: CA-P-1782
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Implementation
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation Implementation
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1782
  relates_to:
  - CA-C-498
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 8-CA-P-1790-TASK--repair-the-compiler-and-cutover-fixture-expectations.md
    path: .caprmedio_caprmedio/03_plan/020_done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/31-CA-P-1782-TASK--repair-the-sealed-n9-unit-failure-groups/020_done
work_sequence_number: 8
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Repair the compiler and cutover fixture expectations

## Objective

repair compiler dry-run input, governed delivery path and interrupted cutover expectations without relaxing the accepted release or source-currentness boundaries.

## Details

- this bounded lane feeds a fresh source-bound N10; retain failed N9 without replay.
- root owns Git, integration, source pins, canonical refresh and actual dispatch. workers preserve other lanes' changes.
- local fixture/source acceptance is not full Release acceptance; installed N remains unchanged.

## Definition of Done

20bf097ff; two compiler and two cutover cases pass; full step-input module awaits the Prompt closure lane.
