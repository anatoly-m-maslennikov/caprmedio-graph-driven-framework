---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:03:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Reject incomplete commit context

## Claim checked

The commit Doer fails closed when a required sealed-context field is absent.

## Test case

Remove the canonical commit message from one otherwise valid sealed `UPDATE` context and invoke `COMMIT_CHANGE_SET` in apply mode.

## Acceptance criteria

The Doer returns a deterministic missing-field diagnostic naming the canonical-message field and creates no governed or Git state change.

## Failure disposition

Reject the Doer if it reconstructs the omitted field during apply, partially applies the context, or emits a generic diagnostic.
