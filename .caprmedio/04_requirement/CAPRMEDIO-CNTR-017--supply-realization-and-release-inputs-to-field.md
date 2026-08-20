---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-18 20:48:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-CNTR-010--supply-realization-inputs-to-ops
relation_kind: realization_input
endpoints:
  - role: provider
    identity: native_realization
    origin: internal
  - role: provider
    identity: published_releases
    origin: internal
  - role: consumer
    identity: field_observations
    origin: internal
---
# Supply REALIZATION and RELEASES inputs to FIELD

Native Realization and published releases supply the enacted inputs from which field observations arise through the `realization_input` Contract.
