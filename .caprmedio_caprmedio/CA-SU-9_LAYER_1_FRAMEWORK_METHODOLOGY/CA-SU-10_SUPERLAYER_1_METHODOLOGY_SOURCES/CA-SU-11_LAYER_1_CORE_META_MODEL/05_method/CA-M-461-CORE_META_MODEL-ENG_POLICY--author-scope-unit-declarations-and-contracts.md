---
atom_id: CA-M-461
form: Eng Policy
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
version: 1
relations: {}
tier: 3
updated_at: 2026-11-02 19:17:40 +0400
role: Method
---
## Summary

Author Scope Unit Declarations and Contracts

## Claim

- Keep the Operator’s wording as close as possible. Correct grammar and organize it into coherent statements with the simplest syntax possible. Preserve clear terms and key concepts; do not replace them with polished synonyms.
- Write one external Scope Unit Declaration for each declared Scope Unit. Use Role Requirement and Form Scope Unit Declaration. Set its active Subject (`subjects.active`) to that specific Scope Unit; do not add another binding field or an additional per-unit Definition Atom.
- Keep one or more Goals separate from the Declaration and outside the declared Scope Unit; link them without duplicating their content.
- A Scope Constraint is external to the governed Scope Unit and may be part of its Declaration.
- Keep Scope Contract Atoms inside the governed Scope Unit at tier 0. Use applicable RMEDO roles; do not impose a minimum count, exactly one Contract, or every role. A Scope Unit may have no local Contract Atoms.

## Details

A Declaration states the Scope Unit ID where applicable, Name, ordered state, optional Label, conditional order.number and direct containment. Do not add Navigation Number to Scope Unit Declarations. Keep the Project Declaration outside the Project, like the Project Goal, with external Operator ownership.

Authority and Delivery Folder names are derived. Only non-root Authority Folder names include the Scope Unit ID prefix. The Project Authority Folder is `.caprmedio_<project name>`, without an ID. Do not author derived paths in individual Scope Unit Declarations.

Use the declared direct parent, not physical nesting, to establish logical parentage. Do not author Structural Level or Structural Coordinate. Keep Label independent of ordered state. Distinguish a declared Scope Unit, its materialized Carriers and its Goal coverage.
