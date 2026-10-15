---
content_role: Method
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "programmatic software"
  depends_on: [Implementation]
version: 1
updated_at: "2026-10-15 22:01:28 +0400"
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
