---
atom_id: CA-R-2816
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 1
updated_at: 2026-11-05 16:33:24 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2816@1-draft-CORE_META_MODEL-RULE--define-property-value-selection-with.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define Property-value selection with `:=`

## Claim

### Prose Claim

In a Subject or filtered Node expression in a Formal Claim, `:=` combines allowed-value qualification with selection, as in `Workflow//(.Purpose := Runtime)`. The selected value must satisfy effective admissibility: the OR of applicable HAS_ALLOWED_VALUE alternatives, including inherited alternatives, when present, and the AND of applicable HAS_VALUE_CONSTRAINT restrictions, including inherited restrictions. If no HAS_ALLOWED_VALUE group exists, omit that group (true), so no enumeration restriction is imposed. It is selection syntax, not assignment to an occurrence.
