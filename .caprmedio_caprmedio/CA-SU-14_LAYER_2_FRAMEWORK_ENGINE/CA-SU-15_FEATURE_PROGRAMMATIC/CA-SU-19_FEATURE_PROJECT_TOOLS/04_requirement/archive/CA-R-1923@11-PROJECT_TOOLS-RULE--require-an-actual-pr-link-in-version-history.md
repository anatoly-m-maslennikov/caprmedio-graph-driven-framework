---
atom_id: CA-R-1923@11
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Delivery
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History
  - Subject/Graph Node/Carrier/Pull Request
  - Subject/Graph Node/Domain/Continuant/History/Release.ID
version: 11
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Require an actual PR link in Version History

## Scope

one Version History entry for one public release.

## Claim

**the Operator** **must** record only a concise selected-Version summary and the actual matching public PR hyperlink in that Version History entry.

## Details

A guessed URL, placeholder, prose-only reference, or unrelated PR does not satisfy the Claim. When the actual URL becomes known after the initial push, CA-O-198 owns mechanical finalization and same-PR refresh without another suite or prompt.
