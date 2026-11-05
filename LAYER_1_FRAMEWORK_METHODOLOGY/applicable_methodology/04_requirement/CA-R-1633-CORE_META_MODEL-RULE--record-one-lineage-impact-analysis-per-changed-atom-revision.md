---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
version: 43
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1633
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1633-CORE_META_MODEL-RULE--record-one-lineage-impact-analysis-per-changed-atom-revision.md
  source_atom_id: CA-R-1633
  source_atom_revision: 43
  source_sha256: e463523fd78e7b839676e9f96bc81e1d8f96f0e016be2de90469fd963ecdbd2a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Record one Lineage Impact Analysis per changed atom revision

## Claim

### Prose Claim


`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.


**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis & Advisory Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.
