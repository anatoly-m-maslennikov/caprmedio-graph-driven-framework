---
artifact_type: method
artifact_id: CAPRMADIO-METHOD-METHODOLOGY-001
scope_path: feature:methodology
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-185-initialize-the-session-engine-at-context-boundaries
    - CAPRMADIO-REQUIREMENT-GOV-171-govern-session-engine-rehydration
---

# Initialize the CAPRMADIO session

At session start and after context compaction:

1. Discover the owning project and current scope.
2. Load routing invariants, project settings, and compact session state.
3. Validate the canonical routing tree.
4. Resolve applicable active authority on demand.
5. Enter Exploration Mode unless the operator has supplied an executable instruction.
