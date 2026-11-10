---
atom_id: CA-R-519
ref_id: CA-R-519
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Storage
tier: 1
relations: {}
status: Active
version: 16
updated_at: 2026-11-10 20:47:54 +0400
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-R-519-PROGRAMMATIC-RULE--persist-bounded-session-engine-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Persist bounded session-engine state

## Claim

### Prose Claim

the framework **must** persist the minimum project-local session state required **to** resume routing **after** context compaction under `.caprmedio_runtime`.

