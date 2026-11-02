---
subject_scopes:
- routing
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: 2026-10-26 00:46:35 +0400
relations:
  child_of:
  - CA-R-1640
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-517@12
tier: 1
type: Rule
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Source Selection
---
# Provide a deterministic routing engine

the framework **must** provide a deterministic engine that resolves normalized operator intent **and** current context **to** ordered route candidates from the canonical routing tree.
