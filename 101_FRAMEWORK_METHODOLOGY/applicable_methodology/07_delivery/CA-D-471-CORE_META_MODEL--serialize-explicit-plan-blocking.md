---
subjects:
  governs: "Entity/Continuant/Object/Relation"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Relation", "Entity/Continuant/Object/Atom.ID", "Entity/Continuant/Object/Atom.Subjects"]
version: 8
updated_at: "2026-10-16 12:09:34 +0000"
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
  source_atom_revision: 8
  source_sha256: e6cc522f95242b5e3ee602309b874c9a6fd2392c97f399a840b998f7f9a13fd8
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
