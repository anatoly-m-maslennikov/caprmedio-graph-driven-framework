---
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: 2026-10-26 00:46:35 +0400
relations:
  child_of:
  - CA-R-1643
  - CA-R-1644
  - CA-R-1126
  - CA-R-1127
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-562@12
type: Rule
tier: 1
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
---
# Record governed action lifecycles

the session engine **and** **every** Skill that performs governed work **must** use deterministic Tools **to** record its start **and** terminal outcome **and** **to** reconcile missing Work Journal coverage **after** session initialization **or** context recovery.
