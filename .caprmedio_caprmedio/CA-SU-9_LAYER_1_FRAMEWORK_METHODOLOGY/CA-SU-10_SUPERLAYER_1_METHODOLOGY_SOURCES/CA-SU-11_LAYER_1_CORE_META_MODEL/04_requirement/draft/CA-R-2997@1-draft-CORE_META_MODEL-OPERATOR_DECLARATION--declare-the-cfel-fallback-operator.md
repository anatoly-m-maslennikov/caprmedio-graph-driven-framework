---
atom_id: CA-R-2997
ref_id: CA-R-2997@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Operator Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL/Operator//Fallback
tier: 3
status: Draft
version: 1
updated_at: "2026-11-06 20:09:50 +0400"
carrier_destination:
  file:
    name: CA-R-2997@1-draft-CORE_META_MODEL-OPERATOR_DECLARATION--declare-the-cfel-fallback-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare the CFEL fallback operator

## Claim

### Prose Claim

`x ?== y` returns `y` when `x` is empty; otherwise it returns `x`. Empty means `null`, an empty string, or an undefined value. An omitted value is undefined. Zero, false, whitespace and empty collections are not empty under this operator.

Evaluate a chain from left to right by applying the same binary rule. Evaluate `y` only when `x` is empty. If every operand is empty, the chain returns its final operand. The operator assigns neither operand and does not write the Model or a Carrier.
