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
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
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

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
