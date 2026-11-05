---
atom_id: CA-R-2635
ref_id: CA-R-2635
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Implementation Retry Limit
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2635-CORE_META_MODEL-DECLARATION--declare-project-settings-implementation-retry-limit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2635-CORE_META_MODEL-DECLARATION--declare-project-settings-implementation-retry-limit.md
  source_atom_id: CA-R-2635
  source_atom_revision: 2
  source_sha256: a502dac8941ebb5cfd2de6091b0ae071341f0c1eac9a433ec1a234cca7ce1201
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.Implementation Retry Limit

## Claim

### Prose Claim


An omitted value follows the governed default resolution. A value is an integer at least zero. Zero permits no retries after the initial failure. The limit does not grant repair permission or bypass authority or confidence rules.

### Formal Claim

```CFEL
# model
Project.Settings.Implementation Retry Limit:: [int]{::0..1};

Project.Settings.Implementation Retry Limit.*[]{::0}
```

