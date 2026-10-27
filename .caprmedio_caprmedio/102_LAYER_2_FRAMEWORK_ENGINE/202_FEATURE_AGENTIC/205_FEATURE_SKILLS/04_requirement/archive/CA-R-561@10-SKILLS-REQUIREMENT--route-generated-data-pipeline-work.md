---
subject_scopes:
- routing
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 10
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CAPRMEDIO-GOV-REQU-337-CORE_META_MODEL-REQUIREMENT--register-generated-data-stage-prefixes
  - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-521--validate-generated-data-stage-pipelines
  - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-524--project-work-journal-ndjson-to-toon
  - CA-R-1059
  - CA-R-1060
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-561@10
type: Rule
tier: 1
---
# Route generated-data pipeline work

Skills that handle generated-data pipeline work **must** route stage selection, validation, **and** materialization through the governed stage vocabulary **and** deterministic Tools **without** redefining either.
