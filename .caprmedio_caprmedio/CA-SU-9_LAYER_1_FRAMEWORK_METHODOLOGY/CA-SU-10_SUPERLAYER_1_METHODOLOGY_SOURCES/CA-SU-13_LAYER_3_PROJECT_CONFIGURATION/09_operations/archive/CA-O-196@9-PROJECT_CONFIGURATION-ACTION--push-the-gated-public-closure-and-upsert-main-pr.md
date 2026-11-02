---
atom_id: CA-O-196@9
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Carrier/Pull Request
  depends_on:
  - Subject/Graph Node/Carrier/Git Commit
  - Subject/Graph Node/Carrier/Git Repository
  - Subject/Graph Node/Carrier/Pull Request
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 9
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
---
# Summary

Push the gated public closure and upsert `main` PR

## Action

Push the gated public closure and upsert `main` PR **means** the native, explicitly authorized remote effect that records an immutable `amm/dev` commit/push proof and one actual matching open `main` PR identity.

## Details

This Action accepts only the selected personal remote scope. Its Tool-call effect references are evidence on this Action Run; a new PR URL is not assumed until the remote result returns it. Merge is excluded.
