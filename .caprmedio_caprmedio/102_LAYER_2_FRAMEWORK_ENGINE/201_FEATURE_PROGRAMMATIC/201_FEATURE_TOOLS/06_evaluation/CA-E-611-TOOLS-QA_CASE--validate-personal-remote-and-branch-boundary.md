---
atom_id: "CA-E-611"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release remote boundary"
  depends_on: [Personal Remote, Git Branch, Tool]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1921, CA-M-365]
---
# Summary

Validate personal remote and branch boundary

## Scope

the remote and branch fields of one public-release request.

## Claim

**the Operator** **must** verify that only an explicit personal remote with `amm/dev` head and `main` base is admitted, while missing remote identity, another scope, or any branch change is refused before effects.

## Details

The case verifies configuration boundaries, not remote credentials or GitHub access.
