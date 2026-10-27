---
atom_id: CA-C-596@1
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-24 07:51:34 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Graph/Relation
relations: {}
---
# Summary

Should typed prerequisites also be Subject topics?

## Question

Should an exact prerequisite Plan ID stay in Subjects when the same direct
DEPENDS_ON relation and the task's prerequisite text already preserve it?

## Scope

Eight Current Plans: P940, P945, P946, P947, P948, P949, P950 and P951.

## Details

Bounded choice: remove only these eight redundant ID-valued Subject entries.
Each source explicitly waits until that same Plan is Done and already stores
its exact ID in the typed depends_on relation. Keep that relation, its direction,
target and all body text unchanged. R2004 defines Subjects as topic expressions;
repeating the prerequisite identity there adds no distinct topic meaning.

This is not a general deletion of named instances or dependencies. No missing
relation is inferred, no prerequisite is removed, and no historical Plan is
executed or newly declared complete. Other unresolved Subjects remain visible.
