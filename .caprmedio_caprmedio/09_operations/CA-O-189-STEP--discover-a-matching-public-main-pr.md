---
atom_id: "CA-O-189"
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Public release/Step: discover matching main PR"
  depends_on: [Pull Request, Personal Remote, Journal]
version: 1
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-188]
  invokes: [CA-O-190]
---
# Summary

Discover a matching public `main` PR

## Step

This Step invokes CA-O-190 once before public-source freeze and records zero or one actual open Pull Request from `amm/dev` to `main` on the selected personal remote.

## Details

More than one match, a nonmatching base/head, an unsafe URL, or unavailable observation stops the Workflow. Discovery is read-only and does not infer a future URL.
