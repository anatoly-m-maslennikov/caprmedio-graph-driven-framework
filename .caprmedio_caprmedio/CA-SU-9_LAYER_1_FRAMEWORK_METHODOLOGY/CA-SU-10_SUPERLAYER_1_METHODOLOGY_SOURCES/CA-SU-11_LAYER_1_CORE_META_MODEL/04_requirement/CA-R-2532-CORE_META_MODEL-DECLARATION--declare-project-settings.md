---
atom_id: CA-R-2532
ref_id: CA-R-2532
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
version: 8
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 16:48:11 +0400
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Project.Settings

## Claim

### Formal Claim

```CFEL
# model
Project.Settings{::1}:: []{::0};

Project.Settings.*[in (Name, Prefix, AI Agent Confidence Threshold, Artifact Timestamp Timezone, Code-Root Locators, Confidence, Framework Control-Root Locator, Interaction, Authority Modes, Implementation Retry Limit, RMED Review)]{::3..11}
```

