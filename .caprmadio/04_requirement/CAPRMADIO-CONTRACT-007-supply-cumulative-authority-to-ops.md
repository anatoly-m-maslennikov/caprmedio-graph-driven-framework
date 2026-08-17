---
subject_scopes:
  - scope-topology
version: 4
updated_at: 2026-08-17 19:02:58
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-228-assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMADIO-REQUIREMENT-175-define-meta-layer-scope-and-contracts
    - CAPRMADIO-REQUIREMENT-176-define-gov-layer-scope-and-contracts
    - CAPRMADIO-REQUIREMENT-177-define-spec-layer-scope-and-contracts
    - CAPRMADIO-REQUIREMENT-178-define-implementation-layer-scope-and-contracts
    - CAPRMADIO-REQUIREMENT-179-define-delivery-layer-scope-and-contracts
    - CAPRMADIO-REQUIREMENT-180-define-ops-layer-scope-and-contracts
relation_kind: authority_input
endpoints:
  - role: provider
    identity: project
    origin: internal
  - role: provider
    identity: meta_layer
    origin: internal
  - role: provider
    identity: gov_layer
    origin: internal
  - role: provider
    identity: spec_layer
    origin: internal
  - role: consumer
    identity: ops_layer
    origin: internal
---
# Supply cumulative authority to Ops

OPS consumes the complete applicable upstream normative authority set from PROJECT, META, GOV, and SPEC through the `authority_input` Contract.
