---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-174
scope_path: layer:gov
subject_scopes:
  - runtime
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-173-register-the-project-work-journal
---

# Register Work Journal events

GOV must register `started`, `progressed`, `completed`, `failed`, `interrupted`, `abandoned`, and `recovered` Work Journal events. Every event must identify its event, action, kind, occurrence time, session provenance, structural scope, operation, governed subjects, produced outputs, and preceding event when one exists; commit and pull-request provenance remain optional bindings.
