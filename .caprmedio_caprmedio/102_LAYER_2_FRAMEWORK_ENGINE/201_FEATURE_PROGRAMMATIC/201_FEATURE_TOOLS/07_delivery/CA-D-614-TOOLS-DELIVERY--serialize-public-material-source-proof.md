---
atom_id: "CA-D-614"
content_role: "Delivery"
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
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public material source proof

## Scope

the material proof of one public documentation closure.

## Claim

public material source proof **must** carry repository-relative README, full PR body, Version History references, the selected candidate snapshot SHA-256, canonical Version value and `version.toml` SHA-256, and retained local-release gate, promotion and live-verification proof references without source contents, credentials, or secret values.

## Details

The Version History hyperlink is represented only after its actual PR URL is known and is checked against that remote result.

The Tool reopens these carriers and proofs before public effects. The canonical Version value and byte digest must equal the verified local-release identity; a changed Version requires the renewed local cycle governed by CA-R-1922-TOOLS-REQUIREMENT--bind-public-materials-to-the-selected-source-snapshot.
