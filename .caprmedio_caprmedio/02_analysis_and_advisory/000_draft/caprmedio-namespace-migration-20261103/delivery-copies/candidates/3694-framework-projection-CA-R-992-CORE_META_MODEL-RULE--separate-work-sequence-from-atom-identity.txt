---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
version: 36
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2520
atom_id: CA-R-992
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-992-CORE_META_MODEL-RULE--separate-work-sequence-from-atom-identity.md
  source_atom_id: CA-R-992
  source_atom_revision: 36
  source_sha256: 06b9cb409f0ef5b935b268d103137c8b32c4d2b7c67a4cfc7d139dd3a520b7b1
  original_relations_sha256: da1339ac6ab40f2e5666258f225098cfaceb0373e40d73382c0b51ba6b2c42b4
---
## Summary

Separate Work Sequence from Atom identity

## Claim scope

Work Sequence Numbers **and** Atom identity-related properties.

## Claim

a Work Sequence Number **must not** establish **or** change Atom identity, Atom Scope, Claim Target Scope Unit, Type, authoring Subtype, decomposition, **or** blocking.
