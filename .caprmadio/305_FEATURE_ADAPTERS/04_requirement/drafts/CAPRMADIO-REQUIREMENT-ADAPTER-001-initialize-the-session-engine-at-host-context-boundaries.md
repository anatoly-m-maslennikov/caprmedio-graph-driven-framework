---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-ADAPTER-001
scope_path: feature:adapters
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-185-initialize-the-session-engine-at-context-boundaries
---

# Initialize the session engine at host context boundaries

Each supported agent-host adapter must initialize the CAPRMADIO session engine at the host's session-start and post-compaction boundaries without requiring `/ca` invocation.
