---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-TOOL-027
scope_path: feature:tools
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-171-govern-session-engine-rehydration
---

# Persist bounded session-engine state

The framework must persist the minimum project-local session state required to resume routing after context compaction under `.caprmadio_runtime`.
