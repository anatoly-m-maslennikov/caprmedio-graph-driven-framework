---
atom_id: "CA-D-617"
content_role: "Delivery"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Pull Request identity"
  depends_on: [Pull Request, Git Branch, Tool Call]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  delivery_for: [CA-R-1926, CA-R-1927]
---
# Summary

Serialize one actual public PR identity

## Scope

the PR result of one public-release remote action.

## Claim

public PR evidence **must** retain one actual HTTPS PR URL, positive PR number, open state, `amm/dev` head, `main` base, and repository-relative Tool-call result reference.

## Details

This representation records PR maintenance only. It contains no merge effect, merge receipt, or target-branch adoption claim.
