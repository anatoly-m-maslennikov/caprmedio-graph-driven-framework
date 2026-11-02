---
atom_id: CA-R-1927@3
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Public release merge boundary
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Pull Request
  - Git Commit
version: 3
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
---
# Summary

Exclude merge from public-release Workflow

## Scope

one public-release Workflow execution.

## Claim

**the Operator** **must not** merge, approve, retarget, or otherwise adopt the public PR through this Workflow.

## Details

The terminal public result is an actual open or updated PR with evidence, not a release merge, protected-branch update, tag, or deployment.
