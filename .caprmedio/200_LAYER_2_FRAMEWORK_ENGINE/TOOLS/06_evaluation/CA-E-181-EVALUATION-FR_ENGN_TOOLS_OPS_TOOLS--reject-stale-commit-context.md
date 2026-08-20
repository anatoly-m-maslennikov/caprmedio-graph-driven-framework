---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:57:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Reject stale commit context

## Claim checked

The commit Doer fails closed when the repository state no longer matches the sealed context.

## Test case

Gather one valid `UPDATE` context, advance its Git base or alter one sealed frontier digest, then invoke `COMMIT_CHANGE_SET` in apply mode with the stale envelope.

## Acceptance criteria

The Doer returns a deterministic stale-context diagnostic and creates no index, ref, object-reachability, Journal, or governed-file change.

## Failure disposition

Reject the Doer if it commits, restages, silently refreshes, or partially applies the stale context.
