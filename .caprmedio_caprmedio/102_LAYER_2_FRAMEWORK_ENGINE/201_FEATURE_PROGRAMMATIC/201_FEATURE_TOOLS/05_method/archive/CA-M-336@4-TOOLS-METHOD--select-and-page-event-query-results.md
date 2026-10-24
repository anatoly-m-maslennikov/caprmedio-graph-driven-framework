---
atom_id: CA-M-336@4
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 23:09:56 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Journal Event Query/Result Selection and Paging
relations:
  method_for:
  - CA-R-1863
  - CA-R-1865
  - CA-R-1871
type: Eng Decision
---
# Summary

Select and page Event query results

## Scope

Result construction.

## Claim

To construct results, the Tool **must** order snapshot matches deterministically, apply the bounded page, and expose IDs, selected fields, or full Events only in the requested mode with truthful coverage metadata.

## Details

The next-page token remains bound to the source snapshot, source/prefix hashes,
result selection, and configured limits. Before any continuation it revalidates
captured members and rejects changed, deleted, unreadable, or truncated captured
data, while allowing append strictly after the sealed prefix.
