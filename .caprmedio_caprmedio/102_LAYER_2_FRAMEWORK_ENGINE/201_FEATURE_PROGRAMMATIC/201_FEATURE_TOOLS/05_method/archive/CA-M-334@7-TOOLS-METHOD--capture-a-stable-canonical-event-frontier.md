---
atom_id: CA-M-334@7
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Engineering/Journal Event Query/Stable Source Snapshot
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
relations:
  method_for:
  - CA-R-1861
  - CA-R-1866
type: Eng Decision
tier: 4
---
# Summary

Capture a stable canonical Event frontier

## Scope

Source snapshot construction.

## Claim

To capture the query source, the adapter **must**, before any workflow/action-start
recording or Action dispatch, read and seal the canonical Journal byte-prefix,
enumerate its recorded members once, decode their JSON with the ordinary codec
without row-shape, duplicate-key or unique-ID validation, and seal ordered
references, member byte hashes and actually supplied string Event IDs
into one opaque snapshot token. A standalone Action captures before its own Run
evidence and consumes exactly that token.

## Details

The method enforces configured member and byte maxima, detects changed, deleted,
truncated or unreadable members, and never silently
extends the frontier. Every continuation revalidates the original prefix and
members; later append outside the prefix remains permitted. Capture every decoded
row, including repeated IDs, missing or nonstring IDs, lists and scalar values;
recorded JSON remains unchanged. Snapshot event_ids contains only supplied string
IDs without deduplication. Query result wrappers use None for an absent or
nonstring ID; do not invent an Event identity or insert fields into stored data.
Coverage follows the actual rows and immutable member frontier, not ID uniqueness.
