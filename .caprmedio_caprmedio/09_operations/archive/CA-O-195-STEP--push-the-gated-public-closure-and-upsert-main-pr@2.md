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
  depends_on: [Git Commit, Personal Remote, Pull Request]
version: 2
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  part_of: [CA-O-188]
  invokes: [CA-O-196]
---
# Summary

Push the public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after the content prompt to commit and push the prepared closure on `amm/dev`, then find, create, or update its one `main` PR.

## Details

The Step records the pushed commit and actual PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.

