---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CARMADIO-EVALUATION-CASE-GOV-037
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-EVALUATION-CASE-GOV-032
  - type: check_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-111
---

# QA Case — Storage-boundary interpretability

## Claim checked

An operator can place an Atom, Journal record, resumable checkpoint, generated
cache, and disposable workspace in the governed storage boundary and explain
its retention behavior.

## Applicable conditions

The available boundaries are `.carmadio`, `.carmadio_journal`, `.carmadio_runtime`, and the
host temporary root.

## Acceptance criteria

At least 90% of classifications are correct and no classification treats
runtime or scratch as canonical truth.

## Failure disposition

Record a Concern for every ambiguous boundary and stop storage-boundary
readiness until the governing rule or its presentation is corrected.
