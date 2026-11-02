---
atom_id: CA-M-398
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21T18:40:43Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  child_of: [CA-M-390]
  relates_to: [CA-M-388, CA-M-397]
---
# Summary

Return verified partial results before failure details

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

When an operation has completed only part of the request, retain and present the verified completed results first, followed by the attributable errors and unfinished or uncertain work, without representing aggregate success.

## Details

1. At the operation owner, retain actual completed items and observed effects as work proceeds. A general exception wrapper cannot reconstruct lost local progress or decide business commit boundaries.
2. Return completed data together with errors in the same applicable response contract. Mark incompleteness or partial outcome explicitly and identify failed, skipped, unattempted and uncertain items where known. Do not discard useful verified data because another independent item failed.
3. Results-before-errors is presentation and consumption priority, not a demand for JSON member ordering or a new universal response schema. Preserve each transport's governed result contract while making both available.
4. Do not label an unverified, rolled-back or uncertain effect as completed, leak unsafe/private intermediate data, broaden an effect frontier, or weaken an explicitly atomic operation. If no verified result exists, state that honestly.
5. Do not introduce automatic retry, compensation or replay. Preserve actual recovery information and leave those actions with their declared owner.
