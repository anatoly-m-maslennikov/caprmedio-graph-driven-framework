---
atom_id: CA-M-364
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Recovery and cleanup"
  depends_on: [Tool, Runtime, Operator, Journal, Manifest]
relations:
  method_for: [CA-R-1912, CA-R-1916, CA-R-1917]
---
# Summary

Recover or clean installation state without replay

## Scope

the inspection-only recovery and later separately approved cleanup procedure.

## Claim

the INSTALL_TOOLS facade **must** recover by reopening exact retained evidence or clean by later exact approval, and **must not** replay uncertain effects, bypass a lock or delete unapproved paths.

## Details

1. Reopen selector, context, package, generation and Journal evidence under the target lock; report actual blocked, partial or recording-pending state.
2. Recover only missing recording whose immutable effect inputs and terminal ownership agree; do not rebuild, reselect or start a new run.
3. For cleanup, reopen CA-D-609's exact approval, inventory and quiescence result, then remove only listed paths and record result. Any disagreement refuses.
