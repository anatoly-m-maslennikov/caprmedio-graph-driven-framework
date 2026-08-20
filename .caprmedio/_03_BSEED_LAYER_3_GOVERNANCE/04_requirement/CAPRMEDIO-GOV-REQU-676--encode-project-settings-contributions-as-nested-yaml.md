---
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-675--encode-project-setting-values-in-owning-rmed-atoms
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Encode Project Settings contributions as nested YAML

GOV must encode an RMED Atom's optional Project Settings contribution under one top-level `project_settings` YAML map whose nested plain keys match the emitted setting path, whose leaves are supported scalar or list values, and whose absent, empty, duplicated, or structurally ambiguous entries contribute no accepted value and fail validation when present.
