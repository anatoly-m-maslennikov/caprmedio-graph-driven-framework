---
subjects:
  governs: Lineage Impact Analysis
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Atom Change Classification
  - Subject/Engineering/Carrier
  - Verification
version: 28
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1632
  - CA-R-1687
atom_id: CA-R-1633@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Record one Lineage Impact Analysis per changed atom revision

## Scope

`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.

## Claim

**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.

## Details
