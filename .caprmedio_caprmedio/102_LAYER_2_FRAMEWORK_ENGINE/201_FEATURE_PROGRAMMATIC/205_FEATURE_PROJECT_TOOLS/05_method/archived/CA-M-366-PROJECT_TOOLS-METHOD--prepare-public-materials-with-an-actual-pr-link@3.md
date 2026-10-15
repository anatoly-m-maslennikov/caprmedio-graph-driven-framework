---
atom_id: "CA-M-366"
content_role: "Method"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release documentation preparation"
  depends_on: [README, Pull Request, Version History, Source Proof]
version: 3
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  method_for: [CA-R-1922, CA-R-1923]
---
# Summary

Prepare public materials with an actual PR link

## Scope

the selected public documentation closure.

## Claim

the public-release Tool **must** prepare README, one full PR body, and short Version History bullets from the selected Version. Its one public-writing prompt produces the full PR body with distinct **What's new** and **What's fixed** sections. It discovers an existing matching PR before push and defers a new Version History hyperlink until the remote returns its actual PR URL.

## Details

Version History remains a concise summary plus actual URL. The Tool completes the one fresh public suite after its initial material closure is frozen and before its first publication. If no matching PR exists, it adds that URL through one mechanical metadata-only follow-up commit and push after creation. That follow-up reopens the retained Public Full Gate; it does not rerun the suite, request a separate review or prompt, or change the tested candidate.
