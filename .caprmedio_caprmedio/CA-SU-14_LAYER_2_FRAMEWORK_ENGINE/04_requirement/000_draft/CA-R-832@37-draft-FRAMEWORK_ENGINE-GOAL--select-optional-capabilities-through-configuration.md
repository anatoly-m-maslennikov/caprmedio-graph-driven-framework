---
atom_id: CA-R-832
ref_id: CA-R-832@37-draft
container:
  scope_unit: CA-SU-14
role: Requirement
form: Goal
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 5
relations:
  child_of:
  - CA-R-3033
  - CA-R-815
  - CA-M-006
status: Draft
version: 37
carrier_destination:
  file:
    name: CA-R-832@37-draft-FRAMEWORK_ENGINE-GOAL--select-optional-capabilities-through-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/000_draft
updated_at: "2026-11-11 18:12:55 +0400"
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
---
## Summary
Select optional capabilities through Configuration

## Claim

### Prose Claim


the CAPRMEDIO Framework Instance **must** provide configuration capabilities **to** select, combine, parameterize, **or** disable available optional canonical **and** Extension capabilities **only** within declared configuration boundaries **and** **without** redefining governed meanings.

current Extension activation **and** selected Extension revisions use their authoritative Framework Instance Settings under CA-R-1207; this capability does **not** make Project Configuration Atoms a second owner of those selections.
