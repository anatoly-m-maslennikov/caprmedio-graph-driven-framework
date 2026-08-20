---
subject_scopes:
  - settings
version: 7
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
  replacement_of:
    - CAPRMEDIO-GOV-REQU-629--encode-project-settings-projection-rules-as-a-toml-atom
---
# Register Project Settings Projection mechanics

GOV must register `02_FRAMEWORK_ENGINE/TOOLS/generate_project_settings.py` as the deterministic generator that refreshes the registered Project Settings Map Projection from its selected active RMED sources, reads that Map to emit the Project Settings Projection with exact per-setting source-Atom revision bindings, resolves the Framework Settings Atom through its governed native-Atom identity and current-revision binding, and rejects missing, ambiguous, contradictory, malformed, or incompletely mapped sources.
