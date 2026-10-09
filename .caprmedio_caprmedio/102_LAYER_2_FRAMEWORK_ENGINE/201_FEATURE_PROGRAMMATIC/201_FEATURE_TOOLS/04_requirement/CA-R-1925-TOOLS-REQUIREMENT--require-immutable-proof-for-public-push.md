---
atom_id: "CA-R-1925"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public push proof"
  depends_on: [Git Commit, Personal Remote, Tool Call, Journal]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-196, CA-O-198, CA-M-368, CA-E-615, CA-D-616]
---
# Summary

Require immutable proof for public push

## Scope

one public `amm/dev` push effect.

## Claim

**the Operator** **must** retain an immutable commit identity and remote effect reference for every public push of a gated source snapshot.

## Details

The proof is evidence on the parent Action Run. Failure, partial effect, or absent proof does not permit PR advancement or inferred success.
