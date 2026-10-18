---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Evaluation"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Implementation"]
version: 6
updated_at: "2026-10-15 18:43:45 +0000"
relations: {}
atom_id: "CA-R-1503"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1503-CORE_META_MODEL-CORE-REQUIREMENT--keep-evaluation-atoms-mechanism-neutral.md
  source_atom_id: CA-R-1503
  source_atom_revision: 6
  source_sha256: fdb0d8c27e44915053a5d2dbe1eded1a0b53215963b38609d0d887551720658f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Evaluation Atoms mechanism-neutral

## Scope

Evaluation Atom check definitions and their implementation mechanisms.

## Claim

an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

## Details

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
