---
subject_scopes:
  - feature-boundary
version: 4
updated_at: 2026-08-20 20:15:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-event
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Commit one governed file change set

`COMMIT_CHANGE_SET` must be the second Doer Tool in the `OPS_TOOLS` file-change flow and be exposed through the common Tool interface and project-local runtime. Dry-run returns the resolved `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set, exact affected file identity, complete typed upstream relation set, canonical commit message, predicted Journal record and partition, and validation results without mutation. Apply accepts one current sealed `COMMIT_CONTEXT` and the verified append receipt from `APPEND_CHANGE_EVENT`; rejects stale or incomplete context, an absent or mismatched receipt, unresolved relations, non-current versions, more than one governed subject identity, or unrelated staged changes; stages exactly the subject change and the one appended Journal record identified by the receipt; creates exactly one commit using the receipt's byte-identical `action_message`; and verifies both changes in the resulting commit. A rename contributes `UPDATE`; a Structural-location change contributes `MOVE`; and both together produce `MOVE+UPDATE`. If commit creation fails after a successful append, the event remains available for an idempotent retry and must not be appended again. The Doer must not edit governed subject content or create backup copies.
