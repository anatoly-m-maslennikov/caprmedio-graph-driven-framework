---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
version: 21
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-2535
atom_id: CA-R-1494
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1494-CORE_META_MODEL-RULE--record-projection-dependency-provenance-only-when-required.md
  source_atom_id: CA-R-1494
  source_atom_revision: 21
  source_sha256: 8c069d6864a2bd296b3362739624197ea921dcff2a0ef8f528c1df83ba6afb19
  original_relations_sha256: 77e092f31d4648fd7fe12a07553e000c54159e28bd9f3120ed798159b040e50c
---
## Summary
Record Projection dependency provenance **only** **when** required

## Claim scope
Projections.

## Claim
a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by `CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.
