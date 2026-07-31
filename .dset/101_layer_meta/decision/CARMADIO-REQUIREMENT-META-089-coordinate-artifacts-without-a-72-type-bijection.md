---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-089
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-083
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-035
      - CARMADIO-REQUIREMENT-META-051
      - CARMADIO-REQUIREMENT-META-052
      - CARMADIO-REQUIREMENT-META-088
---

# Requirement — Coordinate artifacts without a 72-Type bijection

Every governed artifact occupies exactly one semantic coordinate:

```text
Artifact form × Content role × Governance locus
```

`scope_path` remains an independent structural ownership coordinate. Direct subtype, carrier format, creation procedure, change procedure, priority, lifecycle condition, and source provenance remain qualifying properties rather than additional primary axes.

The Cartesian product of three Artifact forms, eight Content roles, and three Governance loci describes 72 possible coordinates. It is a classification space, not a mandate to invent 72 distinct top-level Type names or enable every coordinate in every project.

META derives Type names only where a universal invariant exists, including the internal Atom rule. GOV may register additional form-local Types and direct subtypes, admit or reject coordinates, and let one operational Type vocabulary recur across coordinates when the complete coordinate remains explicit and unambiguous.

Writers and validators must never infer Artifact form, Content role, or Governance locus solely from a Type name when the Type is valid at more than one coordinate. An unknown, disabled, contradictory, or ambiguous coordinate fails closed.

## Primary claim

Artifact form, Content role, and Governance locus define an explicit classification space without requiring a one-to-one catalog of 72 distinct Type names.

## Rationale

Explicit coordinates preserve the orthogonal model while allowing predictable internal Atom names and reusable Journal or Projection vocabularies without artificial names for every cell.
