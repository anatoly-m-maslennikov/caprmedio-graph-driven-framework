---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CARMADIO-TEST-CASE-GOV-059
scope_path: layer:gov
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-TEST-CASE-GOV-053
  - type: check_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-107
---

# QA Case — Effective-priority selection

## Claim checked

Conflict selection derives the governed effective priorities and never chooses
through a tie, incomparable scope, uncertainty, or ineligible external
obligation.

## Applicable conditions

1. Accept only stored `high`, `medium`, or `low`.
2. Reject stored `highest`, `critical`, and `deferred`.
3. Apply the strict-ancestor and earlier-layer increments independently and
   together, capped at virtual `highest`.
4. Confirm `ask_always` always asks.
5. Confirm `auto_by_effective_priority` selects exactly one unique eligible
   winner and asks on ties, incomparable scopes, uncertainty, or multiple
   winners.
6. Confirm unsatisfiable external obligations stop rather than auto-resolve.

## Acceptance criteria

Every comparison produces the governed effective priorities and never guesses
through a non-unique or ineligible result.

## Failure disposition

Stop automatic selection, ask the operator, and record a Concern for any
incorrect priority or unauthorized winner.
