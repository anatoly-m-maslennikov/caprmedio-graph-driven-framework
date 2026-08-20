---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-20 19:16:25
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
---
# Emit only operational Hook triggers

`COMMIT_TRIGGER` must be one operational Hook unit owned immediately by `OPS_TOOLS`. When a registered repository file-action boundary occurs, the Hook emits only a trigger identifying the repository, event, and observed file-path candidates; it must not classify the action, traverse the graph, gather Doer context, edit or stage files, create commits, write Journals, or perform any other mutation.
