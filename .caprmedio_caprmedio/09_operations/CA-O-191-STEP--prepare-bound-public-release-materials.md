---
atom_id: "CA-O-191"
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Public release/Step: prepare materials"
  depends_on: [README, Pull Request, Version History, Version, Journal]
version: 2
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-188]
  invokes: [CA-O-192]
---
# Summary

Prepare bound public-release materials

## Step

This Step invokes CA-O-192 once for the sole public-release content prompt: the full PR description and concise selected-Version History summary.

## Details

README, Version History, Git, and PR updates are mechanical later steps. A newly created actual PR URL is appended only by CA-O-198; this Step does not guess a URL, publish, or merge.
