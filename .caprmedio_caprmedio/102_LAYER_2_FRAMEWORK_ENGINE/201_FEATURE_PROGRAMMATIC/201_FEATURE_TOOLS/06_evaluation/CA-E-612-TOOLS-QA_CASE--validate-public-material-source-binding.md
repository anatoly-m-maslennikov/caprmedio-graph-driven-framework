---
atom_id: "CA-E-612"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release material source proof"
  depends_on: [README, Pull Request, Version History, Source Proof]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1922, CA-M-366]
---
# Summary

Validate public material source binding

## Scope

one selected public documentation closure.

## Claim

**the Operator** **must** verify that README, full PR body, Version History carrier, selected Version, and candidate snapshot remain the exact submitted source proof and reject substituted carrier or snapshot results.

## Details

The golden successful case contains distinct What’s new and What’s fixed PR sections.
