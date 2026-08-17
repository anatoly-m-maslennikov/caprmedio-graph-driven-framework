---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-EVALUATION-CASE-GOV-037
scope_path: layer:gov
subject_scopes:
  - assurance
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-EVALUATION-CASE-GOV-032
  check_of:
    - CAPRMADIO-REQUIREMENT-GOV-173-register-the-project-work-journal
---

# Storage-boundary interpretability

## Claim checked

An operator can place an Atom, Journal record, resumable checkpoint, generated
cache, and disposable workspace in the governed storage boundary and explain
its retention behavior.

## Applicable conditions

The available boundaries are `.caprmadio`, `.caprmadio_runtime`, and the host
temporary root. Governed Journals are located inside `.caprmadio` by scope and
Content role.

## Acceptance criteria

At least 90% of classifications are correct and no classification treats
runtime or scratch as canonical truth.

## Failure disposition

Record a Concern for every ambiguous boundary and stop storage-boundary
readiness until the governing rule or its presentation is corrected.
