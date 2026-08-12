---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-098
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-035
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
      - CARMADIO-REQUIREMENT-META-089
---

# Requirement — Derive artifact coordinates from registered types

Every governed artifact declares one registered `artifact_type` and, only when needed, one direct `artifact_subtype`. That canonical type pair maps to exactly one Artifact form, Content role, and Governance locus.

Artifact carriers do not repeat `artifact_form`, `content_role`, or `governance_locus`. Writers and validators resolve them from the registered type pair and fail closed when the pair is unknown, disabled, contradictory, or ambiguous.

`scope_path` remains an explicit structural coordinate outside the semantic route. Priority, provenance, applicability, relation endpoints, and type-specific facts remain separate when they cannot be derived.

## Primary claim

One registered artifact Type and optional direct subtype determine exactly one Artifact form, Content role, and Governance locus without duplicating those derived values in the carrier.

## Rationale

One registered mapping prevents multiple writable representations of the same semantic coordinate while preserving explicit structural scope and non-derived metadata.
