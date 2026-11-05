---
atom_id: CA-R-2560
ref_id: CA-R-2560
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ PROJECT STRUCTURE
version: 2
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare PROJECT STRUCTURE

## Claim

### Formal Claim

```CFEL
# model
PROJECT STRUCTURE {::0}((IS_PROPERTY_OF));

PROJECT STRUCTURE >| (Container == yes);

PROJECT STRUCTURE ((NARROWER_THAN)) Node
```

## Semantics

PROJECT STRUCTURE describes the actual structure of a Project, including its Scope Units, Aspects, and other declared components.
