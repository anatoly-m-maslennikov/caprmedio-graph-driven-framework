---
subjects:
  governs: Subject/Graph Relation
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
version: 16
updated_at: 2026-10-25 17:32:27 +0400
relations:
  delivery_for:
  - CA-R-1580
atom_id: CA-D-471@16
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize explicit Plan blocking

## Scope

explicit `A BLOCKS B` facts, including their storage on Plan `A` under `relations.blocks` for Plan `B`.

## Claim

**every** explicit `A BLOCKS B` fact **must** be stored once on Plan `A` under `relations.blocks`, as a unique canonical Atom ID for Plan `B`; an omitted list encodes **`=0`** outgoing blocking Relations.

- do **not** store a separate inverse list.
- do **not** encode Plan scheduling with `relations.depends_on` **or** `subjects.depends_on`.
- store decomposition separately under CA-D-481-CORE_META_MODEL-ENG_DECISION--store-plan-decomposition-on-the-decomposing-plan; do **not** derive blocking from decomposition **or** directory order.

## Details
