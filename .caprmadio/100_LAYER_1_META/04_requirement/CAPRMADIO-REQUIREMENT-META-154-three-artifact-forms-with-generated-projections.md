---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-154
scope_path: layer:meta
subject_scope: artifact-model
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-123
      - CAPRMADIO-REQUIREMENT-META-131
      - CAPRMADIO-REQUIREMENT-META-133
      - CAPRMADIO-REQUIREMENT-META-136
      - CAPRMADIO-REQUIREMENT-META-153
---

# Requirement — Use three Artifact forms with generated Projections

Every governed artifact has exactly one Artifact form:

- `atom` is the smallest independently governed unit under its Content role's
  atomicity model, with one stable identity and one indivisible lifecycle.
  Every committed Atom revision is immutable and recoverable through governed
  history.
- `journal` is an ordered sequence of admitted records. Records may be appended,
  while accepted records cannot be edited, reordered, or removed.
- `projection` is a non-authoritative generated view. Every Projection is
  reproducibly generated from declared governed sources, never edited as its
  source of meaning, and never populated from operator-authored projection
  content. A Projection may be mandatory and generated automatically when an
  applicable rule, source change, or gate requires it.

A declared source identifies the exact governed Artifact revisions, Journal
frontier, or native project target revisions consumed by the generator. The
source declaration also identifies the governed generator and configuration
needed to reproduce the result. A Projection is current only for the context in
which its declared source frontier and generator remain current and no
unresolved lineage impact invalidates the view.

Artifact form is independent of Content role, Governance locus, and structural
scope. Implementation is a Content role and the native project realization,
not an Artifact form. A directly revised governed artifact is an Atom or an
append-only Journal, never a Projection.

## Primary claim

CAPRMADIO classifies governed artifacts as Atom, Journal, or generated
Projection, with no directly edited Projection exception.
