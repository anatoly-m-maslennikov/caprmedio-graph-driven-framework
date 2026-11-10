---
atom_id: CA-R-519
ref_id: CA-R-519@15
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage
tier: 1
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
status: Archived
version: 15
updated_at: 2026-11-02 19:44:26 +0400
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
carrier_destination:
  file:
    name: CA-R-519@15-SKILLS-RULE--persist-bounded-session-engine-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement/archive
---
## Summary

Persist bounded session-engine state

## Claim

### Prose Claim

the framework **must** persist the minimum project-local session state required **to** resume routing **after** context compaction under `.caprmedio_runtime`.
