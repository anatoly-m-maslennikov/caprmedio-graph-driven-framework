---
atom_id: CA-R-1925@2
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: Archived
subjects:
  governs: "Public push proof"
  depends_on: [Git Commit, Personal Remote, Tool Call, Journal]
version: 2
updated_at: "2026-10-14 12:27:48 +0000"
relations: {}
---
# Summary

Require immutable proof for public push

## Scope

one public `amm/dev` push effect.

## Claim

**the Operator** **must** retain an immutable commit identity and remote effect reference for every public push of the selected public source/material bindings.

## Details

The proof is evidence on the parent Action Run. Failure, partial effect, or absent proof does not permit PR advancement or inferred success.
