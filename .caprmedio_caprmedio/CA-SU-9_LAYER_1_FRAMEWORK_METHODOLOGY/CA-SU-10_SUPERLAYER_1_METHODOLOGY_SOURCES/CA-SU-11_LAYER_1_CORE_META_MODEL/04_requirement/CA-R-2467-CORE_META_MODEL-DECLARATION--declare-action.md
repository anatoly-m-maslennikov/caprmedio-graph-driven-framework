---
atom_id: CA-R-2467
ref_id: CA-R-2467
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
tier: 3
status: Active
version: 4
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Action

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Action;

Action ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations));

# instances
Action//$action{::0+}((IS_RUN_BY)) (in (Step, Substep))//$selected
```

## Semantics

An Action is a reusable operational building block. Its boundary reflects one modeled responsibility.
