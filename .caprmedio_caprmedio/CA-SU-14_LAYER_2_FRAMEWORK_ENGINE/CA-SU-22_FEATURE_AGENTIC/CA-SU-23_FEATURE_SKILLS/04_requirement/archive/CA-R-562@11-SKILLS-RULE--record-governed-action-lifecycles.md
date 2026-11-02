---
subject_scopes:
- session-engine
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 11
updated_at: 2026-10-24 11:58:20 +0400
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
atom_id: CA-R-562@11
type: Rule
tier: 1
---
# Record governed action lifecycles

the session engine **and** **every** Skill that performs governed work **must** use deterministic Tools **to** record its start **and** terminal outcome **and** **to** reconcile missing Work Journal coverage **after** session initialization **or** context recovery.
