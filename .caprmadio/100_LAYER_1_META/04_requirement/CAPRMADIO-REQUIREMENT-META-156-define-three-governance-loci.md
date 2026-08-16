---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-156
scope_path: layer:meta
subject_scope: semantics
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-069
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Requirement — Define three Governance loci

Governance locus classifies where a governed artifact's primary meaning is
owned. It has exactly three values:

- `internal` means the current project establishes and owns the meaning;
- `external` means an identified source outside the current project establishes
  or imposes the meaning, while the project records and binds itself to that
  source; and
- `relation` means the meaning exists only between explicit role-bearing
  endpoints and is not owned by either endpoint in isolation.

Governance locus is independent of Artifact form, Content role, structural
scope, provenance, and the internal or external origin of individual relational
endpoints. A citation, dependency, or traceability edge does not make an
otherwise internal or external artifact relational.

The current project boundary is ambient. META owns these three meanings; GOV
registers the concrete Types, endpoint schemas, and carrier rules admitted at
their coordinates.

## Primary claim

Every governed artifact has exactly one Governance locus—internal, external,
or relation—determined by where its primary meaning is owned.
