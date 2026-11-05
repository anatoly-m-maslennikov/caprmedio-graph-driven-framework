---
atom_id: CA-M-334
ref_id: CA-M-334
role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:42 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
relations:
  method_for:
  - CA-R-1861
  - CA-R-1866
form: Eng Decision
tier: 4
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-M-334-TOOLS-ENG_DECISION--capture-a-stable-canonical-event-frontier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method
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
