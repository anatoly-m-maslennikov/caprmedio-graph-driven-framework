---
atom_id: CA-R-2996
ref_id: CA-R-2996@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Construct Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL/Construct//Property Calculation
tier: 3
status: Draft
version: 1
updated_at: "2026-11-06 19:33:59 +0400"
carrier_destination:
  file:
    name: CA-R-2996@1-draft-CORE_META_MODEL-CONSTRUCT_DECLARATION--declare-property-calculation-specialization.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Property calculation specialization

## Claim

### Prose Claim

A Declaration supplies a Property calculation as `p == expression` for its selected kind.

- The calculation from the most specific applicable Declaration replaces an inherited calculation for the same Property.
- A missing local calculation leaves the inherited calculation applicable.
- An ambiguous most-specific calculation is a conflict.
- Inherited formats, cardinalities, allowed-value rules and Relation constraints remain applicable.
- Separate applicable Rule Claims still constrain the result.

Replacement selects the calculation. It does not change the receiver's identity or store a value.
