---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-001
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

# Requirement — Governed feedback cycle

Test cases, evaluation cases, and implementation plans are Methods. Code and
generated operative outputs are Implementations. Test and evaluation results
are Observations. Each governed artifact has one primary content role while
relations connect it to other roles.

## Primary claim

CAPRMADIO uses one six-role feedback cycle: Inquiry, Definition, Rationale, Method, Implementation, and Observation.

## Rationale

One role cycle keeps desired state, reasoning, realization, and observed feedback distinct without turning workflow position into artifact identity.
