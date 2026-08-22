---
subject_scopes:
  - project-settings
version: 3
updated_at: 2026-08-22 04:20:12
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
---
# Derive Project Graph State and Source Map from Configuration Authority

The Project Graph State generator must resolve exactly one governed Project
Configuration Atom as the sole source of current operator-selected values. It
may compose only applicable active Atom `project_graph_state` contributions
that declare registered facts, allowed values, defaults, structural context, or
other non-configurational inputs. No Atom other than the Configuration Atom
may contribute `project_settings` values.

The generator must derive Project Graph State and its Source Map from those
exact sources, never read either Projection as semantic input, preserve exact
per-value bindings, and fail before writing on missing, malformed, unresolved,
ambiguous, stale, contradictory, or incompletely mapped sources.
