---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-104
scope_path: layer:meta
subject_scope: scope-topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-065
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-071
      - CARMADIO-REQUIREMENT-META-100
---

# Requirement — Propagate structural scope through realization

## Primary claim

A project structural scope is registered once and reused unchanged by every
realization layer that governs it. Layer-local subject scopes may refine its
meaning but never redefine its structural identity.

## Rationale

One cross-layer scope identity preserves traceability without copying project
truth or turning a layer-local subject classification into a second structural
owner.
