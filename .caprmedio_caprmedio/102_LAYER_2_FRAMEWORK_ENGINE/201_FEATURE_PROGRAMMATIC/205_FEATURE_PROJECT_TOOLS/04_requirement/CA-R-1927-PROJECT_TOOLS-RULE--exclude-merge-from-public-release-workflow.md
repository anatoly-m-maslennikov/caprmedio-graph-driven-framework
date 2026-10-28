---
atom_id: CA-R-1927
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
version: 12
updated_at: 2026-10-27 20:00:05 +0400
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
