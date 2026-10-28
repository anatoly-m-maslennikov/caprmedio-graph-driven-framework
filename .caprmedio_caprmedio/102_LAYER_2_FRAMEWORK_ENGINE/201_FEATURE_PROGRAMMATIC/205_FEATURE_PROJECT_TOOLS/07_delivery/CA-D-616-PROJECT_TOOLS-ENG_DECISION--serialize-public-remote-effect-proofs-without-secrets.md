---
atom_id: CA-D-616
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 14
updated_at: 2026-10-27 19:59:27 +0400
relations:
  delivery_for:
  - CA-R-1921
  - CA-R-1925
type: Eng Decision
tier: 4
---
# Summary

Serialize public remote effect proofs without secrets

## Scope

the remote proof of one public push.

## Claim

public remote effect evidence **must** retain the personal remote identity, branch direction, immutable commit identity, and repository-relative result/effect references without credentials, tokens, passwords, or arbitrary environment values.

## Details

An absent effect reference is not converted into a successful push claim.
