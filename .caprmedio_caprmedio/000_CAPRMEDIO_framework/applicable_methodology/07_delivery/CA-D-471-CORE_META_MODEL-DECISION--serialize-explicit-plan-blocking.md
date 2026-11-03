---
subjects:
  active: CFEL <+ Relation
  passive:
  - Atom/(.Role := Plan)
  - CFEL <+ Relation
  - Atom.ID
  - Atom.Subjects
version: 24
updated_at: 2026-11-02 08:06:47 +0400
relations:
  delivery_for:
  - CA-R-1580
atom_id: CA-D-471
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-471-CORE_META_MODEL-DECISION--serialize-explicit-plan-blocking.md
  source_atom_id: CA-D-471
  source_atom_revision: 24
  source_sha256: 8282cf7ed8c0fde283e71e258e8fae23659b6530fcf2f76a36673e9df9b8c28a
  original_relations_sha256: b9827eecea8416db112a5056a7c7def708d6483cae4e2b7f7bfaec9981959427
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
