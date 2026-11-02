---
atom_id: "CA-O-191"
content_role: Operations
type: Step
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Public release/Step: prepare materials"
  depends_on: [README, Pull Request, Version History, Version, Journal]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  part_of: [CA-O-188]
  invokes: [CA-O-192]
---
# Summary

Prepare bound public-release materials

## Step

This Step invokes CA-O-192 once to prepare the selected README and full PR description, plus the concise selected-Version History content only when an actual matching PR URL was already discovered.

## Details

No guessed URL or placeholder is valid Version History content. Material preparation returns source proofs; it does not itself publish or merge them.
