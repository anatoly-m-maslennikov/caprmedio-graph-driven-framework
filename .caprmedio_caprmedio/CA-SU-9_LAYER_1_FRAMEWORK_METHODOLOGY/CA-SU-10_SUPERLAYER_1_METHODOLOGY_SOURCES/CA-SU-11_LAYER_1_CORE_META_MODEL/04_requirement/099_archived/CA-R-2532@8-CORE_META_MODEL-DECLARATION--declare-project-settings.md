---
atom_id: CA-R-2532
ref_id: CA-R-2532@8
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
tier: 3
status: archived
version: 8
updated_at: 2026-11-02 16:48:11 +0400
carrier_destination:
  file:
    name: CA-R-2532@8-CORE_META_MODEL-DECLARATION--declare-project-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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

