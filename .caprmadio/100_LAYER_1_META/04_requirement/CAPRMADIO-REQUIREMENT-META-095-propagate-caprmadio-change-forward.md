---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-095
scope_path: layer:meta
subject_scope: scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-059
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
---

# Requirement — Propagate accepted change forward

An accepted upstream change propagates only forward through the ordered layer graph. It:

1. identifies affected downstream Projections, Methods, Assurance criteria, Delivery rules, Implementations, and Ops consumers;
2. marks each affected downstream artifact potentially stale without mutating historical atoms;
3. routes required reconciliation to the artifact's owning layer; and
4. closes only when every affected currentness or assurance gate reaches its required disposition.

Refreshing a Projection alone does not complete propagation. Downstream Method, Assurance, Delivery, Implementation, and Ops remain independently accountable. Feedback from a later layer may create a new upstream Concern, but cannot rewrite upstream authority or introduce a backward dependency.

## Primary claim

Accepted upstream change propagates potential staleness forward to every affected owner without creating backward governance or treating one Projection refresh as complete reconciliation.
