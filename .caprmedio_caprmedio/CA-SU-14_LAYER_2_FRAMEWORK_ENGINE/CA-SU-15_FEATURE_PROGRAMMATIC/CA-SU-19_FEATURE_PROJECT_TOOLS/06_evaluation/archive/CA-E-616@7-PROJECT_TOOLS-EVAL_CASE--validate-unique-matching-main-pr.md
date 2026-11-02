---
atom_id: CA-E-616@7
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Pull Request Identity
  depends_on:
  - Subject/Engineering/Pull Request
  - Subject/Engineering/Git/Remote
  - Subject/Engineering/Public Release/Pull Request Identity Evaluation
version: 7
updated_at: 2026-10-24 20:11:44 +0400
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
