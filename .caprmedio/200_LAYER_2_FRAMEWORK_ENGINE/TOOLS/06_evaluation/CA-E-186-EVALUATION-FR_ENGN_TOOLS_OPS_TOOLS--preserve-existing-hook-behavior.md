---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-20 22:24:00
relations:
  check_of:
    - CA-D-006-DELIVERY-FR_ENGN_TOOLS_OPS_TOOLS--deliver-project-local-commit-automation
---
# Preserve existing Hook behavior

## Claim checked

Installing, controlling, and removing the project-local commit adapter preserves pre-existing repository Hook behavior.

## Test case

Prepare a repository with one existing executable Hook that records a sentinel. Run the adapter's install, status, enable, disable, and uninstall operations, invoking the file-change boundary while enabled, while disabled, and after uninstall.

## Acceptance criteria

The existing Hook records its sentinel during every invocation. The enabled adapter emits exactly one `COMMIT_TRIGGER`; the disabled and uninstalled adapter emits none. Status reports each state correctly, uninstall restores the pre-install carrier bytes and executable mode, and no backup carrier is created.

## Failure disposition

Reject delivery if existing behavior is skipped, duplicated, reordered incompatibly, overwritten, or not restored byte-for-byte; if disabled or uninstalled operation emits a trigger; or if installation creates a repository backup copy.
