---
atom_id: CA-P-1531
ref_id: CA-P-1531
container:
  atom: CA-P-1520
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Journal Event Query
  dependencies:
  - Subject/Graph Node/Engineering/Operations
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1520
  blocks:
  - CA-P-1533
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 11-CA-P-1531-TASK--repair-journal-query-source-contract.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/8-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/done
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Repair Journal query source contract

## Objective

Within <=15 minutes, repair only the rejected Journal source packet before fresh independent review.

## Details

Read CA-P-1523, the saved CA-P-1524 rejection, active Project Principles, O161–163, R1861–1872, M334–337, E575–580, D555–558 and the current shared R1850 contract. Own these Journal source carriers, required predecessor archives, and Concerns CA-C-435–437. Address raw duplicate JSON keys, snapshot-wide Event-ID uniqueness, changed/deleted/truncated captured-prefix rejection on cursor continuation with later appends allowed, and enforceable configurable budgets. Use the single shared filter grammar, typed structural values and escaped field selectors authored by CA-P-1530; do not edit R1850 or create a second parser authority. No code, registration, competing logs or live Journal/Projection writes.

### Definition of Done

The current Journal packet has saved exact pins, all confirmed Journal-specific defects have corrected contracts and QA cases, and verification and Concern dispositions are retained. Fresh independent CA-P-1533 acceptance is still required.

## Result

Repaired and archived the owned v1 predecessors. The current Journal contract is
O161–163@2; R1861, R1862, R1865, R1866, R1868, R1869@2; M334, M336, M337@2;
E575, E577, E578, E580@2; and D556@2. It specifies raw duplicate-key rejection
before parse, frontier-wide Event-ID uniqueness, pre-dispatch byte-prefix capture,
continuation revalidation with append-after-prefix allowed, configured exhaustion
evidence, and Journal RFC6901 selectors. It reuses current shared R1850@2;
fresh independent P-1533 acceptance remains required and no implementation is
claimed.
