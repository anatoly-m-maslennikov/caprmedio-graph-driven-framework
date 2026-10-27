---
atom_id: CA-E-611@7
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Remote and Branch Boundary
  depends_on:
  - Subject/Engineering/Git/Remote
  - Subject/Engineering/Git/Branch
  - Subject/Engineering/Public Release/Remote and Branch Boundary Evaluation
version: 7
updated_at: 2026-10-24 20:11:44 +0400
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
