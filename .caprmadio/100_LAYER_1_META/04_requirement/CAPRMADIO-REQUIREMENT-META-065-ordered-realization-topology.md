---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-065
scope_path: layer:meta
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-META-116-preserve-strict-semantic-distinctions
---

# Define the ordered realization topology

CAPRMADIO uses six ordered layers:

```text
META → GOV → SPEC → IMPLEMENTATION → DELIVERY → OPS
```

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, principles, invariants, Layer topology, and inter-Layer semantics |
| GOV | Carrier, identity, naming, routing, provenance, lifecycle, and structural rules |
| SPEC | The applicable Requirement, Method, Assurance, and Delivery authority |
| IMPLEMENTATION | The actual project realization of SPEC and its traceability |
| DELIVERY | Packaging, environment, deployment, release, and publication authority |
| OPS | Post-delivery operation, supportability, investigation, containment, recovery, and runtime evidence |
