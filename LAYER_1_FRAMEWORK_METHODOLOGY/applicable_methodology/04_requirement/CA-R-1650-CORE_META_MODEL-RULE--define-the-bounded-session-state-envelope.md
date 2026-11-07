---
atom_id: CA-R-1650
ref_id: CA-R-1650
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Validation
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Runtime/Session
tier: 2
status: Active
version: 34
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1650-CORE_META_MODEL-RULE--define-the-bounded-session-state-envelope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1650-CORE_META_MODEL-RULE--define-the-bounded-session-state-envelope.md
  source_atom_id: CA-R-1650
  source_atom_revision: 34
  source_sha256: 2204c803ec76a4e35d2299acd72ec1d0c37881ad9bea9bb5763275514189241d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define the bounded session-state envelope

## Claim

### Prose Claim


the bounded session-state envelope.


the bounded session-state envelope **must** contain **only** routing invariants, current scope, applicable settings, compact session state, **and** references needed **to** load active authority on demand.
