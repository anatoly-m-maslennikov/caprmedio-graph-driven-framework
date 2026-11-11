---
atom_id: CA-P-2160
ref_id: CA-P-2160
container:
  atom: CA-P-1959
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
  dependencies:
  - Subject
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2158
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 23-CA-P-2160-TASK--record-approved-quarantine-decisions.md
    path: .caprmedio_caprmedio/03_plan/020_done/18-CA-P-1959-EPIC--improve-entity-model-stage-2/020_done
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Record approved quarantine decisions

## Objective

The actual Operator choices for legacy Atom IDs and timestamp serialization are recorded without inventing selector approval.

## Details

Own work: at most fifteen minutes. Record the actual reply and exact audited input pins; update the current Epic checkpoint. Keep captured reports and original Core unchanged.

## Completion

Recorded the Operator's choice to migrate the six legacy IDs to new canonical IDs and to use quoted timestamps with explicit UTC offsets. The selector question remains open because the Operator requested an explanation. Evidence: `_projection/core-entity-review/stage2/operator.quarantine-decisions.2026-10-11.json`. This Task records decisions only; no successor ID was allocated, timestamp policy adopted, original source changed, or source migration performed.

### Definition of Done

Not Done if the recorded choices differ from the actual reply, selector approval is inferred, current input pins are stale, historical evidence or source contents change, or a decision record is presented as an execution receipt.
