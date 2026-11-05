---
atom_id: CA-A-1232
ref_id: CA-A-1232
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Subject
tier: 3
status: Done
version: 4
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Compare dependency-only Subjects within selected sources

## Question

Is zero Governs evaluated inside the selected sources or across the whole project?

## Operator decision

“Within the selected sources (recommended).”

## Rule

Within the selected Current RMEDO source set, compare exact canonical paths in subjects.depends_on against paths in subjects.governs. List each path present only in depends_on once. A Governs reference outside that source selection does not remove it from this view.

For example, an Engine selection may report a Subject whose defining Atom is in Core. This is selection-relative coverage information; it does not establish a missing definition across the project. Keep branch/namespace identity exact and retain referring Atom IDs as provenance.

## Applied check

R2225 records this selection-relative rule. The fixture keeps a dependency visible when its Governs source is outside the selected Scope Units. Actual Current Core plus Relation-branch rendering also passes; unrelated branches are excluded. Production Tools/runtime were not changed.
