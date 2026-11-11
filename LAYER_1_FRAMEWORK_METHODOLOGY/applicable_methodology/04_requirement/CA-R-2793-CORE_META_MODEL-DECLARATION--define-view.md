---
identity:
  atom_id: CA-R-2793
  ref_id: CA-R-2793
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: MODEL//CAPRMEDIO <+ (View, View.id, View.sql, View.name)
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2793-CORE_META_MODEL-DECLARATION--define-view.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2793-CORE_META_MODEL-DECLARATION--define-view.md
  source_atom_id: CA-R-2793
  source_atom_revision: 4
  source_sha256: 375b384e539af6e9af0f6d69d03b239ee3f9d1b82fcd2c789588c323ea12a05e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define View

## Claim

### Prose Claim

A View is a Workbench SQL document in one Workspace. It has one stable string ID, one complete SQL query and may have one name. A View can be edited, run, fetched, focused, renamed, removed or saved through the Workspace operations.
### Formal Claim

```CFEL
# model
View.id{::1}:: [string]{::1};
View.sql{::1}:: [string]{::1};
View.name{::0..1}:: [string]{::0..1}
```

