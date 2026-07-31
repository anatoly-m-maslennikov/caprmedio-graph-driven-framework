---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-102
scope_path: layer:meta
subject_scopes:
  - external-boundary
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-056
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
      - CARMADIO-REQUIREMENT-META-089
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-051
      - CARMADIO-REQUIREMENT-META-091
---

# Requirement — Preserve external boundary obligations

An operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, or comparable external obligation is represented by its semantic contribution and locus.

An obligation imposed by one external source is an external Requirement. An obligation that exists between explicit participants is a relation-locus Contract with explicit endpoints. Both pin the applicable external source version or digest.

Implementation must conform to the exact committed obligation revision it consumes and cannot rewrite it. A changed external source creates a new committed revision when the same obligation remains identifiable. A different obligation requires a new Atom with an explicit replacement relation. Existing Implementations remain bound to their consumed revisions until lineage-impact review determines their disposition.

META defines this boundary without assigning concrete external or relational Type names. GOV owns their registered names, carriers, identities, and catalog entries.

## Primary claim

External obligations are external Requirements or endpoint-bound Contracts, preserve their pinned source revision, and cannot be rewritten by their Implementations.

## Rationale

Separating externally imposed Requirements from participant Contracts preserves non-negotiable interfaces without reviving the retired Definition role.
