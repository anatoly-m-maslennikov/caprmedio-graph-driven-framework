---
atom_id: CA-R-1923@5
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Version History public release entry
  depends_on:
  - Subject/Engineering/Release/Version History
  - Subject/Engineering/Pull Request
  - Version
version: 5
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
tier: 3
---
# Summary

Require an actual PR link in Version History

## Scope

one Version History entry for one public release.

## Claim

**the Operator** **must** record only a concise selected-Version summary and the actual matching public PR hyperlink in that Version History entry.

## Details

A guessed URL, placeholder, prose-only reference, or unrelated PR does not satisfy the Claim. When the actual URL becomes known after the initial push, CA-O-198 owns mechanical finalization and same-PR refresh without another suite or prompt.
