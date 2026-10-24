---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Authority Modes"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings", "Entity/Node/Continuant/Project.Structure", "Authority Mode", "Entity/Node/Continuant/Project", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom"]
version: 11
updated_at: "2026-10-19 15:53:03 +0400"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-M-279"
atom_id: CA-R-1430@11
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Select Authority Modes through Framework Instance Settings

## Scope

the selection **and** overrides of Authority Modes through Framework Instance Settings.

## Claim

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.

## Details
