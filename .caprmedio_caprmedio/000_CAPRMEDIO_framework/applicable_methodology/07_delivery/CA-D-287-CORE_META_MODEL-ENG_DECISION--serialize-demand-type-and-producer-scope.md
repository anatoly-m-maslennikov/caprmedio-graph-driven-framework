---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand).Target Scope Unit
version: 29
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-D-287
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-287-CORE_META_MODEL-ENG_DECISION--serialize-demand-type-and-producer-scope.md
  source_atom_id: CA-D-287
  source_atom_revision: 29
  source_sha256: 25d02056bf7bfecfd48890ee01d5452aa9fe998cd90f396d43ca4ef8c1dddb24
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Demand Type and Producer Scope

## Claim

### Prose Claim


Demand Atom filenames.


**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
