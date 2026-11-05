---
atom_id: CA-R-1869
ref_id: CA-R-1869
role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-11-02 19:44:26 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
form: Rule
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-R-1869-TOOLS-RULE--reject-event-selectors-outside-the-canonical-namespace.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
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
