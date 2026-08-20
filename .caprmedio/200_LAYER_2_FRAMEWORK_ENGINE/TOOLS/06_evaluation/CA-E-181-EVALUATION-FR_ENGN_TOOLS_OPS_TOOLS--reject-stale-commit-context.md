---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-20 22:10:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Reject stale commit context

## Claim checked

The commit Doer fails closed when the repository state no longer matches the sealed context.

## Test case

Gather one valid `UPDATE` context, advance its Git base or alter one sealed frontier digest, then invoke the complete apply flow with the stale envelope.

## Acceptance criteria

The flow releases any provisional unconsumed lease, returns a deterministic stale-context diagnostic before the first Journal append, and creates no index, ref, object-reachability, Journal, runtime blockage, or governed-file change.

## Failure disposition

Reject the Doer if it commits, restages, silently refreshes, or partially applies the stale context.
