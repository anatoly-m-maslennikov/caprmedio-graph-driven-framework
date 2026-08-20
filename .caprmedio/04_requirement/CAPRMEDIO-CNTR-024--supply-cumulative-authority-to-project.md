---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-20 03:09:39
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
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
  - role: consumer
    identity: project
    origin: internal
---
# Supply cumulative authority to PROJECT

PROJECT consumes the complete applicable upstream authority set from METAMODEL, SEMANTICS, and GOVERNANCE through the `authority_input` Contract.
