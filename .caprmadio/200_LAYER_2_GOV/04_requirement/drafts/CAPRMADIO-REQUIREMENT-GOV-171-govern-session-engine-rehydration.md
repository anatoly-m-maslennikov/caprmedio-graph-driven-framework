---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-171
scope_path: layer:gov
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-185-initialize-the-session-engine-at-context-boundaries
    - CAPRMADIO-REQUIREMENT-META-110-isolate-runtime-state-under-caprmadio-runtime
---

# Govern session-engine rehydration

Session-engine rehydration must restore only routing invariants, current scope, applicable settings, compact session state, and references needed to load active authority on demand.
