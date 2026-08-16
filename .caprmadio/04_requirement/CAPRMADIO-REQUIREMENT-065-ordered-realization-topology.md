---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-065
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Define the ordered realization topology

CAPRMADIO uses one project scope above six ordered Layers:

```text
PROJECT → META → GOV → SPEC → IMPLEMENTATION → DELIVERY → OPS
```

PROJECT is the root structural scope rather than a seventh Layer. It owns this
Layer decomposition, the canonical responsibility and boundary of every Layer,
and every Contract whose endpoints belong to different Layers. A Layer may
govern work inside its boundary but cannot unilaterally define or change a
cross-Layer Contract. Traceability between individual artifacts remains
governed by its registered relation kind and does not become a Contract merely
because the artifacts occupy different Layers.

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, principles, invariants, Layer topology, and inter-Layer semantics |
| GOV | Carrier, identity, naming, routing, provenance, lifecycle, and structural rules |
| SPEC | The applicable Requirement, Method, Assurance, and Delivery authority |
| IMPLEMENTATION | The actual project realization of SPEC and its traceability |
| DELIVERY | Packaging, environment, deployment, release, and publication authority |
| OPS | Post-delivery operation, supportability, investigation, containment, recovery, and runtime evidence |
