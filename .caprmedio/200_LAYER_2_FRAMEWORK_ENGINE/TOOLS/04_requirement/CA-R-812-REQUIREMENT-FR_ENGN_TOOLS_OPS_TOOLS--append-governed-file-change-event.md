---
subject_scopes:
  - provenance
version: 1
updated_at: 2026-08-20 20:14:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
---
# Append the governed file-change event

`APPEND_CHANGE_EVENT` must be one Doer Tool owned immediately by `OPS_TOOLS`. After a mutation-free preflight accepts one sealed `COMMIT_CONTEXT`, dry-run must return the exact predicted Work Journal record and partition without mutation. Apply must create one `completed` event with `kind` equal to `governed_file_change`, the classified action as its operation, and an `action_message` byte-identical to the context's canonical commit message; append it through the generic Work Journal Tool; fsync it; and return the append receipt. Reapplying the same event identity must return the existing receipt without duplicating the event. The Doer must not stage files, create commits, or modify the governed subject change.
