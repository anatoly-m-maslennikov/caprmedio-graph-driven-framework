---
atom_id: "CA-O-196"
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Push gated public closure and upsert main Pull Request"
  depends_on: [Git Commit, Personal Remote, Pull Request, Tool Call, Journal]
version: 2
updated_at: "2026-10-14 12:35:36 +0000"
relations: {}
---
# Summary

Push the gated public closure and upsert `main` PR

## Action

Push the gated public closure and upsert `main` PR **means** the native, explicitly authorized remote effect that records an immutable `amm/dev` commit/push proof and one actual matching open `main` PR identity.

## Details

This Action accepts only the selected personal remote scope. Its Tool-call effect references are evidence on this Action Run; a new PR URL is not assumed until the remote result returns it. Merge is excluded.
