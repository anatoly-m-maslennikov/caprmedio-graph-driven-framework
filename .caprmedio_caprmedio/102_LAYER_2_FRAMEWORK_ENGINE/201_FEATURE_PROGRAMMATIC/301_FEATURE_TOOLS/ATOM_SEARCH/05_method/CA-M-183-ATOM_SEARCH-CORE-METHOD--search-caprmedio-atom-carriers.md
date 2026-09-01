---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-863
  derived_from:
    - CA-A-058
---
# Search CAPRMEDIO Atom carriers

## Applicable when

Use this Method when an operator or another Tool needs to locate Atom carriers without changing project authority.

## Procedure

1. Resolve the configured CAPRMEDIO control root and the requested lifecycle, subtree, exact-selector, and field filters.
2. Enumerate only Atom carriers inside the selected boundary; exclude runtime state, projections, and non-Atom files.
3. Parse only the filename, frontmatter, and body fields needed by the requested output mode.
4. Apply all supplied filters conjunctively and preserve a diagnostic for every malformed or unreadable candidate.
5. Return matches in stable path order with their stable identifiers and the requested metadata, content, or both.
6. Perform no write, rename, move, lifecycle transition, or projection rebuild.

## Outcome

A reproducible read-only result set identifies every matching Atom carrier within an explicit search frontier.

## Failure or stop

Stop without mutation when the control root or selector grammar is invalid. Report malformed carriers separately from valid non-matches.
