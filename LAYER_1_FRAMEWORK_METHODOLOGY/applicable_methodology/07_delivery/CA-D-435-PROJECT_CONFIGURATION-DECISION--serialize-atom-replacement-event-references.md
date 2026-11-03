---
subjects:
  active: Carrier/File.Main Content
  passive:
  - Carrier
  - Journal
  - Event Record
  - Atom.ID
version: 25
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-D-435
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-435-PROJECT_CONFIGURATION-DECISION--serialize-atom-replacement-event-references.md
  source_atom_id: CA-D-435
  source_atom_revision: 25
  source_sha256: 3e611da260df568a00191b42106d6b26eabb569ecc9155866aa94899157f0268
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Atom replacement event references

## Claim scope

actual Atom replacement references supplied to the Main Content of a Journal Carrier.

## Claim

the Main Content of a Journal Carrier **must** preserve the actually supplied predecessor **and** successor Atom references of a replacement observation, including `predecessor_atom_id` **and** `successor_atom_ids` **when** supplied.

- preserve reference values **and** array order as data through safe encoding. array order does **not** establish priority **or** execution order.
- do **not** look up an earlier Journal Event Record, require a predecessor chain, compute a digest, validate the replacement **or** fabricate a baseline **to** append these observations.
- absence of replacement references does **not** establish whether the action was a replacement. do **not** infer missing identities, successors **or** historical facts.
- existing encoded Event Record representations remain readable **without** rewriting their fields, selected representation **or** observed values. legacy **or** nonconforming values remain observations, **not** certified replacements.
- actual source replacement, exact predecessor history **and** successor correctness remain independently governed by CA-R-807 **and** CA-E-462. Journal Carrier append **or** read grants no source-effect permission **and** proves none of those conditions.
