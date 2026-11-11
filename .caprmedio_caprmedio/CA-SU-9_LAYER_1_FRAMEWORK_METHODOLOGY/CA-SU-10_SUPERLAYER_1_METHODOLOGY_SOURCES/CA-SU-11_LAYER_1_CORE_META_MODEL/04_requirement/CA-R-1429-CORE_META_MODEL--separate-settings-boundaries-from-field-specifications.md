---
atom_id: CA-R-1429
ref_id: CA-R-1429
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Active
version: 28
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1429-CORE_META_MODEL-RULE--separate-settings-boundaries-from-field-specifications.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Separate settings boundaries from field specifications

## Claim

### Prose Claim


the authority boundary between settings foundations, shared settings specifications, **and** concrete specifications.


- the settings foundations for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
- an independently governable shared settings specification **must** preserve those foundations **without** selecting a concrete representation;
- **every** concrete section, field, **or** Carrier syntax specification **must** be specified explicitly.

a setting **must not** require a shared settings specification **unless** a distinct shared specification requires independent authority.
