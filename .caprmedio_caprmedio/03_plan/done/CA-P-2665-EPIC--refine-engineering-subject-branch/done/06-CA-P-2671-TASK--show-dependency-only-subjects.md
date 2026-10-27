---
atom_id: CA-P-2671
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
version: 2
updated_at: 2026-10-27 06:19:16 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2665
tier: 4
---
# Summary

Show dependency-only Subjects

## Objective

Add a separate section to each Subject Graph view for Subjects used in subjects.depends_on but never explicitly in subjects.governs within that view's selected Current source set.

## Details

Compare exact canonical Subject values from the two fields. Do not infer Governs membership from ancestors, children or inherited properties. Show each dependency-only Subject once with its referring Atom IDs, in deterministic alphabetical order. Keep the existing primary, properties and instances sections. This section is a derived review aid, not a new Subject root or automatic authority for creating or retiring Atoms.

Update the relevant methodology layout definitions through Drafts first. Integrate the section into the local projection rebuild after the accepted corrections; production tool/runtime code remains outside this Epic. Do not create a separate large mapping report.

## Definition of Done

- Relevant definition Drafts express the accepted section without changing Subject/link meanings.
- The four rebuilt views contain the exact depends_on-minus-governs set for their own sources.
- Referring IDs and alphabetical order match the selected sources; existing sections and source trace remain intact.

## Completion

Completed in Candidate #9: reviewed Drafts were promoted with predecessor archives; the four Current-source Subject views were rebuilt and checked. See the parent Epic for the applied counts and retained exclusions.
