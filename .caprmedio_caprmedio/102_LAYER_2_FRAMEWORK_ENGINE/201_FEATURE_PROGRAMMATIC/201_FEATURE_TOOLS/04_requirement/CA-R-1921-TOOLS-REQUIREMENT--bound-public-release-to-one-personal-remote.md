---
atom_id: "CA-R-1921"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release remote boundary"
  depends_on: [Personal Remote, Git Branch, Pull Request]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-188, CA-O-196, CA-M-365, CA-E-611, CA-D-616]
---
# Summary

Bind public release to one personal remote

## Scope

the selected remote boundary of one public release.

## Claim

**the Operator** **must** bind one public-release invocation to an explicit personal remote identity and the exact `amm/dev` to `main` branch direction.

## Details

The binding contains no credential or secret. A different remote, owner, head, base, or branch direction is out of scope and stops the invocation.
