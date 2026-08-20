---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-19 01:14:21
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-CNTR-018--supply-cumulative-authority-to-methodology
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
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
  - role: consumer
    identity: framework_methodology_layer
    origin: internal
---
# Supply cumulative authority to FRAMEWORK_METHODOLOGY

FRAMEWORK_METHODOLOGY consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, GOVERNANCE, and PROJECT through the `authority_input` Contract.
