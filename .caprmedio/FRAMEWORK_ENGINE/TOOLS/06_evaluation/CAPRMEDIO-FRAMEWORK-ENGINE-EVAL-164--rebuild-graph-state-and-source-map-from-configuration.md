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
# Rebuild Graph State and Source Map from Configuration Authority

## Test case

**Fixture:** Remove both generated Graph State outputs from an isolated
current-project fixture whose Project Configuration binding and admitted active
`project_graph_state` contributions are valid.

**Expected result:** One authorized generator run recreates both outputs from
the exact Configuration revision and admitted sources, with exact per-value
bindings and without reading a prior Graph State or Source Map Projection.
