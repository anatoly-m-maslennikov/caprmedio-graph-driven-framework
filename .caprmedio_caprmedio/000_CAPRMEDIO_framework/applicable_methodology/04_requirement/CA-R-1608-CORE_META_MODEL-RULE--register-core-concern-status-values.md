---
atom_id: CA-R-1608
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1608-CORE_META_MODEL-RULE--register-core-concern-status-values.md
  source_atom_id: CA-R-1608
  source_atom_revision: 21
  source_sha256: 636a857fcc3f05add74c75db36b0c29d70410a6731b5ab95345c5a54018f4548
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Concern Status Values

## Claim

### Prose Claim


the Core Concern Status model.


the Core Concern Status model **must** inherit the allowed values of Atom.Header.Status and add (Resolved, Canceled).
