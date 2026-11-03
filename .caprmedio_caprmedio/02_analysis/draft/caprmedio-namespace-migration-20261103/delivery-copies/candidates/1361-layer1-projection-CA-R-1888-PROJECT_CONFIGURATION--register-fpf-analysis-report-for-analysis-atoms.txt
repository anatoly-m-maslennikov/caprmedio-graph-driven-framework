---
atom_id: CA-R-1888
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory").Form
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")
version: 16
updated_at: 2026-11-02 19:33:47 +0400
relations: {}
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1888-PROJECT_CONFIGURATION--register-fpf-analysis-report-for-analysis-atoms.md
  source_atom_id: CA-R-1888
  source_atom_revision: 16
  source_sha256: 213c220b1729430e17c05231cfcf03bfa33bd5b5c3a8f79851f53b9209ba68de
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register FPF Analysis Report for Analysis Atoms

## Claim scope

the CAPRMEDIO Project Configuration contribution to `Atom/(.Role := "Analysis & Advisory").Form`.

## Claim

the CAPRMEDIO Project Configuration **must** register FPF Analysis Report as an additional value of `Atom/(.Role := "Analysis & Advisory").Form` under CA-R-1286. this registration does **not** change the Core contribution under CA-R-1232@28 **or** create another Form Property.

## Details

CA-R-1889 defines the registered Form. CA-D-581 defines its filename token. The Form remains within Role Analysis & Advisory.

