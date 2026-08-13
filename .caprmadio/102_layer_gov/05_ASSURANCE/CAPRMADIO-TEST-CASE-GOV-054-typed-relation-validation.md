---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-TEST-CASE-GOV-054
scope_path: layer:gov
subject_scopes:
  - assurance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-TEST-CASE-GOV-036
  - type: check_of
    targets:
      - CAPRMADIO-IMPL-GOV-004
---

# QA Case — Canonical relation validity

## Claim checked

Every registered relation accepts valid endpoints and rejects unknown kinds,
invalid cardinality, and ambiguous active targets.

## Applicable conditions

1. Admit one valid example of every registered relation kind.
2. Reject an unknown relation kind.
3. Reject a relation without the endpoint cardinality required by its kind.
4. Resolve every target by active identity and reject zero or multiple active
   matches.
5. Confirm an archived target remains addressable as history but does not
   become active authority.

## Acceptance criteria

All valid examples pass and every invalid fixture fails with the exact relation
and endpoint identified.

## Failure disposition

Record a Concern naming the relation and invalid endpoint behavior and stop
relation-schema readiness.
