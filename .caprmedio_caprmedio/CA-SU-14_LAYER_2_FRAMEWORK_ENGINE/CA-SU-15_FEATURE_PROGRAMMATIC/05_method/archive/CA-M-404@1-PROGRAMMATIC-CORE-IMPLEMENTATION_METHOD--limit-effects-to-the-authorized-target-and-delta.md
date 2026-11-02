---
atom_id: CA-M-404@1
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Core"
global_tier: 6
status: Archived
subjects:
  governs: "Method/Effect Authorization"
  depends_on:
    - "Method/Implementation Authorization"
    - "Method/Behavior Ownership"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Limit effects to the authorized target and delta

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** change state, bind the admitted target, explicit delta and required expected state, then apply **only** that authorized change.

## Details

Candidate source: [CA-M-388@2](archive/CA-M-388-PROGRAMMATIC-CORE--limit-effects-to-the-authorized-target-and-delta@2.md)

- Do not substitute targets, broaden the affected frontier or add semantic operations.
- Observing additional files or state does not grant permission to change them.
- An unresolved, ambiguous, stale or unsupported binding stops the affected change; it does not authorize a fallback target or broader effect.

Source basis: CA-M-376, CA-M-381.
