---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom.ID", "Entity/Carrier/Directory Carrier"]
version: 9
updated_at: "2026-10-19 15:55:57 +0400"
relations: {"relates_to": ["CA-R-1579", "CA-R-117", "CA-R-118", "CA-D-268", "CA-D-460", "CA-D-475"]}
atom_id: "CA-D-481"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-481-CORE_META_MODEL-DELIVERY--store-plan-decomposition-on-the-decomposing-plan.md
  source_atom_id: CA-D-481
  source_atom_revision: 9
  source_sha256: 5ffc83dc1fe9564a6c348866acb0a91b0c489fc29524d5b2c5eb09ad430d81f3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Store Plan decomposition on the decomposing Plan

## Scope

direct Plan-decomposition facts declared on Plan Atom frontmatter.

## Claim

the direct fact `A IS_DECOMPOSITION_OF B` **must** be declared **only** **in** Plan `A` frontmatter as `relations.is_decomposition_of`, a collection containing the canonical Atom ID of Plan `B`.

- the collection has **`<=1`** target; omission represents **`=0`** direct targets.
- derive `B DECOMPOSES_INTO A` from that declaration; do **not** store `relations.decomposes_into` **or** an independent inverse list on `B`.
- derive recursive decomposition from the direct edges; do **not** store their transitive closure.
- directory nesting **may** represent the declared Relation but **must not** create, delete, **or** retarget it. **if** a Plan is placed inside another Plan's Directory Carrier, the declared immediate decomposition target **must** match that Plan, skipping reserved Status directories.
- placement **in** `03_plan` **or** `03_plan/001_backlog` does **not** erase an explicit decomposition Relation. a matching file **and** folder carry **`=1`** Atom, **not** a self-edge.

## Details
