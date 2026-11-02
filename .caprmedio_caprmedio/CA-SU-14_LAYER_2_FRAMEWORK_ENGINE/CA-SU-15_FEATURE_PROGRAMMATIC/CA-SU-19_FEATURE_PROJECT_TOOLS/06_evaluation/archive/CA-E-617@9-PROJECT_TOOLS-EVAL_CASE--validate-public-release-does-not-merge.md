---
atom_id: CA-E-617@9
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Engineering/Pull Request
  - Subject/Graph Node/Engineering/Public Release/Merge Exclusion Evaluation
version: 9
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-R-1927
  - CA-M-368
tier: 5
---
# Summary

Validate public release does not merge

## Scope

one public-release effect declaration.

## Claim

**the Operator** **must** verify that the native public-release binding exposes no merge, approval, target-retargeting, protected-branch update, tag, or deployment effect and ends with an open PR result only.

## Details

The absence of merge is verified from the declared binding and mocked effect trace, not inferred from intent.
