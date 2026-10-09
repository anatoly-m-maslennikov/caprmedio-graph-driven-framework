---
atom_id: "CA-R-1922"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release material source proof"
  depends_on: [README, Pull Request, Version History, Source Proof, Version, Local Release]
version: 1
updated_at: "2026-10-09 17:05:28 +0400"
relations:
  relates_to: [CA-O-192, CA-O-194, CA-O-198, CA-M-366, CA-E-612, CA-D-614]
---
# Summary

Bind public materials to the selected source snapshot

## Scope

one selected public documentation closure.

## Claim

the public-release Tool **must** bind the README, full PR description, concise Version History carrier, selected Version, and candidate snapshot to one source proof before public gating.

## Details

The full PR description separately states What’s new and What’s fixed. A substituted carrier, version, or candidate snapshot invalidates its gate evidence.

The selected Version value and exact root `version.toml` byte digest must agree with the reopened verified local-release Version and its retained gate, promotion and live-verification proof. If public preparation changes the Version, publication requires a fresh local candidate, full local gate, same-bytes promotion and live verification first. A public-only Full Gate cannot substitute for that local release.
