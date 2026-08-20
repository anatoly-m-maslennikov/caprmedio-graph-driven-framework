---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 20:02:00
relations:
  check_of:
    - CA-D-006-DELIVERY-FR_ENGN_TOOLS_OPS_TOOLS--deliver-project-local-commit-automation
---
# Preserve existing Hook behavior

## Claim checked

Installing and removing the project-local commit Hook preserves pre-existing repository Hook behavior.

## Test case

Prepare a repository with one existing executable Hook that records a sentinel, install the OPS_TOOLS Hook adapter, invoke the boundary once, remove the adapter, and invoke the boundary again.

## Acceptance criteria

The existing Hook records its sentinel during both invocations, the installed invocation also emits exactly one `COMMIT_TRIGGER`, and removal restores the pre-install carrier bytes and executable mode.

## Failure disposition

Reject delivery if existing behavior is skipped, duplicated, reordered incompatibly, overwritten, or not restored byte-for-byte.
