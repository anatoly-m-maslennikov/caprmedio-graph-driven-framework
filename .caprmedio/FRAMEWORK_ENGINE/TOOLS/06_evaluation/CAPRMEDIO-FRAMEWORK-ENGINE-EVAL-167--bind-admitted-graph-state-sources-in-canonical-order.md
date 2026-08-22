---
artifact_subtype: qa_case
subject_scopes:
  - project-settings
version: 3
updated_at: 2026-08-22 04:20:12
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-674--derive-project-graph-state-and-map-from-configuration-authority
---
# Bind admitted Graph State sources in canonical order

## Test case

**Fixture:** Provide multiple admissible active `project_graph_state`
contributions to one registered multi-source Graph State value, then discover
the carriers in different filesystem orders.

**Expected result:** Every run emits the same value and Source Map bindings in
canonical source-identity order, with no contribution treated as a
project-selected setting.
