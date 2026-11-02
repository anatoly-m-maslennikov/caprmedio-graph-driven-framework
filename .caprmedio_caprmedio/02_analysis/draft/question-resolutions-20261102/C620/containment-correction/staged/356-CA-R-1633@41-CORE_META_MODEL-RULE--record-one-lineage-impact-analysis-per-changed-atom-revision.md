---
subjects:
  active: Atom
  passive:
  - Atom
  - Carrier
  - Entity/Aspect/Engineering/Traceability
version: 41
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
atom_id: CA-R-1633@41
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary

Record one Lineage Impact Analysis per changed atom revision

## Claim scope

`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.

## Claim

**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis & Advisory Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.
