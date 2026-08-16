---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-185
scope_path: layer:meta
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-057-bounded-recursive-self-hosting
---

# Initialize the session engine at context boundaries

The CAPRMADIO session engine must initialize at every session start and reinitialize after every context compaction, without requiring an operator command.
