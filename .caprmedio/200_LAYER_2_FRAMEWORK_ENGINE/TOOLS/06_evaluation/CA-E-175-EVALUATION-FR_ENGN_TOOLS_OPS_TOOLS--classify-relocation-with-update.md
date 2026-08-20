---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:51:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
---
# Classify relocation with update as MOVE+UPDATE

## Claim checked

One file identity that changes Structural location and also changes content, filename, or other governed carrier state is classified as one `MOVE+UPDATE` change set.

## Test case

Supply a trigger for one identity whose directory and governed content both change in the same working-tree transition.

## Acceptance criteria

The sealed context reports exactly `MOVE+UPDATE`, records both paths and the resulting version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report any split into two actions, missing flag, identity split, or incorrect relation source.
