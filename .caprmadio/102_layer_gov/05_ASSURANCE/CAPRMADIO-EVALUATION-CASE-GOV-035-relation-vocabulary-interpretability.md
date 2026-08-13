---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-EVALUATION-CASE-GOV-035
scope_path: layer:gov
subject_scopes:
  - assurance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-EVALUATION-CASE-GOV-026
  - type: check_of
    targets:
      - CAPRMADIO-IMPL-GOV-004
---

# QA Case — Relation-vocabulary interpretability

## Claim checked

The registered relation vocabulary lets an independent assessor select the
governed relation for representative artifact pairs without inventing another
kind.

## Applicable conditions

The case covers lineage, implementation, checking, evidence, resolution,
conflict solution, override, replacement, recurrence, and generic relation.

## Acceptance criteria

At least 90% of classifications match the governed relation and no pair
produces a repeated conceptual ambiguity.

## Failure disposition

Record a Concern for every ambiguous pair and stop relation-vocabulary
readiness until the owning GOV claim or its presentation is corrected.
