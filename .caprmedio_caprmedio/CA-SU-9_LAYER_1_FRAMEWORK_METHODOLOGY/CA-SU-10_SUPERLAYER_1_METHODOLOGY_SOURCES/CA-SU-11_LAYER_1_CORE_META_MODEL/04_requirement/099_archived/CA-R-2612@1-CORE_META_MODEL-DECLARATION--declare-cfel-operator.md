---
atom_id: CA-R-2612
ref_id: CA-R-2612@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//RecursiveWildcard
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2612@1-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare CFEL operator **

## Claim

### Formal Claim

```CFEL
# model
Operator//RecursiveWildcard == "**"
```

## Semantics

Select distinct dependent Property identities recursively below p in one bearer.
A `p.**` count aggregates that selection across all descendant depths; it does
not count values or another bearer's selection.
