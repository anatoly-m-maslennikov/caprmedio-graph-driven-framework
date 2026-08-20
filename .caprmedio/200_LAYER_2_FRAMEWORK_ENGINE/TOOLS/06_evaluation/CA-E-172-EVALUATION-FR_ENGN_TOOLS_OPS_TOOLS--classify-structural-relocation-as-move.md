---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:48:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
---
# Classify structural relocation as MOVE

## Claim checked

Relocation of one unchanged governed file identity to a different Structural location is classified only as `MOVE`.

## Test case

Supply a trigger for one identity whose directory changes while filename, content, governed carrier state, and version remain unchanged.

## Acceptance criteria

The sealed context reports `MOVE`, preserves the version, records both repository-relative paths, and resolves upstream relations from the unchanged Artifact graph.

## Failure disposition

Reject classification and report any added `UPDATE` flag, version change, or incorrect relation source.
