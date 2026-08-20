---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:52:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
---
# Classify file removal as REMOVE

## Claim checked

Disappearance of one governed file identity from the active carrier address is classified only as `REMOVE`.

## Test case

Supply a trigger whose committed graph contains one governed file identity that is absent from the resulting working and staged graph.

## Acceptance criteria

The sealed context reports `REMOVE`, names the last committed filename and version, and resolves upstream relations from the last committed graph.

## Failure disposition

Reject classification and report any competing change set, resulting-version reference, or incorrect relation source.
