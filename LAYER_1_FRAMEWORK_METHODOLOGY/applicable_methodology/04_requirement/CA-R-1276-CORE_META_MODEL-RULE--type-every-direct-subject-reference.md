---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1276
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1276-CORE_META_MODEL-RULE--type-every-direct-subject-reference.md
  source_atom_id: CA-R-1276
  source_atom_revision: 25
  source_sha256: 6cbd35b10bd29acc99fdab0364b9c63503089c33fb018d1819eb4a5cc50a6a65
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Type Every Direct Subject Reference

## Claim

### Prose Claim


direct references in an Atom's Subjects Property.


**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.
