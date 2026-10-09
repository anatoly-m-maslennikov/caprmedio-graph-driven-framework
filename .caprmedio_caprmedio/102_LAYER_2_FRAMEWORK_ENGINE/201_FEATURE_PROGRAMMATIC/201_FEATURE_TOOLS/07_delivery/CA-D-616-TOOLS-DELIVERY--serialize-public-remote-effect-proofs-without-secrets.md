---
atom_id: "CA-D-616"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public remote effect proof"
  depends_on: [Personal Remote, Git Commit, Tool Call, Journal]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  delivery_for: [CA-R-1921, CA-R-1925]
---
# Summary

Serialize public remote effect proofs without secrets

## Scope

the remote proof of one public push.

## Claim

public remote effect evidence **must** retain the personal remote identity, branch direction, immutable commit identity, and repository-relative result/effect references without credentials, tokens, passwords, or arbitrary environment values.

## Details

An absent effect reference is not converted into a successful push claim.
