---
atom_id: CA-R-2327
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Cardinality
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2327-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality.md
  source_atom_id: CA-R-2327
  source_atom_revision: 5
  source_sha256: 176a534e4da9b13617e42b90f6742f80d5804b9c14617a15c49613cb1b749a51
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Cardinality

## Claim

Cardinality is CFEL syntax for expressing the allowed number of direct values,
dependent Properties, Relation instances or contained parts.


```CFEL
CFEL <+ Cardinality
```

The forms are `{:n}`, `{:n+}` and `{:n..m}` with non-negative integer bounds.

## Details

Source meaning: CA-R-1248@23 and CA-R-2244@1. Scope-specific constraints
remain in their governing Declarations.
