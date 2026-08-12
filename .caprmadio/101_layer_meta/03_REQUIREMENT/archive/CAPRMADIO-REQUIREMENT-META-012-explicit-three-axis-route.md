---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-012
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-018
---

# Requirement — Explicit three-axis route

Routing values are declared metadata. Authority, provenance, priority,
lifecycle state, applicability, and scope path remain independent.

## Primary claim

Every governed artifact explicitly declares one revision_mode, one content_role, and one governance_locus; other metadata remains outside this route.

## Rationale

Independent explicit axes prevent filenames, folders, workflow position, authority, or lifecycle from silently reclassifying an artifact.
