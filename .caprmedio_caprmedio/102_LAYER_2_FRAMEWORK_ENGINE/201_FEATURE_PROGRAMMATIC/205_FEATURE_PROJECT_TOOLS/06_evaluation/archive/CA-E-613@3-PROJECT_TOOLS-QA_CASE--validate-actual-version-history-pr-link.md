---
atom_id: CA-E-613@3
content_role: Evaluation
type: QA Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Version History actual PR link
  depends_on:
  - Subject/Engineering/Release/Version History
  - Pull Request
  - Source Proof
version: 3
updated_at: 2026-10-23 03:14:50 +0400
relations:
  evaluation_for:
  - CA-R-1923
  - CA-M-366
---
# Summary

Validate actual Version History PR link

## Scope

one public Version History entry.

## Claim

**the Operator** **must** verify that an existing matching PR is linked before the initial public push, while a newly created PR causes finalization with its returned URL and never accepts a guessed URL or placeholder.

## Details

The entry contains only the concise selected-Version summary and that actual hyperlink.
