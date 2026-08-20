---
subject_scopes:
  - feature-boundary
version: 2
updated_at: 2026-08-20 19:24:34
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Commit one governed file action

`COMMIT_FILE_ACTION` must be one Doer Tool owned immediately by `OPS_TOOLS`. It accepts either one sealed `COMMIT_CONTEXT` envelope or one Hook trigger and, when only a trigger is supplied, invokes the same context-gathering logic internally. Dry-run returns the resolved `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set, exact affected file identity, complete typed upstream relation set, canonical commit message, and validation results without changing Git state. Apply must reject stale or incomplete context, unresolved relations, non-current versions, more than one affected file identity, or unrelated staged changes; stage only the affected file change set; create exactly one commit with the canonical message; and verify the resulting commit. A rename contributes `UPDATE`; a Structural-location change contributes `MOVE`; and both together produce `MOVE+UPDATE`. The Doer commits an already-produced file change and must not edit governed file content or create backup copies.
