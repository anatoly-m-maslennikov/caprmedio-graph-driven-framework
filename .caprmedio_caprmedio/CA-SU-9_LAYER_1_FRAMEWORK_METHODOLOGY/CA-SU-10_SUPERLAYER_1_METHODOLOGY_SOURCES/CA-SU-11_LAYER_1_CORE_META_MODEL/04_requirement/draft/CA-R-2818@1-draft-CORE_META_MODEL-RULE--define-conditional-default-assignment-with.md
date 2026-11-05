---
atom_id: CA-R-2818
ref_id: CA-R-2818@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 14:25:52 +0400
carrier_destination:
  file:
    name: CA-R-2818@1-draft-RULE--define-conditional-default-assignment-with.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define conditional default assignment with `?==`

## Claim

### Prose Claim

Write conditional default assignment as `p ?== e`. It keeps an authored value of `p`; when `p` is absent, it sets the first available valid value in the Model under the ordered fallback rule. A present invalid value is not absence. This syntax does not itself write a Carrier; persistence belongs to an adapter or Delivery rule.
