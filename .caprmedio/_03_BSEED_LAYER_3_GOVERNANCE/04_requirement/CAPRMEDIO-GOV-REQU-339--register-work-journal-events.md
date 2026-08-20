---
subject_scopes:
  - runtime
version: 2
updated_at: 2026-08-20 20:09:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
---
# Register Work Journal events

GOV must register `started`, `progressed`, `completed`, `failed`, `interrupted`, `abandoned`, and `recovered` Work Journal events. Every newly accepted event must identify its event, action, kind, full GitHub author username, occurrence time, session provenance, structural scope, operation, governed subjects, produced outputs, and preceding event when one exists. A governed repository-file-change event must also carry `action_message` byte-identical to the canonical Git commit message for that change; commit and pull-request provenance remain optional bindings. Previously accepted events remain valid under their declared schema version.
