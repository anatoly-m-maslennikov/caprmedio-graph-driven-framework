---
artifact_type: method
artifact_subtype: technical_decision
artifact_id: CAPRMADIO-IMPL-GOV-001
scope_path: layer:gov
subject_scopes:
  - methodology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-144
---

# Bounded scripted migrations

A migration script must be scoped to named carriers or exact patterns, fail
when an expected source pattern is absent, and leave reviewable repository
diffs. It does not rewrite immutable atomic artifacts unless a separately
accepted carrier migration explicitly authorizes that transformation.

## Rationale

Mechanical repository-wide migrations are less error-prone when one explicit transformation is applied consistently than when equivalent replacements are repeated manually.
