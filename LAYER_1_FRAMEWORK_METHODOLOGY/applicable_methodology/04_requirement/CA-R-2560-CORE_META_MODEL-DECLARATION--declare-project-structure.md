---
atom_id: CA-R-2560
ref_id: CA-R-2560
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ PROJECT STRUCTURE
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md
  source_atom_id: CA-R-2560
  source_atom_revision: 2
  source_sha256: c7f4f44c715d92772a1e7e8a651c571eae7e826c17a64d4a5f676a1c7ba12360
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
