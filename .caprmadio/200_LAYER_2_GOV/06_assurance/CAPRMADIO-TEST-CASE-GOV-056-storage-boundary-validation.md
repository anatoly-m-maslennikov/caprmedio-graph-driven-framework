---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-TEST-CASE-GOV-056
scope_path: layer:gov
subject_scopes:
  - assurance
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-TEST-CASE-GOV-048
  check_of:
    - CAPRMADIO-REQUIREMENT-GOV-173-register-the-project-work-journal
---

# Storage-boundary enforcement

## Claim checked

Each governed storage boundary accepts only its registered content and cleanup
cannot remove canonical authority or Journal history.

## Applicable conditions

1. Persist governed authority only under `.caprmadio`.
2. Append Journal records only as complete NDJSON lines in the applicable
   `.caprmadio` role folder.
3. Remove `.caprmadio_runtime` after a completed workflow and prove governed truth
   and journal history remain intact.
4. Create scratch under the host temporary root, force success and handled
   failure, and prove cleanup in both cases.
5. Reject repository-local scratch and any attempt to keep the only governed
   copy in runtime or scratch.

## Acceptance criteria

Every boundary accepts only its governed content, and cleanup cannot remove
authority or journal history.

## Failure disposition

Record a high-priority Concern for misplaced canonical data, unsafe cleanup, or
repository-local scratch and stop storage-boundary readiness.
