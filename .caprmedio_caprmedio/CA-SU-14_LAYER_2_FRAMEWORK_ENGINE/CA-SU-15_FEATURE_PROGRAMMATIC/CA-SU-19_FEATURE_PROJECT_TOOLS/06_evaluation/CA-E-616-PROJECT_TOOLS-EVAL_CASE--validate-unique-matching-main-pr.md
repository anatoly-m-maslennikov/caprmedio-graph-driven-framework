---
atom_id: CA-E-616
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 11
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1926
  - CA-M-368
tier: 5
---
# Summary

Validate unique matching `main` PR

## Scope

one public-release PR discovery and update.

## Claim

**the Operator** **must** verify that zero matching PRs permits creation only after the initial push, one matching PR is reused, and duplicate, retargeted, closed, or URL-changed results stop before further material preparation or remote effects.

## Details

The final refresh must retain the same actual PR URL returned by the initial upsert.
