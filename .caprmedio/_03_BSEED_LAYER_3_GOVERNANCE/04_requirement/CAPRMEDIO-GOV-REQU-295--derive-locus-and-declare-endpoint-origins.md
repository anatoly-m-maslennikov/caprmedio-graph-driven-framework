---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-19 04:55:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-444--artifact-and-endpoint-governance-origins
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
---
# Derive locus and declare endpoint origins

Each registered Artifact Type derives exactly one
`governance_locus`: `internal`, `external`, or `relation`. Artifact carriers do
not repeat the derived locus or store a separate `governance_origin` property.

A relational artifact declares one stable relation kind and at least two
typed, role-bearing endpoints. Each endpoint independently declares whether its
participant is internal or external relative to the current project boundary.
Direction follows from the relation kind and endpoint roles.

Endpoint origin does not become another artifact-routing axis and cannot be
inferred from the relation carrier's locus. External provenance, issuer, source,
or ownership facts use their precise type-specific properties rather than a
generic duplicate origin field.

## Rationale

The rule preserves the participant information needed for contracts and pull
requests without storing a second artifact-level coordinate that duplicates the
Type-derived route.
