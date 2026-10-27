---
atom_id: CA-D-616@10
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Outcome Evidence
  depends_on:
  - Subject/Engineering/Git/Remote
  - Subject/Engineering/Git/Commit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
version: 10
updated_at: 2026-10-24 23:44:24 +0400
relations:
  delivery_for:
  - CA-R-1921
  - CA-R-1925
type: Eng Decision
tier: 4
---
# Summary

Serialize public remote effect proofs without secrets

## Scope

the remote proof of one public push.

## Claim

public remote effect evidence **must** retain the personal remote identity, branch direction, immutable commit identity, and repository-relative result/effect references without credentials, tokens, passwords, or arbitrary environment values.

## Details

An absent effect reference is not converted into a successful push claim.
