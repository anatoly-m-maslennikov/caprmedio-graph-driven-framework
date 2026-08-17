---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-067
scope_path: layer:meta
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-192-preserve-bounded-meaning-across-structural-scales
---
# Define current Layer handoffs

Each adjacent boundary owns a handoff:

| Boundary | Accepted input | Produced output |
|---|---|---|
| META → GOV | Semantic invariants and layer constitution | Governable carriers, identities, settings, lifecycle, and conflict policy |
| GOV → SPEC | Governed project scopes, enabled artifact vocabulary, and authoring constraints | Project-owned Requirement, Method, Assurance, and Delivery authority |
| SPEC → IMPLEMENTATION | Complete applicable `RMAD` Specification | Concrete realization and its traceability |
| IMPLEMENTATION → DELIVERY | Assured realization and distributable outputs | Environment-specific package, deployment, release, or publication |
| DELIVERY → OPS | Released and supportable output | Operable, observable, and diagnosable service or product |

Every handoff declares entry criteria, exit criteria, and blocker behavior.
Adjacent handoffs are preferred. A direct forward skip is allowed only when
the intermediate layers have no meaningful transformation or ownership to add.
CAPRMADIO does not create placeholder artifacts merely to simulate an unnecessary handoff.
