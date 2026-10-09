---
atom_id: "CA-R-1927"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release merge boundary"
  depends_on: [Workflow, Pull Request, Git Commit]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-188, CA-O-196, CA-M-368, CA-E-617, CA-D-617]
---
# Summary

Exclude merge from public-release Workflow

## Scope

one public-release Workflow execution.

## Claim

**the Operator** **must not** merge, approve, retarget, or otherwise adopt the public PR through this Workflow.

## Details

The terminal public result is an actual open or updated PR with evidence, not a release merge, protected-branch update, tag, or deployment.
