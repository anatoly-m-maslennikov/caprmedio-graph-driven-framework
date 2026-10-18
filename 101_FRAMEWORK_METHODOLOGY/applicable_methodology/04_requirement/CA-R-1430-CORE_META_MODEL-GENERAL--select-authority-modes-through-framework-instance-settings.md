---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings.Authority Modes"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Entity/Continuant/Object/Project.Structure", "Authority Mode", "Entity/Continuant/Object/Project", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom"]
version: 10
updated_at: "2026-10-15 18:42:54 +0000"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-M-279"
atom_id: "CA-R-1430"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1430-CORE_META_MODEL-GENERAL--select-authority-modes-through-framework-instance-settings.md
  source_atom_id: CA-R-1430
  source_atom_revision: 10
  source_sha256: 0c4bddac50aeadb374f61ab797d49fb49b9276a028809025e76e322428ce236e
  original_relations_sha256: be5cc3030b7779b3445d3df040c85d6952a487441c36cfe1927e563974c04f18
---
# Summary

Select Authority Modes through Framework Instance Settings

## Scope

the selection **and** overrides of Authority Modes through Framework Instance Settings.

## Claim

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.

## Details
