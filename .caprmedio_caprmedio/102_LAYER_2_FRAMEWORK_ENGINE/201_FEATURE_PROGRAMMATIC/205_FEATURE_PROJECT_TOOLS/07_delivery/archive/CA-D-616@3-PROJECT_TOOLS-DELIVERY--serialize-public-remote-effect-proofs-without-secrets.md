---
atom_id: CA-D-616@3
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Public remote effect proof
  depends_on:
  - Personal Remote
  - Git Commit
  - Subject/Domain/Node/Occurrent/Execution
  - Journal
version: 3
updated_at: 2026-10-23 23:34:06 +0400
relations:
  delivery_for:
  - CA-R-1921
  - CA-R-1925
type: Eng Decision
---
# Summary

Serialize public remote effect proofs without secrets

## Scope

the remote proof of one public push.

## Claim

public remote effect evidence **must** retain the personal remote identity, branch direction, immutable commit identity, and repository-relative result/effect references without credentials, tokens, passwords, or arbitrary environment values.

## Details

An absent effect reference is not converted into a successful push claim.
