---
atom_id: CA-R-2995
ref_id: CA-R-2995@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Construct Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL/Construct//Declaration Expression Call
tier: 3
status: Draft
version: 1
updated_at: "2026-11-06 19:30:28 +0400"
carrier_destination:
  file:
    name: CA-R-2995@1-draft-CORE_META_MODEL-CONSTRUCT_DECLARATION--declare-declaration-qualified-expression-calls.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare declaration-qualified expression calls

## Claim

### Prose Claim

`<Kind>.p(a)` evaluates the expression for Property path `p` authored in the Declaration of `Kind`, using the bound participant `a`.

- `p` is relative to `Kind`.
- `a` satisfies the selected Kind and its qualifications.
- The call selects the expression authored in that Declaration, including when a narrower Declaration supplies another calculation for the same Property.
- The expression reads Property values from the same `a`.
- A missing or ambiguous expression is an error.

The call evaluates a value. It creates no instance or stored fact.
