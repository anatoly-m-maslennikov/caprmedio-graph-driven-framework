---
atom_id: CA-M-368@5
content_role: Method
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Public release remote effects
  depends_on:
  - Git Commit
  - Personal Remote
  - Subject/Engineering/Pull Request
  - Subject/Domain/Node/Occurrent/Execution
version: 5
updated_at: 2026-10-24 01:18:03 +0400
relations:
  method_for:
  - CA-R-1925
  - CA-R-1926
  - CA-R-1927
type: Eng Decision
tier: 3
---
# Summary

Bind public remote effects to one PR identity

## Scope

the selected `amm/dev` push and `main` PR maintenance sequence.

## Claim

**the Operator** **must** use admitted native bindings to prove the immutable pushed commit and retain exactly one matching open PR identity through its create/update and any final refresh.

## Details

The bindings may use local subprocess facilities after their own admission; this Method adds no MCP prerequisite. It excludes merge and makes an identity change a stop condition.
