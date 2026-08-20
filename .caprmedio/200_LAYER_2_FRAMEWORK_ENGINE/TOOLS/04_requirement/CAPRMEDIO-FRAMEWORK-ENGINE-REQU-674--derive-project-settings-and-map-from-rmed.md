---
subject_scopes:
  - project-settings
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-SPEC-TOOLS-REQU-668--derive-project-settings-bindings-from-the-source-map
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Derive Project Settings and Map from RMED

The Project Settings generator must derive both the Project Settings values and their Map bindings directly from applicable active RMED `project_settings` contributions, never read either Projection as semantic input, and fail before writing on malformed, unresolved, ambiguous, contradictory, or non-deterministically composable contributions.
