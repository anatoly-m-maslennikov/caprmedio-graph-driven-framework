---
atom_id: CA-R-1983
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: Project.Settings
relations:
  child_of:
  - CA-R-1176
version: 15
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1983-PROJECT_CONFIGURATION-RULE--define-project-framework-settings-parameter-resolution.md
  source_atom_id: CA-R-1983
  source_atom_revision: 15
  source_sha256: 4e5ea75c1551dec37b5af9a3cbe2e3c07f40f4498237ce1fd9c27bbaa6575253
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Parameter Resolution

## Claim scope

resolution of an effective framework parameter.

## Claim

Resolve each effective framework parameter from explicit Framework Settings or Default Settings under the applicable precedence. The result is derived; do not store it as a new Project.Settings Property.

## Details

Evidence: CA-M-279 defines the existing resolution method; CA-R-1402@27 and CA-R-1441 define its two configurations. Candidate #6 decisions 2 and 13 retain the governed setting and distinguish defaults from explicit selections. This definition adds no receipt, history-admission gate, stored result or fallback rule. Detailed precedence and invalid-value handling remain in the governing Method. The concrete CAPRMEDIO mechanism belongs in Project Configuration.
