---
atom_id: CA-R-1869@8
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Engineering/Journal Event Query/Selector Admission
relations:
  relates_to:
  - CA-R-1850
  - CA-R-1862
  - CA-R-1864
  - CA-E-575
type: Rule
tier: 3
---
# Summary

Reject Event selectors outside the canonical namespace

## Scope

The Journal-specific selector admission boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** reject every selector outside the
canonical Event namespace or with invalid pointer syntax before passing the
expression to CA-R-1850.

## Details

A valid Event selector is exactly `event:/` (only for full-Event query) or
`event:/` followed by a syntactically valid RFC6901 pointer. A selector outside
that namespace, a bad pointer escape or syntax, and dot-qualified traversal are
rejected locally. A valid pointer absent from an individual Event is passed to
CA-R-1850, where its comparison is false; explicit `null` remains a value.
SQL, code, grammar, boolean precedence, literal validity, and structural
comparison remain exclusively governed by CA-R-1850; this Requirement adds no
second expression grammar.
