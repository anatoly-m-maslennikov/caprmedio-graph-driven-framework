---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
version: 28
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-030
  - CA-R-1767
atom_id: CA-R-1672
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1672-CORE_META_MODEL-RULE--permit-terminal-implementation-methods.md
  source_atom_id: CA-R-1672
  source_atom_revision: 28
  source_sha256: 743b467880915e2097815d4e1a435171fcca64ea6ae5b371eb8b50021c45b962
  original_relations_sha256: 104250d8f1edead7d78dc4e68ca75b90678ae2012d09695ad7885fdc6aa6267f
---
## Summary

Permit terminal Implementation Methods

## Claim scope

terminal permission for an active Eng Policy after its local Eng Decisions are absorbed and archived.

## Claim

`eng_policy` **must** be registered as terminal-permitted, so an active Eng Policy Atom **may** remain childless in Atom topology **after** its local Eng Decision Atoms have been losslessly absorbed **and** archived.

## Details

This Atom-topology permission does not create a Scope Unit child or grant local Eng Policy ownership to a leaf; an actual declared child and every-child applicability remain required by CA-R-2119@8.
