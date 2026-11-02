---
atom_id: CA-D-556
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 19:59:27 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
relations:
  delivery_for:
  - CA-R-1862
  - CA-R-1863
  - CA-R-1865
  - CA-R-1868
  - CA-R-1869
  - CA-R-1871
type: Eng Decision
tier: 4
---
# Summary

Encode the bounded Journal Event query interface

## Scope

The Tool input and result contract.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** deliver one bounded interface with a
snapshot token (source root, byte-prefix length/hash, ordered member hashes, and
Event-ID frontier), literal filter, JSON-Pointer Event selectors, result
selection, page request, and the shared configurable maxima for request bytes,
grammar depth, filter tokens, IN members, page size, selected fields, frontier
members, per-member bytes, total reads, timeout, and retained findings. Result
evidence reports each applicable configured and consumed/exhausted limit.

## Details

The interface has no SQL, code, secret, mutation, or implicit selection field.
