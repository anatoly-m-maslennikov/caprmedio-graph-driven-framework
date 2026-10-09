---
atom_id: "CA-E-617"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release merge exclusion"
  depends_on: [Workflow, Pull Request, Tool]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1927, CA-M-368]
---
# Summary

Validate public release does not merge

## Scope

one public-release effect declaration.

## Claim

**the Operator** **must** verify that the native public-release binding exposes no merge, approval, target-retargeting, protected-branch update, tag, or deployment effect and ends with an open PR result only.

## Details

The absence of merge is verified from the declared binding and mocked effect trace, not inferred from intent.
