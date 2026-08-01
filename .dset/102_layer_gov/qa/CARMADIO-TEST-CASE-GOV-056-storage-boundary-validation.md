---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CARMADIO-TEST-CASE-GOV-056
scope_path: layer:gov
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-TEST-CASE-GOV-048
  - type: check_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-111
---

# QA Case — Storage-boundary enforcement

## Claim checked

Each governed storage boundary accepts only its registered content and cleanup
cannot remove canonical authority or Journal history.

## Applicable conditions

1. Persist governed authority only under `.dset`.
2. Append journal records only as complete NDJSON lines under
   `.dset_journal`.
3. Remove `.dset_runtime` after a completed workflow and prove governed truth
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
