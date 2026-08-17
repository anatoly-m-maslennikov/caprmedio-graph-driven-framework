---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-185
scope_path: layer:meta
subject_scopes:
  - session-engine
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Initialize the session engine at context boundaries

The CAPRMADIO session engine must initialize at every session start and reinitialize after every context compaction, without requiring an operator command.
