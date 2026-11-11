---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Directory
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Carrier/Directory
version: 29
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-264
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-264-CORE_META_MODEL-ENG_DECISION--derive-direct-containment-from-the-nearest-directory-carrier.md
  source_atom_id: CA-D-264
  source_atom_revision: 29
  source_sha256: f2f43c816e8ad2ecb659c8ba140d2c553369c562ac4b710e9137d06c6b4c2faa
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Direct Containment from the Nearest Directory Carrier

## Claim scope

Artifact Revisions whose canonical Carriers are nested below Directory Carriers.

## Claim

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive **`=1`** direct `IS_CONTAINED_BY` connection to the Structural Entity Revision carried by its nearest ancestor Directory Carrier **and** the reverse `CONTAINS` view from that connection.

## Details

For this Carrier-derived view, canonical nesting supplies the fact; the view does not create a second authored relation declaration. IS_CONTAINED_BY is the child-to-parent direction, and CONTAINS is its derived inverse. Reading or refreshing the inverse view does not edit the containing entity's carrier; when that entity is an Atom, it does not create a new Version for it. Physical nesting does not silently replace the logical parent declared by Project Structure under CA-R-1660. Existing Revision/Structural Entity wording is retained for the separate content migration.
