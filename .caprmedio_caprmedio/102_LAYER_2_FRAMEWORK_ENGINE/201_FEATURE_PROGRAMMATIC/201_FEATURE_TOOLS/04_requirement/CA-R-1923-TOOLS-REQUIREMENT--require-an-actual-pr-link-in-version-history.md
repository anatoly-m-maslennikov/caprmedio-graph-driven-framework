---
atom_id: "CA-R-1923"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Version History public release entry"
  depends_on: [Version History, Pull Request, Version]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-190, CA-O-192, CA-O-198, CA-M-366, CA-E-613, CA-D-615]
---
# Summary

Require an actual PR link in Version History

## Scope

one Version History entry for one public release.

## Claim

**the Operator** **must** record only a concise selected-Version summary and the actual matching public PR hyperlink in that Version History entry.

## Details

A guessed URL, placeholder, prose-only reference, or unrelated PR does not satisfy the Claim. When the URL is created after the initial gate, CA-O-198 owns the finalization and renewed gate.
