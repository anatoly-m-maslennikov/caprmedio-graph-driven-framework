---
atom_id: CA-R-1923@3
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Version History public release entry
  depends_on:
  - Subject/Engineering/Release/Version History
  - Pull Request
  - Version
version: 3
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
---
# Summary

Require an actual PR link in Version History

## Scope

one Version History entry for one public release.

## Claim

**the Operator** **must** record only a concise selected-Version summary and the actual matching public PR hyperlink in that Version History entry.

## Details

A guessed URL, placeholder, prose-only reference, or unrelated PR does not satisfy the Claim. When the actual URL becomes known after the initial push, CA-O-198 owns mechanical finalization and same-PR refresh without another suite or prompt.
