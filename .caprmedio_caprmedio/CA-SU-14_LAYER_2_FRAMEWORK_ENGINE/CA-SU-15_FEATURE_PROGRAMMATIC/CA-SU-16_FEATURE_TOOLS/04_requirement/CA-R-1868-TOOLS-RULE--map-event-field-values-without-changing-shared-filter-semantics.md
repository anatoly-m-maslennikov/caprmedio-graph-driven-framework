---
atom_id: CA-R-1868
ref_id: CA-R-1868
role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-11-02 19:44:26 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
form: Rule
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-R-1868-TOOLS-RULE--map-event-field-values-without-changing-shared-filter-semantics.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
---
# Summary

Map Event field values without changing shared filter semantics

## Scope

The Journal-specific selector value extraction.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** pass each selected canonical Event field's exact value state to CA-R-1850 without coercion, normalization, or inferred filename value.

## Details

The Tool marks absent selectors as absent and explicit null as null. Arrays and
objects are passed as parsed RFC8259 structural values, including nested fields
resolved by RFC6901 pointers, without stringification or flattening. It delegates
all comparison and invalid-literal decisions to CA-R-1850.
