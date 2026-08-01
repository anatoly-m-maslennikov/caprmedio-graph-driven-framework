---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: DSET-EVALUATION-CASE-GOV-035
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-EVALUATION-CASE-GOV-026
  - type: check_of
    targets:
      - DSET-IMPL-GOV-004
---

# Evaluation Case — Assess relation-vocabulary interpretability

Give independent reviewers representative artifact pairs and ask them to
select the relation kind without seeing an answer key.

Evaluate whether reviewers can distinguish lineage, implementation, checking,
evidence, resolution, conflict solution, override, replacement, recurrence,
and generic relation without inventing new kinds.

The plan passes when at least 90% of selections match the governed answer and
no relation pair produces a repeated conceptual ambiguity.
