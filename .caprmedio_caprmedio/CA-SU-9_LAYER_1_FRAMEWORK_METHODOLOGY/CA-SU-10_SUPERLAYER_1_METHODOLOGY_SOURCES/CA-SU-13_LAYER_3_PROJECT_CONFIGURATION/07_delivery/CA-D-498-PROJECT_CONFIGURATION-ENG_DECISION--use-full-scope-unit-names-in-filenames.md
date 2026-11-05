---
atom_id: CA-D-498
ref_id: CA-D-498
version: 14
updated_at: 2026-11-03 23:25:51 +0400
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
relations:
  depends_on:
  - CA-D-284
  - CA-D-302
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-D-498-PROJECT_CONFIGURATION-DECISION--use-full-scope-unit-names-in-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
---
## Summary

Use full Scope Unit names in filenames

## Claim

### Prose Claim


Scope Unit references serialized **in** Atom filenames **in** the CAPRMEDIO Project.


**every** filename token representing a Scope Unit **must** use its complete Scope Unit Name, rendered **in** uppercase with underscores under `CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case`, **without** abbreviation **or** a separately maintained alias.

## Details

this selects the representation required by `CA-D-302-CORE_META_MODEL-DELIVERY--serialize-scope-unit-references-as-filename-tokens`. `CORE_META_MODEL` remains `CORE_META_MODEL`; `PROJECT_CONFIGURATION` remains `PROJECT_CONFIGURATION`. the Scope Unit Name is the source; the filename token is its representation.
