---
subject_scopes:
  - provenance
version: 4
updated_at: 2026-08-20 22:27:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
    - CAPRMEDIO-GOV-REQU-340--recover-work-journal-coverage-without-invention
---
# Append governed file-change Journal records

`APPEND_CHANGE_RECORDS` must be one Doer Tool owned immediately by `OPS_TOOLS`. After a mutation-free preflight accepts one sealed `COMMIT_CONTEXT`, dry-run returns the complete ordered structured Journal sidecar record set, including its `llm_session` object and single `occurred_at`, and predicted partitions without mutation. The set contains exactly one `completed` `governed_file_change` event and, only when the subject has no accepted prior result event and recovery evidence is sufficient, one preceding `recovered` `governed_file_state` baseline whose result the change event names through `previous_result_event`.

Apply acquires one exclusive repository-scoped apply lease for the context action before repeating every stale-context, frontier, identity, LLM-session, occurrence-time, recovery-evidence, Journal, and Git-base preflight. While that lease is active, another auto-commit apply for the same resolved repository must wait without appending a Journal record, staging a file, or changing Git. The Doer then appends and fsyncs every sealed record through the generic Work Journal Tool and returns one ordered receipt set containing exactly one receipt per related record plus the live lease token required by `COMMIT_CHANGE_SET`. Every record and receipt must carry the context's action identity and canonical event digest; stable event identities make an interrupted or repeated apply reuse the same `llm_session` and `occurred_at` and remain idempotent across the complete set even when rollover places related records in different Journal segments. An interruption or failure leaves one observable recoverable blocked action under `.caprmedio_runtime`; the same action may resume, while a different action must not silently replace it. The Doer must not stage files, create commits, modify the governed subject change, copy LLM-session provenance into Atom or Projection carriers, store a commit-message or combined session-string copy, admit a baseline whose prior state cannot be recovered without invention, or release the lease before commit verification or explicit operator resolution.
