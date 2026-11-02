---
atom_id: CA-R-1927@9
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Public release merge boundary
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Engineering/Pull Request
  - Subject/Graph Node/Engineering/Git/Commit
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Exclude merge from public-release Workflow

## Scope

one public-release Workflow execution.

## Claim

**the Operator** **must not** merge, approve, retarget, or otherwise adopt the public PR through this Workflow.

## Details

The terminal public result is an actual open or updated PR with evidence, not a release merge, protected-branch update, tag, or deployment.
