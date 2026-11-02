---
atom_id: CA-C-629
role: Concern
form: Question
status: Active
version: 1
updated_at: 2026-11-02 07:52:54 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
priority: medium
subjects:
  active: CFEL
relations: {}
---

## Summary

How should CFEL test and set cardinalities?

## Question

How should a CFEL condition test an actual cardinality, and how should a conditional conclusion require a cardinality, under the latest `{:n}` allowed-cardinality notation and the `=` condition and `==` set-value distinction?

## Details

The selected working choice preserves the existing `{=n}` and `{==n}` expressions as unresolved source evidence until their equivalent syntax is explicitly established. It does not substitute `{:n}`: an allowed bound, a test, and a conditional conclusion have different jobs. The affected Declarations and source pins are recorded in the notation compatibility inventory. This Question does not pause unrelated work; an affected expression must not be declared successfully migrated without an equivalent.

One option is to define a reusable count expression that can be compared with `=` or set with `==`. Another is to define a precise contextual interpretation of the allowed-cardinality form in IF conditions and conclusions. Either option needs to preserve actual count tests, conditional requirements, and independent endpoint ownership.
