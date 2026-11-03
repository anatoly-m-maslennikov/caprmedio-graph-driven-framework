---
atom_id: CA-R-2635
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Implementation Retry Limit
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2635-CORE_META_MODEL-DECLARATION--declare-project-settings-implementation-retry-limit.md
  source_atom_id: CA-R-2635
  source_atom_revision: 1
  source_sha256: 4279dfcc77266fb34b62499adfb816c0442fd5f2f3dfd2801639d0ec9b041d28
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.Implementation Retry Limit

## Claim

An omitted value follows the governed default resolution. A value is an integer at least zero. Zero permits no retries after the initial failure. The limit does not grant repair permission or bypass authority or confidence rules.

```CFEL
Project.Settings.Implementation Retry Limit{:0..1}: [int]{:1};
Project.Settings.Implementation Retry Limit.*[]{:0}
```
