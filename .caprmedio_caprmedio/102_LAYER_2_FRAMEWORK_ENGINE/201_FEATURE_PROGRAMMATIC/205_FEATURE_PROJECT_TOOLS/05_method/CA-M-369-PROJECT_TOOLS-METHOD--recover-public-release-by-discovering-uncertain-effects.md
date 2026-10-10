---
atom_id: "CA-M-369"
content_role: "Method"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release recovery evidence"
  depends_on: [Journal, Git Commit, Pull Request, Tool Call]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  method_for: [CA-R-1928, CA-R-1929]
---
# Summary

Recover public release by discovering uncertain effects

## Scope

recovery after one interrupted public remote effect.

## Claim

**the Operator** **must** restore only existing schema-v5 Run evidence, discover an unknown push or PR from the remote, and require a fresh explicitly authorized continuation instead of replaying uncertainty.

## Details

Tool-call references remain parented evidence. Recording-only recovery cannot turn an unknown remote result into completed execution.
