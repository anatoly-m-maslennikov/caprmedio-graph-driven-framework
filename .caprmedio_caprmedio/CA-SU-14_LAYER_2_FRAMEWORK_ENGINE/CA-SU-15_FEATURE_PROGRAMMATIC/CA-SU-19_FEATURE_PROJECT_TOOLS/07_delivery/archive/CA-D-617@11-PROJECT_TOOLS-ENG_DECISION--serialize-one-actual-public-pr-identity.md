---
atom_id: CA-D-617@11
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - Subject/Graph Node/Engineering/Public Release/Pull Request Identity
  - Subject/Graph Node/Engineering/Git/Branch
  - Subject/Graph Node/Domain/Occurrent/Execution
version: 11
updated_at: 2026-10-26 00:46:35 +0400
relations:
  delivery_for:
  - CA-R-1926
  - CA-R-1927
type: Eng Decision
tier: 4
---
# Summary

Serialize one actual public PR identity

## Scope

the PR result of one public-release remote action.

## Claim

public PR evidence **must** retain one actual HTTPS PR URL, positive PR number, open Draft state, `amm/dev` head, `main` base, and repository-relative Tool-call result reference.

## Details

This representation records PR maintenance only. A created PR is Draft, and an existing open PR is converted to Draft before its body is edited. It contains no merge effect, merge receipt, or target-branch adoption claim.
