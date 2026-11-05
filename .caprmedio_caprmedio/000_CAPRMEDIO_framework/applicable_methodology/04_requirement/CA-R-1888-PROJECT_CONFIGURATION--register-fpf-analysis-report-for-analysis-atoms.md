---
atom_id: CA-R-1888
ref_id: CA-R-1888
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory").Header.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
tier: 2
status: Active
version: 16
updated_at: 2026-11-02 19:33:47 +0400
carrier_destination:
  file:
    name: CA-R-1888-PROJECT_CONFIGURATION-RULE--register-fpf-analysis-report-for-analysis-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1888-PROJECT_CONFIGURATION--register-fpf-analysis-report-for-analysis-atoms.md
  source_atom_id: CA-R-1888
  source_atom_revision: 16
  source_sha256: ca7eae1429e04b39bc933ec5fb0d96dd5050b1a4a4522804117cef9ae289e95a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register FPF Analysis Report for Analysis Atoms

## Claim

### Prose Claim


the CAPRMEDIO Project Configuration contribution to `Atom/(.Header.Role := "Analysis & Advisory").Header.Form`.


the CAPRMEDIO Project Configuration **must** register FPF Analysis Report as an additional value of `Atom/(.Header.Role := "Analysis & Advisory").Header.Form` under CA-R-1286. this registration does **not** change the Core contribution under CA-R-1232@28 **or** create another Form Property.

## Details

CA-R-1889 defines the registered Form. CA-D-581 defines its filename token. The Form remains within Role Analysis & Advisory.

