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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md
  source_atom_id: CA-R-2532
  source_atom_revision: 8
  source_sha256: 8149738f83fd0f420ae4f63d9c95219e0999659f5c391aad820d48fba0bdc106
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Project.Settings

## Claim

```CFEL
Project.Settings{:1}: []{:0};
Project.Settings.*[in (Name, Prefix, AI Agent Confidence Threshold, Artifact Timestamp Timezone, Code-Root Locators, Confidence, Framework Control-Root Locator, Interaction, Authority Modes, Implementation Retry Limit, RMED Review)]{:3..11}
```
