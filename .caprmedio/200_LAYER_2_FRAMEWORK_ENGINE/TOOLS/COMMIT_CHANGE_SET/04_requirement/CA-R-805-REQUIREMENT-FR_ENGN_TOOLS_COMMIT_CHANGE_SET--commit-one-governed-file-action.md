---
subject_scopes:
  - feature-boundary
version: 9
updated_at: 2026-08-21 00:02:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Commit one governed file action

`COMMIT_CHANGE_SET` must own both the end-to-end auto-commit interface and the final Git mutation boundary. Its end-to-end interface accepts one `COMMIT_TRIGGER`, invokes the same deterministic context-gathering logic exposed by `COMMIT_CONTEXT`, passes the sealed context to `APPEND_CHANGE_RECORDS`, and then performs its own commit boundary. This orchestration composes peer Tools without giving the Doer structural ownership over them. Dry-run must execute the same resolution and validation path and return the sealed context, resolved `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set, exact governed subject identity, complete typed upstream relation set, complete structured Journal sidecar record set, predicted partitions, deterministically projected Git message, and validation results without mutation.

For commit-only execution or idempotent retry, the Doer may instead accept one current sealed `COMMIT_CONTEXT`, the complete ordered receipt set, and the live repository-scoped lease token returned by `APPEND_CHANGE_RECORDS`. Before mutation it rejects stale or incomplete context, an absent, incomplete, unrelated, or mismatched receipt set or lease, unresolved relations, non-current versions, more than one governed subject identity, unrelated staged changes, or a changed Git base, and repeats these checks while it owns the lease. It stages exactly the subject change plus every receipt-bound Journal line related to the same action identity, including lines across multiple Journal segment carriers when rollover requires them, and must not stage another record already present in those carriers.

The Doer creates exactly one commit using the canonical renderer over the structured `governed_file_change` event and its referenced previous result, then verifies the subject change, every related sidecar record, projected message, commit tree, and parent Git base before releasing the lease. A rename contributes `UPDATE`; a Structural-location change contributes `MOVE`; and both together produce `MOVE+UPDATE`. If commit creation fails after successful appends, the receipt-bound records and lease state remain available as one observable blocked action for an idempotent retry; a later action must not bypass it until the same action succeeds or an operator explicitly resolves it. The Doer must not edit governed subject content, create backup copies, or release or reassign a failed action silently.
