---
atom_id: CA-D-636
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier
  passive:
  - Entity
  - CFEL > Relation//CARRIES
  - Entity/Object/Continuant/History
relations:
  child_of:
  - CA-R-1174
version: 16
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-636-CORE_META_MODEL-ENG_DECISION--bind-carriers-to-their-represented-current-or-historical-entities.md
  source_atom_id: CA-D-636
  source_atom_revision: 16
  source_sha256: 36df6cb03554652c0ed955ae56f642bb2897f316bf91a4687b3c04bf3670bc29
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Bind Carriers to their represented current or historical Entities

## Claim scope

Carrier bindings of non-ephemeral Entities.

## Claim

a Carrier binding **must** identify the Entity actually represented by that Carrier. a current Entity's Carrier binds that current Entity; a preserved historical version's Carrier binds that archived Atom version or the historical record actually represented, not a separate Revision entity. citing a current Entity's Version **must not** reclassify the current Entity as an archived version.

## Details

Use the separately defined CARRIES meaning. Its IS_CARRIED_BY inverse exposes the same binding with the endpoints reversed; neither direction substitutes an archived version for the Current Entity actually represented. The applicable Carrier policy determines the representation. General representation rules may carry dependent properties inside one File Carrier; this policy does not require a separately registered binding for each field or section. It creates no additional Carrier, snapshot, Journal record or history gate.
