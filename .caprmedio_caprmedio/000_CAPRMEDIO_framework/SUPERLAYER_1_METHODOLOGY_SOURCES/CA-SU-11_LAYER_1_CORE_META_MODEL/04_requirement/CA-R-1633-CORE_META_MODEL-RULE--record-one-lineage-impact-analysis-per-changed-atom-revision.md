---
atom_id: CA-R-1633
ref_id: CA-R-1633
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
tier: 2
status: Active
version: 43
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1633-CORE_META_MODEL-RULE--record-one-lineage-impact-analysis-per-changed-atom-revision.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Record one Lineage Impact Analysis per changed atom revision

## Claim

### Prose Claim


`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.


**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis & Advisory Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.
