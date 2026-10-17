---
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Project.Framework Settings.Parameter Resolution"
version: 2
updated_at: "2026-10-16 13:03:26 +0000"
---
# Summary

Define Project.Framework Settings.Parameter Resolution

## Scope

resolution of one framework parameter from explicit Framework Settings or Default Settings.

## Claim

Parameter Resolution **means** selecting the effective framework parameter value from explicit Framework Settings **or** Default Settings under the parameter's governing rules.

## Details

Evidence: CA-M-279 defines the existing resolution method; CA-R-1402 and CA-R-1441 define its two configurations. Candidate #6 decisions 2 and 13 retain the governed setting and distinguish defaults from explicit selections. This definition adds no receipt, history-admission gate, stored result or fallback rule. Detailed precedence and invalid-value handling remain in the governing Method. The concrete CAPRMEDIO mechanism belongs in Project Configuration.

This is an unassigned Draft in a non-authoritative review package. PROJECT_CONFIGURATION is its intended owner; the historical CORE_META_MODEL filename is retained for lineage. No file relocation, source Atom creation or admission is performed. This proposed Claim is not active R coverage and does not close the source-definition gap.
