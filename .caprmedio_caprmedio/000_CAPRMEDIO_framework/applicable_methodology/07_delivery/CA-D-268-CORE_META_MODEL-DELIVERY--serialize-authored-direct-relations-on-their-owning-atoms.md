---
subjects:
  governs: "Entity/Relation"
  depends_on:
    ["Entity/Relation.Source Reference"]
version: 18
updated_at: "2026-10-20 00:10:33 +0400"
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
  source_atom_revision: 18
  source_sha256: eb33ffdb1ae992b8db8ea50dbb332ab3fd91b90040096c5be4965d89afc96888
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Authored Direct Relations on Their Owning Atoms

## Scope

Authored direct semantic relations.

## Claim

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references; target position **must not** add, remove, **or** alter a direct relation **or** dependency. source-file target order is nonsemantic; validation **must not** require canonical sorting **or** order normalization. each Relation Kind's direction, endpoint validity **and** other declared semantics remain applicable.

## Details

Serialize only the Relation Kind's declared direct direction, never a second declaration for its derived inverse. For containment, the child carries IS_CONTAINED_BY with the parent reference; CONTAINS is a derived parent view and is not serialized on the parent. A change confined to the child does not request a parent-carrier write or a new parent Version. The relation's spelling does not determine which direction is direct.

This policy governs authored relation declarations. When canonical Carrier nesting already supplies a containment fact under CA-D-264, do not add a second independent declaration for the same fact; CA-D-266 governs that derived view. This source contract does not itself register a new runtime relation key.
