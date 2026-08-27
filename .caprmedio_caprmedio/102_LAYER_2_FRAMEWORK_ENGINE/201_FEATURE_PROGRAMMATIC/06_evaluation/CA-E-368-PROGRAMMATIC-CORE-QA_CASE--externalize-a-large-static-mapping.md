---
atom_id: CA-E-368
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - static-mapping
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
---
# Externalize a large static mapping

## Claim checked

One large reusable static mapping is stored outside a hand-authored Python
module while its loader retains a typed, validated boundary.

## Test case

Evaluate one changed Python module whose physical size is dominated by a large
literal mapping rather than executable behavior.

## Acceptance criteria

Pass only when the mapping is moved to a declared asset carrier and its loader
validates the expected structure without changing the mapping's meaning.

## Failure disposition

Reject the source-size claim until data and executable behavior are separated.
