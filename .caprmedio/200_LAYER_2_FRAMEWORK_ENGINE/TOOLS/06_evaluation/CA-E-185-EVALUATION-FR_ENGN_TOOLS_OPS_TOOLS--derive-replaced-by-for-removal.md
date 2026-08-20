---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:01:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Derive replaced_by for removal

## Claim checked

Removal of a replaced file uses the derived inverse `replaced_by` relation from an already committed replacement.

## Test case

Prepare a committed replacement file at version 1 with an authored `replacement_of` edge to an active old file at version 4, then gather and apply removal of the old file.

## Acceptance criteria

The resulting one-file `REMOVE` commit message begins `replaced_by=<replacement-file>@1`, names `<old-file>@4` as affected, and contains no authored inverse backlink in either carrier.

## Failure disposition

Reject the flow if the inverse is absent, inferred without a committed direct edge, persisted as a backlink, or rendered under another relation name.
