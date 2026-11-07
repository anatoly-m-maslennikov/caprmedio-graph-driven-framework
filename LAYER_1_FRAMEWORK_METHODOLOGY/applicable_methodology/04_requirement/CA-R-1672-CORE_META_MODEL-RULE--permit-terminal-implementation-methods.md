---
atom_id: CA-R-1672
ref_id: CA-R-1672
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
relations:
  child_of:
  - CA-R-030
  - CA-R-1767
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1672-CORE_META_MODEL-RULE--permit-terminal-implementation-methods.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1672-CORE_META_MODEL-RULE--permit-terminal-implementation-methods.md
  source_atom_id: CA-R-1672
  source_atom_revision: 28
  source_sha256: f9f6691fff8f492be961578e037c074e84b0c620487deb489b119a4ec7babee2
  original_relations_sha256: 104250d8f1edead7d78dc4e68ca75b90678ae2012d09695ad7885fdc6aa6267f
---
## Summary

Permit terminal Implementation Methods

## Claim

### Prose Claim


terminal permission for an active Eng Policy after its local Eng Decisions are absorbed and archived.


`eng_policy` **must** be registered as terminal-permitted, so an active Eng Policy Atom **may** remain childless in Atom topology **after** its local Eng Decision Atoms have been losslessly absorbed **and** archived.

## Details

This Atom-topology permission does not create a Scope Unit child or grant local Eng Policy ownership to a leaf; an actual declared child and every-child applicability remain required by CA-R-2119@8.
