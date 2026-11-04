---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Component Structure
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1515-PROJECT_CONFIGURATION-RULE--keep-canonical-actions-and-workflows-in-methodology.md
  source_atom_id: CA-R-1515
  source_atom_revision: 25
  source_sha256: c4d3c7e9b810ba755e3fd5fd54f2ca4c6f3d856fe6dd24bc7745ebe699065707
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
