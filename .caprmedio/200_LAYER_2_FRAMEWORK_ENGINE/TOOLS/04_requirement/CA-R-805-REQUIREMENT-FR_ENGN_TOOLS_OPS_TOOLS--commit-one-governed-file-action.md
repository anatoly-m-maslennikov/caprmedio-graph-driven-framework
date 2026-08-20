---
subject_scopes:
  - feature-boundary
version: 5
updated_at: 2026-08-20 21:25:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Commit one governed file change set

`COMMIT_CHANGE_SET` must be the second Doer Tool in the `OPS_TOOLS` file-change flow and be exposed through the common Tool interface and project-local runtime. Dry-run returns the resolved `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set, exact governed subject identity, complete typed upstream relation set, structured Journal sidecar record set, predicted partitions, deterministically projected Git message, and validation results without mutation.

Apply accepts one current sealed `COMMIT_CONTEXT` and the complete ordered receipt set from `APPEND_CHANGE_RECORDS`; rejects stale or incomplete context, an absent, incomplete, unrelated, or mismatched receipt set, unresolved relations, non-current versions, more than one governed subject identity, or unrelated staged changes; and stages exactly the subject change plus every receipt-bound Journal line related to the same action identity, including lines across multiple Journal segment carriers when rollover requires them. It must not stage another record already present in those carriers. The Doer creates exactly one commit using the canonical renderer over the structured `governed_file_change` event and its referenced previous result, then verifies the subject change, every related sidecar record, projected message, commit tree, and parent Git base. A rename contributes `UPDATE`; a Structural-location change contributes `MOVE`; and both together produce `MOVE+UPDATE`. If commit creation fails after successful appends, the receipt-bound records remain available for an idempotent retry and must not be appended again. The Doer must not edit governed subject content or create backup copies.
