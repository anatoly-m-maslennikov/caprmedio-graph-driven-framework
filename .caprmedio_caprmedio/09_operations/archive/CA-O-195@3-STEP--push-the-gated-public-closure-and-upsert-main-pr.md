---
atom_id: CA-O-195@3
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Public release/Step: push and upsert main PR'
  depends_on:
  - Git Commit
  - Personal Remote
  - Pull Request
version: 3
updated_at: 2026-10-12 00:41:30 +0000
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-196
---
# Summary

Push the public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after the content prompt to commit and push the prepared closure on `amm/dev`, then find its one matching open `main` PR or create it as Draft. An existing matching open PR is converted to Draft before its body is edited.

## Details

The Step records the pushed commit and actual Draft PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.
