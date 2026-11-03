---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Carrier
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-457
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-457-CORE_META_MODEL-ENG_DECISION--serialize-operations-atom-type-tokens.md
  source_atom_id: CA-D-457
  source_atom_revision: 26
  source_sha256: 28d9f5c0cf4c85be34498e5cdc777fdf69ae5caae78dca9c0da315608b476d66
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Operations Atom Type tokens

## Claim scope

Operations Atom File Carriers and their Type filename tokens.

## Claim

an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Step | `STEP` |
