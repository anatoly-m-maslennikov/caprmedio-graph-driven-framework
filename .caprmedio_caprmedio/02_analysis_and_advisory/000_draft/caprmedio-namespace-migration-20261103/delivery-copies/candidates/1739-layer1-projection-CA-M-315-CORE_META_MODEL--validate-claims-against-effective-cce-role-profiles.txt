---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Validation
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Type
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-307
  - CA-M-308
atom_id: CA-M-315
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-315-CORE_META_MODEL--validate-claims-against-effective-cce-role-profiles.md
  source_atom_id: CA-M-315
  source_atom_revision: 26
  source_sha256: 949a1284ae479cc2c94810b982698a0ce99570fca2c2fd6d268b0869c36395c7
  original_relations_sha256: cce5365b461cbd3dbc2378bf4574c500418c6d2157ddda95835141a2896efdef
---
## Summary

Validate Claims against Effective CCE Role Profiles

## Claim scope

Atom Claims against effective CCE Role Profiles.

## Claim

**to** validate one Atom Claim against its effective CCE Role Profile, the Validator **must** perform **all** of:

1. resolve the effective profile under CA-M-308 **without** inferring a different Content Role from the wording under review.
2. identify the Claim's primary contribution, every subordinate content slot, **and** every registered CCE Operator occurrence.
3. verify that the primary contribution matches the resolved role profile **and** that every narrower Type **or** content-slot contribution remains within its admitted boundary.
4. verify that every CCE Operator use is permitted for its exact primary **or** subordinate context **and** has explicit logical scope.
5. reject a primary contribution owned by another Content Role even **when** every individual CCE Operator is present **in** the global registry.
6. for Concern **or** Analysis & Advisory, validate shared CCE **and** their governed Content Role meaning **without** requiring a role-specific profile.
7. for Implementation content, report that no CCE Role Profile is registered; do **not** apply another role's profile **or** report role-profile conformance.
8. report every mismatch by Content Role, Type, content slot, primary contribution, **and** Operator occurrence. do **not** rewrite the source Claim **or** report conformance while one required classification remains unresolved.

## Details

global CCE Operator registration is necessary but insufficient for role-profile conformance.
