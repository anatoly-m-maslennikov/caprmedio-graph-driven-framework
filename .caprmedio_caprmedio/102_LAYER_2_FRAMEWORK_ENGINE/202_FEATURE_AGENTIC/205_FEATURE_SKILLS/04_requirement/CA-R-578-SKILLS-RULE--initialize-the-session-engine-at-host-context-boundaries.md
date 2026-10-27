---
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-507-FRAMEWORK_METHODOLOGY-CORE-REQUIREMENT--automatically-initialize-the-session-engine
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Active
atom_id: CA-R-578
type: Rule
tier: 1
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
---
# Initialize the session engine at host context boundaries

Each supported agent-host adapter **must** initialize the CAPRMEDIO session engine at the host's session-start **and** post-compaction boundaries **without** requiring `/ca` invocation.
