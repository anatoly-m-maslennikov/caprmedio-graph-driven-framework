---
atom_id: CA-R-578
ref_id: CA-R-578
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 1
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-507-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--automatically-initialize-the-session-engine
status: Active
version: 12
updated_at: 2026-10-27 20:00:10 +0400
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
---
# Initialize the session engine at host context boundaries

Each supported agent-host adapter **must** initialize the CAPRMEDIO session engine at the host's session-start **and** post-compaction boundaries **without** requiring `/ca` invocation.
