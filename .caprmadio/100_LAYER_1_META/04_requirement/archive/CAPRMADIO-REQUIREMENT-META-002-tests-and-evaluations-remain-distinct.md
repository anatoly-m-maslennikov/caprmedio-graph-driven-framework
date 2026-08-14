---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-002
scope_path: layer:meta
subject_scope: assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-001
---

# Requirement — Tests and Evaluations remain distinct

Behavior with one exact expected result belongs to deterministic Test casening.
Behavior with multiple acceptable results judged by criteria belongs to
Evaluation casening. Their execution results remain distinct Observations.

## Primary claim

CAPRMADIO keeps deterministic Tests and qualitative, probabilistic, statistical, or model-judged Evaluations in separate plans, implementations, and observation streams.

## Rationale

Automation does not erase the semantic difference between an exact assertion and a judgment against criteria or a rubric.
