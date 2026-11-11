---
atom_id: CA-D-435
ref_id: CA-D-435
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
tier: 3
status: Active
version: 26
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-435-PROJECT_CONFIGURATION-DECISION--serialize-atom-replacement-event-references.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Serialize Atom replacement event references

## Claim

### Prose Claim


actual Atom replacement references supplied to the Main Content of a Journal Carrier.


the Main Content of a Journal Carrier **must** preserve the actually supplied predecessor **and** successor Atom references of a replacement observation, including `predecessor_atom_id` **and** `successor_atom_ids` **when** supplied.

- preserve reference values **and** array order as data through safe encoding. array order does **not** establish priority **or** execution order.
- do **not** look up an earlier Journal Event Record, require a predecessor chain, compute a digest, validate the replacement **or** fabricate a baseline **to** append these observations.
- absence of replacement references does **not** establish whether the action was a replacement. do **not** infer missing identities, successors **or** historical facts.
- existing encoded Event Record representations remain readable **without** rewriting their fields, selected representation **or** observed values. legacy **or** nonconforming values remain observations, **not** certified replacements.
- actual source replacement, exact predecessor history **and** successor correctness remain independently governed by CA-R-807 **and** CA-E-462. Journal Carrier append **or** read grants no source-effect permission **and** proves none of those conditions.
