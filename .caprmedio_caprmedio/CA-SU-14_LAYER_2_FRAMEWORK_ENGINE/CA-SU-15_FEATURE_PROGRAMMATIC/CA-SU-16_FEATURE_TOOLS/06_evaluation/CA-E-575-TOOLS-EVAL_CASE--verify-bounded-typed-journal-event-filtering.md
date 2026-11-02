---
atom_id: CA-E-575
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation/Type: Eval Case'
relations:
  evaluation_for:
  - CA-R-1850
  - CA-R-1862
  - CA-R-1868
  - CA-R-1869
tier: 4
---
# Summary

Verify bounded typed Journal Event filtering

## Claim

The Tool applies CA-R-1850 unchanged to every valid canonical Event selector and rejects only unknown or ambiguous Event selectors at its local boundary.

## Test case

Query a fixed snapshot containing scalar, null, array, object, nested,
escaped-key, and array-index values through shared valid/invalid fixtures, plus
unknown, bad-pointer, and dot-qualified Event selectors.

The fixed snapshot includes one Event with `optional: null` and one Event
without `optional`: the valid selector `event:/optional` compared with `null`
matches only the explicit-null Event, while the missing-field comparison is
false under CA-R-1850.

## Acceptance criteria

Shared valid and invalid cases preserve CA-R-1850 results for every Event value
type, including the explicit missing-versus-null fixture; local invalid
selectors return invalid-filter diagnostics and no fallback.
Request-byte, depth, token, IN-member, page-size, selected-field, timeout, and
retained-finding maxima each reject at maximum plus one (or time out) and expose
configured and consumed budget evidence.

## Failure disposition

Reject a divergent local grammar, selector fallback, or filename-based value.
