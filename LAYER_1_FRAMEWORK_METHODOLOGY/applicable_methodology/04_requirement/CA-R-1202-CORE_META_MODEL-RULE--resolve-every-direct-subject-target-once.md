---
subjects:
  active: Atom.Subjects
  passive:
  - CFEL > Relation//GOVERNS
  - CFEL > Relation//DEPENDS_ON
  - Atom.Subjects
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1202
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1202-CORE_META_MODEL-RULE--resolve-every-direct-subject-target-once.md
  source_atom_id: CA-R-1202
  source_atom_revision: 30
  source_sha256: 5333156ba3b0f1cef06a78eaed860977f2b9bc689756d3db13f6ac73b71c7602
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Resolve Every Direct Subject Target Once

## Claim scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
