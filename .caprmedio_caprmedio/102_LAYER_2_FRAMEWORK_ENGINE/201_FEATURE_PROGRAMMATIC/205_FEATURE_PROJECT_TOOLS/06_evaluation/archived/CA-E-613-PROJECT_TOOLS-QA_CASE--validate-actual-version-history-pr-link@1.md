---
atom_id: "CA-E-613"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Version History actual PR link"
  depends_on: [Version History, Pull Request, Source Proof]
version: 1
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  evaluation_for: [CA-R-1923, CA-M-366]
---
# Summary

Validate actual Version History PR link

## Scope

one public Version History entry.

## Claim

**the Operator** **must** verify that an existing matching PR is linked before the first gate, while a newly created PR causes finalization with its returned URL and never accepts a guessed URL or placeholder.

## Details

The entry contains only the concise selected-Version summary and that actual hyperlink.
