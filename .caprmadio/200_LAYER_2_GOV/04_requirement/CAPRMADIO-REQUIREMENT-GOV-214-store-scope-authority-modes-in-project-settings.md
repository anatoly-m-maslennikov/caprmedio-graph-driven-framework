---
subject_scopes:
  - settings
version: 2
updated_at: 2026-08-17 18:42:51
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-225-require-complete-authority-topology-in-strict-mode
    - CAPRMADIO-REQUIREMENT-235-permit-incomplete-rmad-topology-in-casual-mode
---
# Store scope authority modes in project settings

The project TOML settings must store the current `authority_mode` for each configured scope as `strict` or `casual` and must resolve an omitted scope value to `casual`.
