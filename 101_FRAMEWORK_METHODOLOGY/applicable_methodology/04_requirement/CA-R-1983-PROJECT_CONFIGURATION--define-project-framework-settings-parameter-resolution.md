---
atom_id: CA-R-1983
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Parameter Resolution"
relations:
  child_of:
  - CA-R-1176
version: 2
updated_at: "2026-10-18 03:35:00 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1983-PROJECT_CONFIGURATION--define-project-framework-settings-parameter-resolution.md
  source_atom_id: CA-R-1983
  source_atom_revision: 2
  source_sha256: 23fd9d7f7a5e38538328b2ad756bb735690351954c80b2484f32abfe19899177
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Parameter Resolution

## Scope

resolution of one framework parameter from explicit Framework Settings or Default Settings.

## Claim

Parameter Resolution **means** selecting the effective framework parameter value from explicit Framework Settings **or** Default Settings under the parameter's governing rules.

## Details

Evidence: CA-M-279 defines the existing resolution method; CA-R-1402 and CA-R-1441 define its two configurations. Candidate #6 decisions 2 and 13 retain the governed setting and distinguish defaults from explicit selections. This definition adds no receipt, history-admission gate, stored result or fallback rule. Detailed precedence and invalid-value handling remain in the governing Method. The concrete CAPRMEDIO mechanism belongs in Project Configuration.
