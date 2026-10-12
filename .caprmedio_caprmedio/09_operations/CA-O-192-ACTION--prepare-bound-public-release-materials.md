---
atom_id: "CA-O-192"
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Prepare bound public release materials"
  depends_on: [README, Pull Request, Version History, Source Proof, Tool Call, Version, Local Release]
version: 2
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-188, CA-O-191, CA-R-1922, CA-R-1923, CA-R-1928]
---
# Summary

Prepare bound public-release materials

## Action

Prepare bound public-release materials **means** the sole content prompt for one selected Version and source snapshot. It returns the full public PR body and concise Version History summary.

## Details

The PR body distinguishes What’s new and What’s fixed. README, Version History edits, and all remote effects are mechanical later work. If the actual URL is not yet known, CA-O-198 appends it after PR creation; no placeholder is valid. A different Version or changed code, Methodology, or package requires a fresh full suite before public release.
