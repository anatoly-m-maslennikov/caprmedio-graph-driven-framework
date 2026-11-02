---
atom_id: CA-M-426@2
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
subjects:
  governs: Subject/Engineering/Pure Computation and Recording Boundary
  depends_on:
  - Subject/Engineering/Effect Boundary
  - Subject/Engineering/Outcome Evidence
version: 2
updated_at: 2026-10-22 16:26:49 +0000
author: Anatoly Maslennikov
---
# Summary

Separate pure computation from effects and recording

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** construct a result, keep pure computation independent of persistence and Run or Journal writes, leaving those effects with their declared execution owners.

## Details

Candidate source: [CA-M-392@2](archive/CA-M-392-PROGRAMMATIC-CORE--separate-pure-computation-from-effects-and-recording@2.md)

- Construct from bound inputs and return results and diagnostics without hidden writes.
- Persist an output only through its applicable authorized effect boundary.
- Actual execution recording remains with its declared executor; generated output alone does not establish durable terminal completion.

Source basis: CA-M-330, CA-M-259.
