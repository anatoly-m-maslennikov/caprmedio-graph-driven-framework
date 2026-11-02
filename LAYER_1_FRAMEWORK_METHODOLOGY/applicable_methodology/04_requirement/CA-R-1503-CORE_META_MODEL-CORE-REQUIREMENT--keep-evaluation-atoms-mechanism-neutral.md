---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  depends_on:
    ["Entity/Node/Continuant/Atom.Substance", "Implementation"]
version: 7
updated_at: "2026-10-19 15:53:16 +0400"
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
  source_atom_revision: 7
  source_sha256: 95e93a7a0de479ddce6e5c47cebe8ca981db1d7884df5a3351d334c527a9b6a2
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
