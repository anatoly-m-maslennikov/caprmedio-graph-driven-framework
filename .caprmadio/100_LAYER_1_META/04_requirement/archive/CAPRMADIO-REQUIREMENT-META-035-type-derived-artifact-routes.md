---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-035
scope_path: layer:meta
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-012
      - CAPRMADIO-REQUIREMENT-META-018
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-013
      - CAPRMADIO-REQUIREMENT-GOV-094
---

# Requirement — Derive artifact routes from registered types

Every governed artifact declares one registered `artifact_type` and, only when
needed, one direct `artifact_subtype`. That canonical type pair maps to exactly
one Revision mode, Content role, and Governance locus.

Artifact carriers do not repeat `revision_mode`, `content_role`, or
`governance_locus`. Writers and validators resolve them from the registered
type pair and fail closed when the pair is unknown, disabled, or ambiguous.

`scope_path` remains an explicit project-relative structural coordinate outside
the route. Priority, provenance, applicability, relation endpoints, and
type-specific facts remain separate when they cannot be derived.

## Rationale

Storing both a type and its deterministic route creates two writable
representations of one meaning. A single registered mapping preserves the
three-axis model while preventing metadata drift.
