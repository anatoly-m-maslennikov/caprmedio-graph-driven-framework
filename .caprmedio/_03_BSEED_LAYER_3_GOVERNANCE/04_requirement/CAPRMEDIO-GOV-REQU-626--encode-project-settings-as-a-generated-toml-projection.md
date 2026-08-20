---
subject_scopes:
  - settings
project_settings:
  schema_version: 2.0
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-382--generate-one-project-settings-catalog
  child_of:
    - CAPRMEDIO-META-REQU-620--classify-project-settings-as-an-implementation-projection
    - CAPRMEDIO-REQU-622--establish-project-configuration-through-rmed
---
# Encode project settings as a generated TOML Projection

GOV must encode `.caprmedio/caprmedio_project_settings.toml` as a read-only TOML Implementation Projection regenerated from applicable active Project RMED Atoms with carrier-native Projection metadata and no operator-authored setting values.
