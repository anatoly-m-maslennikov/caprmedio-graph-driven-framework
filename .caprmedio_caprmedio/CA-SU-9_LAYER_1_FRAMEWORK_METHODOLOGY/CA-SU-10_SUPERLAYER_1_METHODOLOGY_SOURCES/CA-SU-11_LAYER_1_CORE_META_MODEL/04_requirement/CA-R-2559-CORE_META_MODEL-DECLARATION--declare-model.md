---
atom_id: CA-R-2559
ref_id: CA-R-2559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2559-CORE_META_MODEL-DECLARATION--declare-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare MODEL

## Claim

### Formal Claim

```CFEL
# model
MODEL {::0}((IS_PROPERTY_OF));

MODEL >| (Container == yes);

MODEL ((NARROWER_THAN)) Node
```

### Prose Claim



- A local MODEL inherits CAPRMEDIO's MODEL.
- MODEL inheritance is distinct from Node narrowing.
- Local overrides replace matching inherited rules in the local MODEL.
- Local overrides preserve the base MODEL's rules.
- Unmodified inherited Declarations are reused.

## Semantics

MODEL declares Node kinds, Relations, Properties, and rules.
