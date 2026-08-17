---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-151
scope_path: layer:meta
subject_scope: lifecycle-traceability
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-077-propagate-atomic-revision-impact-through-lineage
    - CAPRMADIO-REQUIREMENT-META-121-bind-traceability-to-exact-claims-and-revisions
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
---
# Requirement — Provide lineage-impact Projections

CAPRMADIO provides a non-authoritative lineage-impact Projection whenever an upstream Atom revision is changed, replaced, or archived. The Projection derives the reachable descendant set without modifying or retargeting any persisted relation.

For every affected descendant, the Projection identifies the exact earlier revision in its lineage, the upstream event that triggered review, and the current disposition: review required, update the existing Atom, create a new Atom, archive the Atom, or confirmed compatible without change. Unresolved descendants remain visible until disposition is recorded through governed history.

The Projection may group and prioritize work, but it cannot change an Atom, break a historical link, or establish compatibility merely by listing it.

## Primary claim

A changed, replaced, or archived ancestor produces a derived review surface for every affected descendant while historical lineage remains intact.
