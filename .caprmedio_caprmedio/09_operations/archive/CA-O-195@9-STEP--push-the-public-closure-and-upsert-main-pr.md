---
atom_id: CA-O-195@9
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Public release/Step: push and upsert main PR'
  depends_on:
  - Subject/Graph Node/Engineering/Git Commit
  - Subject/Graph Node/Engineering/Personal Remote
  - Subject/Graph Node/Engineering/Pull Request
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-196
tier: 3
---
# Summary

Push the public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after the content prompt to commit and push the prepared closure on `amm/dev`, then find its one matching open `main` PR or create it as Draft. An existing matching open PR is converted to Draft before its body is edited.

## Details

The Step records the pushed commit and actual Draft PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.
