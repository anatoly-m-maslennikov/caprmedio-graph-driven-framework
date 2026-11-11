---
subjects:
  active: Atom/(.Role := Operations)
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Scope Unit
  - Atom/(.Role := Operations)
  - Scope Unit//CORE_META_MODEL
  - Entity/Object/Continuant/Selection//Extension Sources
  - Scope Unit//PROJECT_CONFIGURATION
  - Aspects <+ Engineering <+ Architecture <+ Component Structure
version: 25
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1515
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep canonical Actions and Workflows in methodology

## Claim scope

the canonical O definitions of Actions and Workflows used by TOOLS in the caprmedio Project.

## Claim

**in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

## Details

- a Tool references the applicable canonical definition rather than independently defining the same Action **or** Workflow **in** its own Scope Unit.
- the owning methodology source **may** be Core Meta-Model, an admitted Extension, **or** Project Configuration according **to** the definition's actual applicability; this allocation rule does **not** make project-specific behavior universal Core authority.
- Implementation code **and** prompts **may** realize the definition **without** becoming another independently maintained operational definition.
