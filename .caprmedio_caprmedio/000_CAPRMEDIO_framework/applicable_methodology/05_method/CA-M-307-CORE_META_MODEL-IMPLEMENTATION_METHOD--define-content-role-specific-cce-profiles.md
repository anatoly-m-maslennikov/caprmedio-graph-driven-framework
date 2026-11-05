---
atom_id: CA-M-307
ref_id: CA-M-307
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Role
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.Form
tier: 5
relations:
  child_of:
  - CA-M-113
  - CA-M-230
  - CA-M-234
status: Active
version: 29
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-307-CORE_META_MODEL-IMPLEMENTATION_METHOD--define-content-role-specific-cce-profiles.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-307-CORE_META_MODEL-IMPLEMENTATION_METHOD--define-content-role-specific-cce-profiles.md
  source_atom_id: CA-M-307
  source_atom_revision: 29
  source_sha256: 5fe99cedfb4be1574bd2c8467d398d2e201877769b64ff1f64adc82a9ae6d0c9
  original_relations_sha256: 89010f8c6c52d1f5ef8776e8312d32466118f5ac2c9d5c6e29ec0a8f7e77874f
---
## Summary

Define Content-role-specific CCE Profiles

## Claim

### Prose Claim


CCE Role Profiles.


a CCE Role Profile **means** one restriction of shared CCE that identifies the permitted primary Claim contribution, permitted CCE Operator uses, permitted subordinate content slots, **and** prohibited primary contributions for one Content Role **or** one narrower Type **or** content slot.

the current role-specific profiles apply **only** **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations Atoms.

Concern **and** Analysis & Advisory Claims remain subject **to** shared CCE **without** an additional CCE Role Profile. this absence does **not** exempt them from shared CCE **or** authorize normative authority outside their Content Role meanings.

no CCE Role Profile is currently registered for Implementation because the current source set contains no Implementation Atoms. an absent Implementation profile **must not** be replaced by another role's profile **or** treated as role-profile conformance.

a narrower Type **or** content-slot profile **may** restrict its parent role profile **and** define permitted subordinate operator use, but it **must not** change the primary contribution of the Content Role.
