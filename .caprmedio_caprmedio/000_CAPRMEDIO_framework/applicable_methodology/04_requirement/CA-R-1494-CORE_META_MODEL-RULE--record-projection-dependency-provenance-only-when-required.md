---
atom_id: CA-R-1494
ref_id: CA-R-1494
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 2
relations:
  child_of:
  - CA-R-2535
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1494-CORE_META_MODEL-RULE--record-projection-dependency-provenance-only-when-required.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1494-CORE_META_MODEL-RULE--record-projection-dependency-provenance-only-when-required.md
  source_atom_id: CA-R-1494
  source_atom_revision: 21
  source_sha256: d2ac0cf8bf7b6d40d7e4205e12f882480a59f3e4d1f5eb21c1899360c816cbae
  original_relations_sha256: 77e092f31d4648fd7fe12a07553e000c54159e28bd9f3120ed798159b040e50c
---
## Summary
Record Projection dependency provenance **only** **when** required

## Claim

### Prose Claim

Projections.

a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by `CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.
