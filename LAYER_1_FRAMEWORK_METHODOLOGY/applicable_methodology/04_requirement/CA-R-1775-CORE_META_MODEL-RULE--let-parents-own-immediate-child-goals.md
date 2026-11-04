---
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
atom_id: CA-R-1775
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1775-CORE_META_MODEL-RULE--let-parents-own-immediate-child-goals.md
  source_atom_id: CA-R-1775
  source_atom_revision: 33
  source_sha256: ed3b04fb0f3d909b74541ca5c3c9a8ed70105d85eef704fcc4b3058589e16f9d
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Let Parents Own Immediate Child Goals

## Claim

### Prose Claim


parent Scope Units and their immediate child Scope Units.


**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
