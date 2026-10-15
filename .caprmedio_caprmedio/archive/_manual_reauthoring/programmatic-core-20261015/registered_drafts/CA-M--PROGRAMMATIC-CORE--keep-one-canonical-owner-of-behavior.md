---
content_role: Method
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Draft
revision_lineage: {"history_entry_ref": {"history_revision": "d840c56ffc454b938fcd7c09dbdfbea9", "path": ".caprmedio_caprmedio/archive/_draft_history/d840c56ffc454b938fcd7c09dbdfbea9.json"}}
author: Anatoly Maslennikov
subjects:
  governs: "programmatic software"
  depends_on: [Implementation]
version: 2
updated_at: "2026-10-15 22:15:20 +0400"
---
# Summary

Keep one canonical owner of behavior

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** expose a declared capability through different transports, adapters or storage backends, reuse its canonical behavioral owner rather than independently redefining its meaning.

## Details

- Adapters translate supported requests and results; they do not invent domain decisions or hidden Workflow composition.
- Keep identity, lifecycle, semantic admission and sequencing with their declared owner.
- Replacing a transport or backend must not silently change the declared capability.

Source basis: CA-M-341, CA-M-376.
