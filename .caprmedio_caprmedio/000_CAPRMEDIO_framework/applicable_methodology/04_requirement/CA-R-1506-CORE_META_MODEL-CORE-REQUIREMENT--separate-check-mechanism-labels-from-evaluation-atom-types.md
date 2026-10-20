---
subjects:
  governs: "Atom/Content Role: Evaluation/Type"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Evaluation", "Implementation", "Type"]
version: 7
updated_at: "2026-10-19 15:53:17 +0400"
relations: {}
atom_id: "CA-R-1506"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1506-CORE_META_MODEL-CORE-REQUIREMENT--separate-check-mechanism-labels-from-evaluation-atom-types.md
  source_atom_id: CA-R-1506
  source_atom_revision: 7
  source_sha256: 511c3eac64c77b7053918a2ee767a90fc4a5ae990e925a799729b6f4a11b798f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate check mechanism labels from Evaluation Atom Types

## Scope

mechanism labels and admitted Type values for Evaluation Atoms.

## Claim

the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/Content Role: Evaluation/Type`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.

## Details

this distinction does **not** define another Content Role **or** close the admitted Evaluation Type domain. its separately governed Type values remain subject **to** the applicable Type authority.
