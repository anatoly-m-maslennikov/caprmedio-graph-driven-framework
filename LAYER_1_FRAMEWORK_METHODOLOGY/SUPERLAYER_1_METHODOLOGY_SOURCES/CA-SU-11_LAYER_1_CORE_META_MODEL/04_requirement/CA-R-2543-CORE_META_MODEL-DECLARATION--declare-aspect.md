---
atom_id: CA-R-2543
ref_id: CA-R-2543
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Aspect
tier: 3
status: Active
version: 4
updated_at: 2026-11-02 18:21:51 +0400
carrier_destination:
  file:
    name: CA-R-2543-CORE_META_MODEL-DECLARATION--declare-aspect.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Aspect

## Claim

### Prose Claim



- MODEL declares the generic Aspect.
- All concrete Aspects are instances in the applicable PROJECT STRUCTURE tree.

### Formal Claim

```CFEL
# model
Aspect;

Aspect ((NARROWER_THAN)) Node
```

## Semantics

An Aspect is a topic through which an Atom addresses its Subject.
