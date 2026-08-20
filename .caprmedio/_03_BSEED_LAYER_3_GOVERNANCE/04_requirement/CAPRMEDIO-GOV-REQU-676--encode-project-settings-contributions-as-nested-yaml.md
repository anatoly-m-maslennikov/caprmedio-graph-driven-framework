---
subject_scopes:
  - settings
version: 2
updated_at: 2026-08-21 00:21:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--encode-project-setting-values-in-owning-rmed-atoms
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode configuration surfaces in owning Atoms

GOV must encode each configurable Tool or Extension's allowed keys, value types, defaults, constraints, and governed meaning in its owning Atoms. These Atoms must not encode the current project's selected values or a `project_settings` contribution; those values belong only to the Project Configuration Atom.
