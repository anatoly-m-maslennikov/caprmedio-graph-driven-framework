---
subjects:
  governs: "Entity/Relation"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Relation", "Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/Atom.Subjects"]
version: 10
updated_at: "2026-10-19 15:55:54 +0400"
relations: {"delivery_for": ["CA-R-1580"]}
atom_id: "CA-D-471"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-471-CORE_META_MODEL--serialize-explicit-plan-blocking.md
  source_atom_id: CA-D-471
  source_atom_revision: 10
  source_sha256: cab1d31f4fc9a38b31077928a7fc6eacbd47b7a92ba0fdf6caed85bb61a58757
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize explicit Plan blocking

## Scope

explicit `A BLOCKS B` facts, including their storage on Plan `A` under `relations.blocks` for Plan `B`.

## Claim

**every** explicit `A BLOCKS B` fact **must** be stored once on Plan `A` under `relations.blocks`, as a unique canonical Atom ID for Plan `B`; an omitted list encodes **`=0`** outgoing blocking Relations.

- do **not** store a separate inverse list.
- do **not** encode Plan scheduling with `relations.depends_on` **or** `subjects.depends_on`.
- store decomposition separately under CA-D-481-CORE_META_MODEL-DELIVERY--store-plan-decomposition-on-the-decomposing-plan; do **not** derive blocking from decomposition **or** directory order.

## Details
