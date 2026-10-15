---
content_role: Method
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Draft
revision_lineage: {"history_entry_ref": {"history_revision": "dbe8ae8cb52047d4a6e61c0f6108d6eb", "path": ".caprmedio_caprmedio/archive/_draft_history/dbe8ae8cb52047d4a6e61c0f6108d6eb.json"}}
author: Anatoly Maslennikov
subjects:
  governs: "programmatic software"
  depends_on: [Implementation]
version: 2
updated_at: "2026-10-15 22:15:20 +0400"
---
# Summary

Limit effects to the authorized target and delta

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** change state, bind the admitted target, explicit delta and required expected state, then apply **only** that authorized change.

## Details

- Do not substitute targets, broaden the affected frontier or add semantic operations.
- Observing additional files or state does not grant permission to change them.
- An unresolved, ambiguous, stale or unsupported binding stops the affected change; it does not authorize a fallback target or broader effect.

Source basis: CA-M-376, CA-M-381.
