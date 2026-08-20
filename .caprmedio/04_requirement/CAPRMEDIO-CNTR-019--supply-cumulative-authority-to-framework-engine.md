---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-19 01:14:21
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-CNTR-012--supply-cumulative-authority-to-realization
relation_kind: authority_input
endpoints:
  - role: provider
    identity: metamodel
    origin: internal
  - role: provider
    identity: semantics
    origin: internal
  - role: provider
    identity: governance
    origin: internal
  - role: provider
    identity: project
    origin: internal
  - role: provider
    identity: framework_methodology_layer
    origin: internal
  - role: consumer
    identity: framework_engine_layer
    origin: internal
---
# Supply cumulative authority to FRAMEWORK_ENGINE

FRAMEWORK_ENGINE consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, GOVERNANCE, PROJECT, and FRAMEWORK_METHODOLOGY through the `authority_input` Contract.
