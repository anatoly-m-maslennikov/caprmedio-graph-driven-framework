---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-19 04:55:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
---
# Permit one internal default Type per Content role

A Content role may register at most one default Type. Every default Type is internal, and the default does not prevent that role from admitting other internal, external, or relational Types.
