---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:54:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Produce equivalent context through both input paths

## Claim checked

Passing a Hook trigger directly to the Doer invokes the same context-gathering behavior as the standalone Finder.

## Test case

For one fixed `UPDATE` fixture, capture the sealed context returned by `COMMIT_CONTEXT`, then pass the original trigger directly to `COMMIT_CHANGE_SET` in dry-run mode and capture its resolved context.

## Acceptance criteria

The two contexts are byte-identical after excluding only envelope transport metadata registered as non-semantic.

## Failure disposition

Reject the flow and report the first divergent semantic field.
