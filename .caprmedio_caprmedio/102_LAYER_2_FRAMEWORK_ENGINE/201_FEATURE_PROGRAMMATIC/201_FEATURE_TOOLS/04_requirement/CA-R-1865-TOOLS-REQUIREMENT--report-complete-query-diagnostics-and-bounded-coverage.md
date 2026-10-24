---
atom_id: CA-R-1865
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Journal Event Query/Diagnostics and Coverage
relations:
  relates_to:
  - CA-O-162
  - CA-E-577
type: Rule
tier: 3
---
# Summary

Report complete query diagnostics and bounded coverage

## Scope

Query failure and coverage reporting.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** reject and report malformed Events, raw
duplicate JSON keys before parse, missing IDs, duplicate IDs across the captured
frontier, incomplete reads, invalid filters, changed/deleted/truncated captured
members, configurable-budget exhaustion, coverage, and pagination truthfully
without silent skipping.

## Details

The shared configured maxima govern request bytes, expression depth, filter
tokens, IN members, page size, selected fields, frontier members, per-member
bytes, total read bytes, timeout, and retained findings. Each result identifies
the applicable configured limit and consumption/exhaustion state, scanned
coverage, matched and returned counts when determinable, continuation
availability, and every blocking or partial-read diagnostic.
