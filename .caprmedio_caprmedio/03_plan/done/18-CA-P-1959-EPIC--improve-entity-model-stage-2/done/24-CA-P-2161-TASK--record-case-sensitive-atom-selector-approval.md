---
atom_id: CA-P-2161
ref_id: CA-P-2161
role: Plan
form: Plan
label: Task
work_sequence_number: 24
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
topics:
  main_subject: Subject
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 4
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2157
tier: 3
container:
  atom: CA-P-1959
carrier_destination:
  file:
    name: 24-CA-P-2161-TASK--record-case-sensitive-atom-selector-approval.md
    path: .caprmedio_caprmedio/03_plan/done/18-CA-P-1959-EPIC--improve-entity-model-stage-2/done
---
# Summary

Record case-sensitive Atom selector approval

## Objective

The actual selector approval and the distinction between Atom and atom are recorded.

## Details

Own work: at most fifteen minutes. Record the actual reply, explained notation and exact case constraint. Update the current Epic checkpoint; do not rewrite captured evidence or authoritative Core definitions.

## Completion

Recorded approval of selectors for qualified and named Atoms. Atom is the Entity type; atom(...) is selector notation. Case is significant and neither token is normalized into the other. Evidence: `_projection/core-entity-review/stage2/operator.selector-decision.2026-10-11.json`. Grammar alignment, implementation and migration remain separate work; this Task does not claim those effects.

### Definition of Done

Not Done if the actual reply or casing constraint is lost, approval is expanded to source effects, captured evidence changes, or a decision record is presented as grammar implementation or completed migration.
