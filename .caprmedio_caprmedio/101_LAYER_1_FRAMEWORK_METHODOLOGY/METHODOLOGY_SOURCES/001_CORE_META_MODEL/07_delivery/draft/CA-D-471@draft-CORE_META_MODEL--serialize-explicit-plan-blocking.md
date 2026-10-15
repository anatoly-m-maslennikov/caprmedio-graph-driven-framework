---
subjects:
  governs: "Plan Blocking Relations"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Plan Blocking Relations", "Entity/Continuant/Object/Atom.ID", "Entity/Continuant/Object/Atom.Subjects", "Entity/Continuant/Object/Relation"]
version: 7
updated_at: "2026-10-15 18:32:19 +0000"
relations: {"delivery_for": ["CA-R-1580"]}
atom_id: "CA-D-471@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
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
