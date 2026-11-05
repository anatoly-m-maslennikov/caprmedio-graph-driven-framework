---
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Carrier
version: 26
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-D-457
ref_id: CA-D-457
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-457-CORE_META_MODEL-DECISION--serialize-operations-atom-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Serialize Operations Atom Type tokens

## Claim

### Prose Claim


Operations Atom File Carriers and their Type filename tokens.


an Operations Atom File Carrier **must** serialize its Type using this filename-token mapping:

| Operations Atom Type | Filename token |
|---|---|
| Action | `ACTION` |
| Workflow | `WORKFLOW` |
| Step | `STEP` |
