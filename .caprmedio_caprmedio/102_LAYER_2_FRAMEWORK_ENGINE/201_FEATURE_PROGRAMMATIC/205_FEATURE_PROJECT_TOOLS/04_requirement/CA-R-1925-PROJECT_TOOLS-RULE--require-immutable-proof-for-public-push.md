---
atom_id: CA-R-1925
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 14
updated_at: 2026-10-27 20:00:05 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Require immutable proof for public push

## Scope

one public `amm/dev` push effect.

## Claim

**the Operator** **must** retain an immutable commit identity and remote effect reference for every public push of the selected public source/material bindings.

## Details

The proof is evidence on the parent Action Run. Failure, partial effect, or absent proof does not permit PR advancement or inferred success.
