---
atom_id: CA-E-611
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 11
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1921
  - CA-M-365
tier: 5
---
# Summary

Validate personal remote and branch boundary

## Scope

the remote and branch fields of one public-release request.

## Claim

**the Operator** **must** verify that only an explicit personal remote with `amm/dev` head and `main` base is admitted, while missing remote identity, another scope, or any branch change is refused before effects.

## Details

The case verifies configuration boundaries, not remote credentials or GitHub access.
