---
subjects:
  governs: "Lineage Impact Analysis"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Atom Change Classification", "Carrier-Only Recoding", "Verification"]
version: 24
updated_at: "2026-10-19 11:41:48 +0000"
relations:
  relates_to:
    - CA-R-1632
    - CA-R-1687
atom_id: "CA-R-1633@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Record one Lineage Impact Analysis per changed atom revision

## Scope

`semantic_revision`, `replacement`, `carrier_only`, and equivalent `refinement` changes of admitted Atoms.

## Claim

**every** `semantic_revision` **or** `replacement` of an admitted Atom **must** retain **`=1`** identifiable Lineage Impact Analysis whose primary conclusion is the impact state of that exact changed parent Revision. The assessment **may** be part of an existing completed shared review package; a separate Analysis Atom for each changed Atom is not required. A `carrier_only` **or** equivalent `refinement` change **must** require lossless-recoding **or** equivalence Verification instead.

## Details
