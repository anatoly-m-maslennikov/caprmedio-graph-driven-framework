---
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 8
updated_at: 2026-10-24 04:23:08 +0400
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-509-FRAMEWORK_METHODOLOGY-REQUIREMENT--govern-session-engine-rehydration-behavior
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-519@8
tier: 1
type: Rule
---
# Persist bounded session-engine state

the framework **must** persist the minimum project-local session state required **to** resume routing **after** context compaction under `.caprmedio_runtime`.
