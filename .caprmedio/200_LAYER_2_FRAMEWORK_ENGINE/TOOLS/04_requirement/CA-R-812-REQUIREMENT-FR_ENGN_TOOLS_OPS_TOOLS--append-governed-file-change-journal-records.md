---
subject_scopes:
  - provenance
version: 2
updated_at: 2026-08-20 21:24:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
    - CAPRMEDIO-GOV-REQU-340--recover-work-journal-coverage-without-invention
---
# Append governed file-change Journal records

`APPEND_CHANGE_RECORDS` must be one Doer Tool owned immediately by `OPS_TOOLS`. After a mutation-free preflight accepts one sealed `COMMIT_CONTEXT`, dry-run returns the complete ordered structured Journal sidecar record set and predicted partitions without mutation. The set contains exactly one `completed` `governed_file_change` event and, only when the subject has no accepted prior result event and recovery evidence is sufficient, one preceding `recovered` `governed_file_state` baseline whose result the change event names through `previous_result_event`.

Apply appends and fsyncs every sealed record through the generic Work Journal Tool and returns one ordered receipt set containing exactly one receipt per related record. Every record and receipt must carry the context's action identity; stable event identities make an interrupted or repeated apply idempotent across the complete set even when rollover places related records in different Journal segments. The Doer must not stage files, create commits, modify the governed subject change, store a commit-message copy, or admit a baseline whose prior state cannot be recovered without invention.
