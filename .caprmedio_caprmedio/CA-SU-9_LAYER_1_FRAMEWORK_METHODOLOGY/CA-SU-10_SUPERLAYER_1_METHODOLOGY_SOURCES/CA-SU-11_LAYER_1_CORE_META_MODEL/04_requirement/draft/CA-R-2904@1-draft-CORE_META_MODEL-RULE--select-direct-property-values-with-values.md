---
atom_id: CA-R-2904
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 1
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-05 17:25:05 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2904@1-draft-CORE_META_MODEL-RULE--select-direct-property-values-with-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Select direct Property values with VALUES

## Claim

### Prose Claim

`VALUES(p)` selects the actual direct value occurrences of the selected Property expression `p`. Equal values remain distinct occurrences. It does not recursively walk dependent Properties or read value constraints as actual values. A known absent optional Property contributes an empty selection; unresolved or malformed bearer, Property population or value is an error, not an empty selection. Existing applicable cardinality and Format rules continue to apply.
