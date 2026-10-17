---
atom_id: "CA-R-1983@draft"
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Parameter Resolution"
relations:
  child_of:
  - CA-R-1176
version: 2
updated_at: "2026-10-17 23:29:01 +0000"
---
# Summary

Define Project.Framework Settings.Parameter Resolution

## Scope

resolution of one framework parameter from explicit Framework Settings or Default Settings.

## Claim

Parameter Resolution **means** selecting the effective framework parameter value from explicit Framework Settings **or** Default Settings under the parameter's governing rules.

## Details

Evidence: CA-M-279 defines the existing resolution method; CA-R-1402 and CA-R-1441 define its two configurations. Candidate #6 decisions 2 and 13 retain the governed setting and distinguish defaults from explicit selections. This definition adds no receipt, history-admission gate, stored result or fallback rule. Detailed precedence and invalid-value handling remain in the governing Method. The concrete CAPRMEDIO mechanism belongs in Project Configuration.
