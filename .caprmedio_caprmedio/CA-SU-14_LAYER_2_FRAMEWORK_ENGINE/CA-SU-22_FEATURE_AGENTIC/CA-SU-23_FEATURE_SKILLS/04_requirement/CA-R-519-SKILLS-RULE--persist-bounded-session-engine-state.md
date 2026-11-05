---
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 15
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
author: Anatoly Maslennikov
role: Requirement
current_scope_unit: SKILLS
status: Active
atom_id: CA-R-519
ref_id: CA-R-519
tier: 1
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
container:
  scope_unit: CA-SU-23
---
# Persist bounded session-engine state

the framework **must** persist the minimum project-local session state required **to** resume routing **after** context compaction under `.caprmedio_runtime`.
