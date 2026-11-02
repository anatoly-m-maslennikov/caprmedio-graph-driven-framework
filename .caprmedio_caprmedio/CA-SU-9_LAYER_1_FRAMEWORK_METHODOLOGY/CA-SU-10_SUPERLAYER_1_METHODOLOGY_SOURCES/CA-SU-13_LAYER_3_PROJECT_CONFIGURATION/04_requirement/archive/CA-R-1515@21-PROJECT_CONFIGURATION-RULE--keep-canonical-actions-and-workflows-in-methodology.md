---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - Entity/Object/Continuant/Structural Unit/Scope Unit//CORE_META_MODEL
  - Entity/Object/Continuant/Selection//Extension Sources
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
  - Entity/Aspect/Engineering/Architecture/Component Structure
version: 21
updated_at: 2026-10-29 07:17:26 +0400
relations: {}
atom_id: CA-R-1515@21
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 2
---
# Summary

Keep canonical Actions and Workflows in methodology

## Scope

the canonical O definitions of Actions and Workflows used by TOOLS in the caprmedio Project.

## Claim

**in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

## Details

- a Tool references the applicable canonical definition rather than independently defining the same Action **or** Workflow **in** its own Scope Unit.
- the owning methodology source **may** be Core Meta-Model, an admitted Extension, **or** Project Configuration according **to** the definition's actual applicability; this allocation rule does **not** make project-specific behavior universal Core authority.
- Implementation code **and** prompts **may** realize the definition **without** becoming another independently maintained operational definition.
