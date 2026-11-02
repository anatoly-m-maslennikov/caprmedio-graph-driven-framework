---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom
version: 22
updated_at: 2026-10-29 07:17:16 +0400
relations:
  child_of:
  - CA-R-1402
atom_id: CA-R-1430@22
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Select Authority Modes through Framework Instance Settings

## Scope

the selection **and** overrides of Authority Modes through Framework Instance Settings.

## Claim

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.

## Details
