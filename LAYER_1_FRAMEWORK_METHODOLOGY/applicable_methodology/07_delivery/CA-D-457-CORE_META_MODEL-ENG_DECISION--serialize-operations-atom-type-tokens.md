---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Carrier
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
  source_sha256: 36288e9ea2929bfed587077cc3949930fb35232ad74d24cf415ada9d4ff0d043
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
