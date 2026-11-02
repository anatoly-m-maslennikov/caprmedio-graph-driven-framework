---
atom_id: CA-M-draft
content_role: Method
form: Eng Policy
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
version: 1
relations: {}
tier: 3
updated_at: 2026-10-31 18:43:05 +0400
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

A Declaration may state the Scope Unit ID, Name, whether it is ordered or unordered, Label, Local Order, and connections. Do not add Navigation Number to Scope Unit Declarations. Local Order remains; Navigation Number is retained only for Steps and P Atoms. Do not invent additional per-field cardinality, format, default, owner or count rules. Keep the Project Declaration outside the Project, like the Project Goal. Follow the same external Operator ownership; do not assume a project-root carrier path.
