---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ CFEL
  - CAPRMEDIO_MODEL <+ Term//Property
version: 29
updated_at: 2026-11-05 14:25:52 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1245
status: Draft
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1245@29-draft-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Qualify Allowed Values with Colon

## Claim

### Prose Claim


allowed-value qualification in a Subject Expression.


**in** a Subject Expression, `X::Y` **must** admit Y as one possible value of X in X's qualified context, irrespective of X's kind or path. This qualification is CFEL syntax, not a graph Relation. It does not assign Y to an occurrence or determine direct-value cardinality.
