---
artifact_type: concern
artifact_subtype: problem
artifact_id: CAPRMADIO-PROBLEM-GOV-013
scope_path: layer:gov
subject_scopes:
  - provenance
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMADIO-REQUIREMENT-META-113-preserve-implementation-traceability-in-journals
    - CAPRMADIO-REQUIREMENT-GOV-173-register-the-project-work-journal
    - CAPRMADIO-REQUIREMENT-GOV-178-register-implementation-journals-and-projections
---

# Problem — Implementation Journals and Projections are not materialized

The repository does not yet provide the governed Implementation Journal
carriers, journal schema, append writer, replay engine, or deterministic
Projection generator required by the current META and GOV authority.

Git commit messages currently provide the nearest implementation-lineage
record. That record can be rewritten or collapsed by squash merges, rebases,
cherry-picks, and repository migrations, so it cannot satisfy the durable
semantic binding required between normative Atoms and native implementation
targets.

## Primary claim

The accepted Implementation Journal and derived-Projection model is specified
but not yet available as an executable repository capability.

## Rationale

Keeping this gap explicit prevents generated coverage views or Git history
from being treated as the canonical implementation trace before the governed
journal lifecycle is operational.
