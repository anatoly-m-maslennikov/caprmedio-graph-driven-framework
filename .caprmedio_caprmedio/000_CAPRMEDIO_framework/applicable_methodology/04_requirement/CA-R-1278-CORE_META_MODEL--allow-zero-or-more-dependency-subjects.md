---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1278
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1278-CORE_META_MODEL--allow-zero-or-more-dependency-subjects.md
  source_atom_id: CA-R-1278
  source_atom_revision: 23
  source_sha256: 63b0a7e3f07c207566ec25b7159546f89a869ebb685292b6bab6b2fe0c650a46
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Allow Zero or More Dependency Subjects

## Claim

### Prose Claim


direct DEPENDS_ON targets in an Atom's Subjects Property.


**every** Atom **may** declare **`>=0`** distinct direct DEPENDS_ON targets **in** its Subjects Property.
