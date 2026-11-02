---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Governing Objects/Atom.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
version: 21
updated_at: 2026-10-29 10:13:51 +0400
relations:
  delivery_for:
  - CA-R-1580
atom_id: CA-D-471@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize explicit Plan blocking

## Claim scope

explicit `A BLOCKS B` facts, including their storage on Plan `A` under `relations.blocks` for Plan `B`.

## Claim

**every** explicit `A BLOCKS B` fact **must** be stored once on Plan `A` under `relations.blocks`, as a unique canonical Atom ID for Plan `B`; an omitted list encodes **`=0`** outgoing blocking Relations.

- do **not** store a separate inverse list.
- do **not** encode Plan scheduling with `relations.depends_on` **or** `subjects.depends_on`.
- store Plan containment separately on the child under `IS_CONTAINED_BY`, with `CONTAINS` derived; do **not** derive blocking from containment **or** directory order.
