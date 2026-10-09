---
atom_id: "CA-M-366"
content_role: "Method"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release documentation preparation"
  depends_on: [README, Pull Request, Version History, Source Proof]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  method_for: [CA-R-1922, CA-R-1923]
---
# Summary

Prepare public materials with an actual PR link

## Scope

the selected public documentation closure.

## Claim

**the Operator** **must** prepare README and full PR description from the selected Version early, discover an existing matching PR before freeze, and defer a new Version History hyperlink until the remote returns its actual PR URL.

## Details

The PR description separates What’s new from What’s fixed. Version History remains a concise summary plus actual URL, so a new URL changes the closure and requires CA-M-367.
