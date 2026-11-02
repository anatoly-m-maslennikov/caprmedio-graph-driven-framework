---
content_role: Method
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "programmatic software"
  depends_on: [Implementation]
version: 2
updated_at: "2026-10-15 22:15:37 +0400"
atom_id: CA-M-389
---
# Summary

Pass validated configuration through one shared boundary

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement behavior that depends on Project Settings, resolve and validate the authoritative settings through one shared Reader, then pass an immutable snapshot explicitly to consumers **without** duplicating parsing, inventing fallback values or turning the snapshot into authority.

## Details

- Keep the Reader read-only; settings changes use the authoritative Artifact's dedicated writer.
- Preserve the actual values and source provenance in the snapshot.
- Keep component-specific interpretation and behavior outside the shared Reader.

Source basis: CA-M-284.
