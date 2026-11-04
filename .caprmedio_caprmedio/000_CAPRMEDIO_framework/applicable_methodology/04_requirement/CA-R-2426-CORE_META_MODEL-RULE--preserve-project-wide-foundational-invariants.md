---
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
atom_id: CA-R-2426
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2426-CORE_META_MODEL-RULE--preserve-project-wide-foundational-invariants.md
  source_atom_id: CA-R-2426
  source_atom_revision: 3
  source_sha256: dd6f40ab3a3e5b3fa7f4987cc93a7efd7d2332f4f319310046a39a7eb72417df
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Preserve Project-wide foundational invariants

## Claim

### Prose Claim


Project-wide foundational invariants.


CAPRMEDIO must preserve all irreducible governed invariants that apply across the entire current Project independently of Scope Unit ancestry, scope label, Content Role, Artifact form, Extension, Project Configuration or substrate. Those Project-wide foundational invariants retain their applicability throughout the Project; Project-owned Tier `0` Atoms express their foundational authority. This does not make every local or Project-owned Tier `0` Atom Project-wide, add a conflict winner based on Tier, or impose a fixed Role checklist.
