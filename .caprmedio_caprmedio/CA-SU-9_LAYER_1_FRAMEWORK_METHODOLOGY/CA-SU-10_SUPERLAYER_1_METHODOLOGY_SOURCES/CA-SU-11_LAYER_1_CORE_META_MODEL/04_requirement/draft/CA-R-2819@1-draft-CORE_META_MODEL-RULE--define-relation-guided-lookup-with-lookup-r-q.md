---
atom_id: CA-R-2819
ref_id: CA-R-2819@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
version: 1
updated_at: 2026-11-05 14:25:52 +0400
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2819@1-draft-RULE--define-relation-guided-lookup-with-lookup-r-q.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define Relation-guided lookup with `LOOKUP(R, q)`

## Claim

### Prose Claim

In an admitted fallback expression, `LOOKUP(R, q)` starts at the bearer of the target Property `p` and follows one existing outgoing link of declared Relation `R` at each step, in R’s declared direction. It excludes the starting bearer and returns the nearest authored value of `q` that is applicable to that bearer. Resolve `q` by full Property declaration identity and effective MODEL applicability; skip only an inapplicable Property or an absent authored occurrence. At a known end with no applicable authored value, return absence. Do not match by bare name or invent a Property slot.

A present invalid value, unresolved applicability or graph fact, multiple outgoing targets, or revisiting a bearer is an error. Follow only the Relation direction named by `R`.
