---
atom_id: CA-A-1232
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-28 00:02:56 +0400
relations: {}
tier: 3
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
