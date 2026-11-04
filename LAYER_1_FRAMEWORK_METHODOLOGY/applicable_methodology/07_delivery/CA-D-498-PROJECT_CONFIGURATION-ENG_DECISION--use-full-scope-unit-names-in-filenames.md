---
atom_id: CA-D-498
version: 14
updated_at: 2026-11-03 23:25:51 +0400
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-498-PROJECT_CONFIGURATION-ENG_DECISION--use-full-scope-unit-names-in-filenames.md
  source_atom_id: CA-D-498
  source_atom_revision: 14
  source_sha256: 77fc18aa18458c190ea9e976130c33a016ee91eeb44b97852dd0bb81cb4cc13b
  original_relations_sha256: d990781b372f65b5de75cf683d3150a3fb54d4608a2f2f688cab00d4f2b9bb85
---
## Summary

Use full Scope Unit names in filenames

## Claim

### Prose Claim


Scope Unit references serialized **in** Atom filenames **in** the CAPRMEDIO Project.


**every** filename token representing a Scope Unit **must** use its complete Scope Unit Name, rendered **in** uppercase with underscores under `CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case`, **without** abbreviation **or** a separately maintained alias.

## Details

this selects the representation required by `CA-D-302-CORE_META_MODEL-DELIVERY--serialize-scope-unit-references-as-filename-tokens`. `CORE_META_MODEL` remains `CORE_META_MODEL`; `PROJECT_CONFIGURATION` remains `PROJECT_CONFIGURATION`. the Scope Unit Name is the source; the filename token is its representation.
