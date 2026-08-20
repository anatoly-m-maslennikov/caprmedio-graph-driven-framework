---
subject_scopes:
  - feature-boundary
version: 2
updated_at: 2026-08-20 19:38:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
---
# Emit only operational Hook triggers

`COMMIT_TRIGGER` must be one operational Hook unit owned immediately by `OPS_TOOLS`. When a registered repository file-change boundary occurs, the Hook emits only a trigger identifying the repository, event, and observed before-path and after-path candidates; it must not classify the change set, traverse the graph, gather Doer context, edit or stage files, create commits, write Journals, or perform any other mutation.
