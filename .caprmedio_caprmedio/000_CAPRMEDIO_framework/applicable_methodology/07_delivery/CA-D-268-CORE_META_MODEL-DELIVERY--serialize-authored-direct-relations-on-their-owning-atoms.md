---
subjects:
  governs: "Entity/Continuant/Object/Relation"
  depends_on:
    ["Entity/Continuant/Object/Relation.Source Reference"]
version: 15
updated_at: "2026-10-16 12:09:11 +0000"
relations: {}
atom_id: "CA-D-268"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-268-CORE_META_MODEL-DELIVERY--serialize-authored-direct-relations-on-their-owning-atoms.md
  source_atom_id: CA-D-268
  source_atom_revision: 15
  source_sha256: 519ae6c3a9f268c1a935525350769db8b7079d9d4afe5e8d4f40027da1ca8bd8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Authored Direct Relations on Their Owning Atoms

## Scope

Authored direct semantic relations.

## Claim

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references; target position **must not** add, remove, **or** alter a direct relation **or** dependency. source-file target order is nonsemantic; validation **must not** require canonical sorting **or** order normalization. each Relation Kind's direction, endpoint validity **and** other declared semantics remain applicable.

## Details
