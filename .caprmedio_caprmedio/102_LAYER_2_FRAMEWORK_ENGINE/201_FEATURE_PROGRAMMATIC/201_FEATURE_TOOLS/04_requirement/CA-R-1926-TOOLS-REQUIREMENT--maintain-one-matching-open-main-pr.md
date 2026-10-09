---
atom_id: "CA-R-1926"
content_role: "Requirement"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Pull Request identity"
  depends_on: [Pull Request, Git Branch, Personal Remote]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-190, CA-O-196, CA-O-198, CA-M-368, CA-E-616, CA-D-617]
---
# Summary

Maintain one matching open `main` PR

## Scope

one public release Pull Request boundary.

## Claim

**the Operator** **must** discover, create, or update exactly one actual open PR from the selected `amm/dev` head to `main` on the selected personal remote.

## Details

Zero matches permits create after the initial gated push. More than one match, a changed existing identity, or an unsafe/nonmatching URL blocks the Workflow.
