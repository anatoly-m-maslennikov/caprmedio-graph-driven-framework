---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Extension Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 20
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
atom_id: CA-R-1515
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
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
