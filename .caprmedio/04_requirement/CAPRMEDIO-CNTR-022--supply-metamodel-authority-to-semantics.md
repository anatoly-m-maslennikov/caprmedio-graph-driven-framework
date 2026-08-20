---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-20 03:09:39
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-CNTR-002--supply-cumulative-authority-to-meta
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
relation_kind: authority_input
endpoints:
  - role: provider
    identity: metamodel
    origin: internal
  - role: consumer
    identity: semantics
    origin: internal
---
# Supply METAMODEL authority to SEMANTICS

SEMANTICS consumes the complete applicable upstream authority set from METAMODEL through the `authority_input` Contract.
