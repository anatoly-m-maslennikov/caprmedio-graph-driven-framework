---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-SKILL-023
scope_path: feature:skills
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-174-register-work-journal-events
    - CAPRMADIO-REQUIREMENT-GOV-175-recover-work-journal-coverage-without-invention
    - CAPRMADIO-REQUIREMENT-TOOL-030-append-work-journal-events
    - CAPRMADIO-REQUIREMENT-TOOL-031-reconcile-work-journal-coverage
---

# Record governed action lifecycles

The session engine and every Skill that performs governed work must use deterministic Tools to record its start and terminal outcome and to reconcile missing Work Journal coverage after session initialization or context recovery.
