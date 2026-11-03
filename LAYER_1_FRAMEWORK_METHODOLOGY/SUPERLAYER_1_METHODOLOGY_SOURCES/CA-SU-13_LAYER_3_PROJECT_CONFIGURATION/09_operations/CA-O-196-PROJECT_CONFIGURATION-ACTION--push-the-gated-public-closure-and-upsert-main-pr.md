---
atom_id: CA-O-196
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Pull Request
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 10
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
---
# Summary

Push the gated public closure and upsert `main` PR

## Action

Push the gated public closure and upsert `main` PR **means** the native, explicitly authorized remote effect that records an immutable `amm/dev` commit/push proof and one actual matching open `main` PR identity.

## Details

This Action accepts only the selected personal remote scope. Its Tool-call effect references are evidence on this Action Run; a new PR URL is not assumed until the remote result returns it. Merge is excluded.
