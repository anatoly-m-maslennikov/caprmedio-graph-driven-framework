---
atom_id: "CA-M-368"
content_role: "Method"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release remote effects"
  depends_on: [Git Commit, Personal Remote, Pull Request, Tool Call]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  method_for: [CA-R-1925, CA-R-1926, CA-R-1927]
---
# Summary

Bind public remote effects to one PR identity

## Scope

the selected `amm/dev` push and `main` PR maintenance sequence.

## Claim

**the Operator** **must** use admitted native bindings to prove the immutable pushed commit and retain exactly one matching open PR identity through its create/update and any final refresh.

## Details

The bindings may use local subprocess facilities after their own admission; this Method adds no MCP prerequisite. It excludes merge and makes an identity change a stop condition.
