---
atom_id: CA-C-624
ref_id: CA-C-624
container:
  scope_unit: CA-SU-11
role: Concern
form: Question
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Cardinality
tier: 3
status: Resolved
version: 3
updated_at: 2026-11-02 14:59:48 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
carrier_destination:
  file:
    name: CA-C-624-CORE_META_MODEL-QUESTION--should-recursive-property-counts-aggregate-descendant-identities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/021_resolved
---

## Summary

Should recursive Property counts aggregate descendant identities?

## Question

Does `p.**[name format]{:n}` count all selected descendant Properties together across every depth?

## Details

Resolved by the Operator on 2 November 2026.

- `p.**` selects all descendant Properties recursively.
- `p.*` selects immediate Properties.
- Selectors compose: `p.*.*` selects depth 2; `p.*.**` selects depth 2 and deeper.

The existing aggregate-count rule is confirmed. CA-R-2472 records selector composition.
