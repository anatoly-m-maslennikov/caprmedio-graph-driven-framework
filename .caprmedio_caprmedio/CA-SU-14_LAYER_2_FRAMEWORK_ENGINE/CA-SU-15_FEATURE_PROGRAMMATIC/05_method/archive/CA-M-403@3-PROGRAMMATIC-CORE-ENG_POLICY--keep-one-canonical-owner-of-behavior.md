---
atom_id: CA-M-403@3
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Archived
subjects:
  governs: Subject/Engineering/Behavior Ownership
  depends_on:
  - Subject/Engineering/Authoritative Representation
version: 3
updated_at: 2026-10-23 23:34:06 +0400
author: Anatoly Maslennikov
---
# Summary

Keep one canonical owner of behavior

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** expose a declared capability through different transports, adapters or storage backends, reuse its canonical behavioral owner rather than independently redefining its meaning.

## Details

Candidate source: [CA-M-387@2](archive/CA-M-387-PROGRAMMATIC-CORE--keep-one-canonical-owner-of-behavior@2.md)

- Adapters translate supported requests and results; they do not invent domain decisions or hidden Workflow composition.
- Keep identity, lifecycle, semantic admission and sequencing with their declared owner.
- Replacing a transport or backend must not silently change the declared capability.

Source basis: CA-M-341, CA-M-376.
