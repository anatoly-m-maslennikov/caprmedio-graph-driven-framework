---
atom_id: CA-R-2560
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ PROJECT STRUCTURE
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md
  source_atom_id: CA-R-2560
  source_atom_revision: 2
  source_sha256: 72ab8bd178893f921a9abab525507c525812acaca39a6782cd1b9417b344ebd7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare PROJECT STRUCTURE

## Claim

```CFEL
PROJECT STRUCTURE {:0}((IS_PROPERTY_OF));
PROJECT STRUCTURE >| (Container == yes);
PROJECT STRUCTURE ((NARROWER_THAN)) @Node
```

## Semantics

PROJECT STRUCTURE describes the actual structure of a Project, including its Scope Units, Aspects, and other declared components.
