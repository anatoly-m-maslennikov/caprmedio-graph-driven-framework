---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  passive:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  - Project
  - Scope Unit
  - Atom
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1402@27
atom_id: CA-R-1430@25
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary

Select Authority Modes through Framework Instance Settings

## Claim scope

the selection **and** overrides of Authority Modes through Framework Instance Settings.

## Claim

Framework Instance Settings **must** select the Project Authority Mode **and** default Scope Unit Authority Mode. a Scope Unit's explicit Authority Mode override **must** be owned **only** by its Project Structure declaration; an omitted override uses the effective Framework Instance setting **without** becoming an authored per-unit value. permitted values are `strict` **and** `casual`; neither changes the authority of active Atoms.
