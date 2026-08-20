---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 22:58:24
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS--commit-one-governed-file-action
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Store direct replaced_by while archiving predecessor

## Claim checked

Archiving a replaced predecessor stores direct `replaced_by` to an already active successor and derives `replacement_of` only for inverse navigation.

## Test case

Prepare an active successor at version 1 and an active predecessor at version 4, both at global tier `N`, then gather and apply one `MOVE+UPDATE` that adds `replaced_by` to the predecessor and moves it into `archive/`.

## Acceptance criteria

The resulting one-file commit message begins `replaced_by=<successor-file>@1`, records the predecessor path transition and resulting version 5, stores `replaced_by` only on the archived predecessor, stores no `replacement_of`, and derives `replacement_of=<archived-predecessor>@5` when navigating from the successor.

## Failure disposition

Reject the flow if `replaced_by` is absent or derived, `replacement_of` is authored, the successor was not active first, the predecessor remains active, or either carrier stores an inverse backlink.
