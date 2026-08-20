---
subject_scopes:
  - scope-topology
version: 3
updated_at: 2026-08-18 22:19:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-CNTR-009--supply-implementation-realization-to-delivery
relation_kind: realization_input
endpoints:
  - role: provider
    identity: native_realization
    origin: internal
  - role: consumer
    identity: releases_layer
    origin: internal
---
# Supply REALIZATION output to RELEASES

Native Realization supplies realized FRAMEWORK_ENGINE artifacts to the RELEASES Layer through the `realization_input` Contract without making those outputs normative authority.
