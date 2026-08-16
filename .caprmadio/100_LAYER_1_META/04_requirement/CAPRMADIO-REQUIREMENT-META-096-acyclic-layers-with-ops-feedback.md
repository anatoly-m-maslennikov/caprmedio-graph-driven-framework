---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-096
scope_path: layer:meta
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-065-ordered-realization-topology
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Keep current Layer dependencies acyclic

The ordered layer graph is a directed acyclic graph:

- structural authority and refinement flow
  `PROJECT → META → GOV → SPEC → IMPLEMENTATION → DELIVERY → OPS`;
- a later layer may consume authority from its own or any earlier layer;
- no layer may govern or redefine an earlier layer;
- dependency is distinct from scope specialization and `child_of`; and
- peer scopes interact through explicit Contracts rather than layer precedence.

A project Principle may directly parent a Core Requirement in any Layer. That
applicability edge neither creates a Layer dependency nor authorizes work to
bypass an intermediate Layer.

An Ops fact from a later layer may become input to Exploration Mode. After explicit acceptance, the result enters the normal forward flow at its proper owning layer. This feedback is not a backward authority edge.

If backward coupling cannot be deleted, re-homed, or expressed as feedback, CAPRMADIO proposes remodeling the coupled owners as horizontal Features. The operator must accept that structural change.
