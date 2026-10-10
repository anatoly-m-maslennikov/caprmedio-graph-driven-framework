---
atom_id: "CA-O-192"
content_role: Operations
type: Action
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Prepare bound public release materials"
  depends_on: [README, Pull Request, Version History, Source Proof, Tool Call, Version, Local Release]
version: 1
updated_at: "2026-10-09 17:05:28 +0400"
relations:
  relates_to: [CA-O-188, CA-O-191, CA-R-1922, CA-R-1923, CA-R-1928]
---
# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the native preparation of the full public PR body, README change, and concise Version History summary for one selected Version and source snapshot.

## Details

The PR body must distinguish What’s new and What’s fixed. Version History is limited to its concise summary and its actual matching PR hyperlink; if that URL does not yet exist, this Action leaves the link for CA-O-198 rather than fabricating one.

Bind the canonical `version.toml` value and bytes to the reopened verified local-release gate, promotion and live-verification proof. If preparation selects a different Version, return the requirement for a fresh local candidate, gate, promotion and verification before any public publication; do not treat a public-only gate as sufficient.
