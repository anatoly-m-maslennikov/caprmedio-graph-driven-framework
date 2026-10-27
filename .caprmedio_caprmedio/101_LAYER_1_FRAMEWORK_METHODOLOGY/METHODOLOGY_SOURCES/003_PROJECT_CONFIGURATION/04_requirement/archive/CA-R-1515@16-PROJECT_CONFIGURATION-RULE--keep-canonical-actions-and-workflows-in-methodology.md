---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Methodology/Tool Operation Definition Reference
  - Subject/Domain/Node/Continuant/Scope Unit//CORE_META_MODEL
  - Subject/Domain/Node/Continuant/Selection//Extension Sources
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Engineering/Workflow Orchestration/Action Realization
version: 16
updated_at: 2026-10-25 00:22:12 +0400
relations:
  relates_to:
  - CA-M-002
  - CA-R-1530
  - CA-R-1222
atom_id: CA-R-1515@16
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
