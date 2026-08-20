---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-20 19:55:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Keep dry-run mutation-free

## Claim checked

`COMMIT_CHANGE_SET` dry-run returns the complete predicted commit result without changing Git or governed state.

## Test case

Snapshot governed files, runtime outputs, index entries, refs, and object reachability for one valid sealed `UPDATE` context, invoke the Doer in dry-run mode, then repeat every snapshot.

## Acceptance criteria

The result names the exact identity, change set, typed upstream relations, canonical message, and validations, while every captured state remains unchanged and no new reachable commit exists.

## Failure disposition

Reject the Doer and report the first missing prediction or mutation.
