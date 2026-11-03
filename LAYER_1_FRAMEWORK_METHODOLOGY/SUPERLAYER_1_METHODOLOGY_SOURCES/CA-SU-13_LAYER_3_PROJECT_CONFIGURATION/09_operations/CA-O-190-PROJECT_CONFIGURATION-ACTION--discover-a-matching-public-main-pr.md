---
atom_id: CA-O-190
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Pull Request
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 10
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
---
# Summary

Discover a matching public `main` PR

## Action

Discover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and `amm/dev` to `main` boundary.

## Details

The Tool-call input, result, and report references remain evidence of this Action Run. It neither creates nor updates a PR and does not claim an MCP route.
