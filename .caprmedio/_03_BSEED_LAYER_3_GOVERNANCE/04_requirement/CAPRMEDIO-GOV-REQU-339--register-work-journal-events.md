---
subject_scopes:
  - runtime
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
---
# Register Work Journal events

GOV must register `started`, `progressed`, `completed`, `failed`, `interrupted`, `abandoned`, and `recovered` Work Journal events. Every event must identify its event, action, kind, occurrence time, session provenance, structural scope, operation, governed subjects, produced outputs, and preceding event when one exists; commit and pull-request provenance remain optional bindings.
