---
atom_id: "CA-O-190"
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Discover matching public main Pull Request"
  depends_on: [Pull Request, Personal Remote, Tool Call, Journal]
version: 1
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-188, CA-O-189, CA-R-1923, CA-R-1926, CA-R-1928]
---
# Summary

Discover a matching public `main` PR

## Action

Discover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and `amm/dev` to `main` boundary.

## Details

The Tool-call input, result, and report references remain evidence of this Action Run. It neither creates nor updates a PR and does not claim an MCP route.
