---
atom_id: CA-R-2770
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Lookup
version: 2
updated_at: 2026-11-04 20:33:16 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2770-CORE_META_MODEL-DECLARATION--declare-cfel-operator-lookup-r-q.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare CFEL operator LOOKUP(R, q)

## Claim

### Formal Claim

```CFEL
# model
Operator//Lookup == "LOOKUP(R, q)"
```

### Prose Claim

`LOOKUP(R, q)` is an existing contextual value expression admitted in a `?==` fallback expression. Starting at the bearer of target Property `p`, follow one existing outgoing link of declared Relation `R` at each step, in R's declared direction. Exclude the starting bearer. Return the nearest authored value of `q` that is applicable to that bearer. Resolve `q` by full Property declaration identity and effective MODEL applicability; skip only an inapplicable Property or an absent authored occurrence. At a known end with no applicable authored value, return absence. Do not match by bare name or invent a Property slot.

A present invalid value, unresolved applicability or graph fact, multiple outgoing targets, or revisiting a bearer is an error. Follow only the Relation direction named by R.

## Semantics

`Operator//Lookup` identifies the declared CFEL value-expression operator. The traversal semantics above are its complete existing contract.
