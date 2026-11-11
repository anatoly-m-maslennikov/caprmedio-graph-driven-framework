---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Filename.Scope Unit Token
  passive:
  - CAPRMEDIO <+ MODEL <+ Scope Unit.Name
  - CAPRMEDIO <+ STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-302
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-302-CORE_META_MODEL-ENG_DECISION--serialize-scope-unit-references-as-filename-tokens.md
  source_atom_id: CA-D-302
  source_atom_revision: 28
  source_sha256: ed282a5ff49aaf8f36018fb937c8bb91111cb468d3b0248af541ed924999ec67
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Serialize Scope Unit References as Filename Tokens

## Claim scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.
