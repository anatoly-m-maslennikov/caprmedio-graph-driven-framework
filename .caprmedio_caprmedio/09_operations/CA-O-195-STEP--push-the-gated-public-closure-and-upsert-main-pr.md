---
atom_id: "CA-O-195"
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Public release/Step: push and upsert main PR"
  depends_on: [Git Commit, Personal Remote, Pull Request, Full Gate, Journal]
version: 1
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-188]
  invokes: [CA-O-196]
---
# Summary

Push the gated public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after CA-O-193 to commit and push the exact gated closure on `amm/dev`, then find, create, or update its one `main` PR.

## Details

An immutable commit proof and actual PR identity are required. The Step cannot merge, retarget, or silently retry an unknown push or PR effect.
