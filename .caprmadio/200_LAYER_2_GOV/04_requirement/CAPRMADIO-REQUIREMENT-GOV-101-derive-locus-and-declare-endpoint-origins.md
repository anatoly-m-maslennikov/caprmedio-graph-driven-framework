---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-101
scope_path: layer:gov
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-088
  child_of:
    - CAPRMADIO-REQUIREMENT-META-051-relational-artifacts-declare-endpoints
---
# Derive locus and declare endpoint origins

Each registered artifact type and optional direct subtype derives exactly one
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
type-derived route.
