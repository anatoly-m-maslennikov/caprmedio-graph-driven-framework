---
atom_id: "CA-E-616"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Pull Request identity"
  depends_on: [Pull Request, Personal Remote, Tool]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1926, CA-M-368]
---
# Summary

Validate unique matching `main` PR

## Scope

one public-release PR discovery and update.

## Claim

**the Operator** **must** verify that zero matching PRs permits creation only after the initial push, one matching PR is reused, and duplicate, retargeted, closed, or URL-changed results stop before further material preparation or remote effects.

## Details

The final refresh must retain the same actual PR URL returned by the initial upsert.
