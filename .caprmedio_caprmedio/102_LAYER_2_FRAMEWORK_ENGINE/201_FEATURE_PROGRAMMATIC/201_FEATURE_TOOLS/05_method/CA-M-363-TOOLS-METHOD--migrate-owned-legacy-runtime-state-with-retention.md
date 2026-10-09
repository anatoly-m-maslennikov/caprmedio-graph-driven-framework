---
atom_id: CA-M-363
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Legacy migration"
  depends_on: [Tool, Runtime, Process, Manifest, Journal]
relations:
  method_for: [CA-R-1914, CA-R-1915]
---
# Summary

Migrate owned legacy runtime state with retention

## Scope

the copy-verify-switch procedure for exactly three owned legacy subtrees.

## Claim

the INSTALL_TOOLS facade **must** inventory, safely quiesce, copy, verify and switch only owned legacy state while retaining old state and N/history, and **must not** delete or force-stop uncertain state.

## Details

1. Acquire the target installation lock and inventory exactly CA-D-605 roots.
2. Prove process ownership with generation and command evidence; block unsafe quiescence.
3. Stage copies, compare ordered source/destination digests and modes, then revalidate the inventory.
4. Atomically switch the target selector and retain history; failure leaves old state readable. Cleanup is outside this Method.
