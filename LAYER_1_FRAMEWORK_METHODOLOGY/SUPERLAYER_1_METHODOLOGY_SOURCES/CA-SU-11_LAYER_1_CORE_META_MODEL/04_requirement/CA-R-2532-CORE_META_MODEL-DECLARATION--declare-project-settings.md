---
atom_id: CA-R-2532
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings
version: 8
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 16:48:11 +0400
---
## Summary

Declare Project.Settings

## Claim

```CFEL
Project.Settings{:1}: []{:0};
Project.Settings.*[in (Name, Prefix, AI Agent Confidence Threshold, Artifact Timestamp Timezone, Code-Root Locators, Confidence, Framework Control-Root Locator, Interaction, Authority Modes, Implementation Retry Limit, RMED Review)]{:3..11}
```
