---
atom_id: CA-P-1114
ref_id: CA-P-1114
role: Plan
form: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 99
status: Active
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Implementation
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1106
  blocks:
  - CA-P-1115
tier: 3
container:
  atom: CA-P-1106
carrier_destination:
  file:
    name: 3-CA-P-1114-TASK--implement-source-bound-atom-checks.md
    path: .caprmedio_caprmedio/03_plan/14-CA-P-1105-EPIC--validate-atoms-and-their-derived-graphs/1-CA-P-1106-TASK--build-the-atom-carrier-validator
---
# Summary

Implement source-bound Atom checks

## Claim

the assigned AI Agent **must** implement current source-bound Property, section, Subject, Relation and projected-source checks with an independent coverage inventory.

## Definition of Done

the Plan is **not** Done **if** source-dependent checks lack exact authority bindings, unsupported obligations silently vanish, bad fixtures pass, good fixtures fail, or projected fidelity is inferred rather than checked.

## Details

- authority and validation adapters only; estimated 12 minutes, split further if necessary.
- use the source-bound input packet **in** `.caprmedio_tmp/implementation/validate-atoms-20260924`; current source Atoms remain authority. record evidence **without** editing unrelated work, weakening expected results, **or** promoting learned Methods inside this implementation Run.
