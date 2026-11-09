---
atom_id: CA-R-1515
ref_id: CA-R-1515
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure"
tier: 2
status: Active
version: 25
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1515-PROJECT_CONFIGURATION-RULE--keep-canonical-actions-and-workflows-in-methodology.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Keep canonical Actions and Workflows in methodology

## Claim

### Prose Claim


the canonical O definitions of Actions and Workflows used by TOOLS in the caprmedio Project.


**in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

## Details

- a Tool references the applicable canonical definition rather than independently defining the same Action **or** Workflow **in** its own Scope Unit.
- the owning methodology source **may** be Core Meta-Model, an admitted Extension, **or** Project Configuration according **to** the definition's actual applicability; this allocation rule does **not** make project-specific behavior universal Core authority.
- Implementation code **and** prompts **may** realize the definition **without** becoming another independently maintained operational definition.
