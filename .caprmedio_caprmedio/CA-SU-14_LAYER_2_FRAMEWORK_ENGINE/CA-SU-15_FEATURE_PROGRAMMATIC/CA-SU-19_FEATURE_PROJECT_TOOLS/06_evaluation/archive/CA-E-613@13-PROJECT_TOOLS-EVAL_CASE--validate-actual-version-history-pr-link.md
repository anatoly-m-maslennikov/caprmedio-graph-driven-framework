---
atom_id: CA-E-613@13
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Delivery
  depends_on:
  - Subject/Graph Node/Carrier/Pull Request
version: 13
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-1923
  - CA-M-366
tier: 5
---
# Summary

Validate actual Version History PR link

## Scope

one public Version History entry.

## Claim

**the Operator** **must** verify that an existing matching PR is linked before the initial public push, while a newly created PR causes finalization with its returned URL and never accepts a guessed URL or placeholder.

## Details

The entry contains only the concise selected-Version summary and that actual hyperlink.
