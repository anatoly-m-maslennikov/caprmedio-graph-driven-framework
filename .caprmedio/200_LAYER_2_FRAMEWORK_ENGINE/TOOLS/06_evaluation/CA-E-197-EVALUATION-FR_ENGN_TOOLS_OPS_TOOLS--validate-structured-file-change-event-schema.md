---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 21:34:00
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Validate the structured file-change event schema

## Claim checked

Every completed `governed_file_change` event has the canonical structured fields and does not duplicate prior state or the projected Git message.

## Test case

Validate one event for each action type against the registered schema, then inject an absent required field, an invalid state-dependent field, `action_message`, `before_path`, and `before_sha256` in separate runs.

## Acceptance criteria

Each valid event passes; each malformed event fails with a stable field-specific diagnostic; `sources` is ordered; `result` is singular; and forbidden duplicated fields are rejected.

## Failure disposition

Reject the Journal record when its structure is incomplete, ambiguous, action-inconsistent, or duplicates derivable state.
