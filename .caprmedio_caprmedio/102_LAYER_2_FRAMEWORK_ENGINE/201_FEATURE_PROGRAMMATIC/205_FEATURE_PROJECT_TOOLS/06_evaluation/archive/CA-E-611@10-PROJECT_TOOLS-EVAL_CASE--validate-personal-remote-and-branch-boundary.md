---
atom_id: CA-E-611@10
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Delivery
  depends_on:
  - Subject/Graph Node/Carrier/Git Repository
  - Subject/Graph Node/Carrier/Git Branch
  - Subject/Graph Node/Engineering/Verification
version: 10
updated_at: 2026-10-27 06:04:45 +0400
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
