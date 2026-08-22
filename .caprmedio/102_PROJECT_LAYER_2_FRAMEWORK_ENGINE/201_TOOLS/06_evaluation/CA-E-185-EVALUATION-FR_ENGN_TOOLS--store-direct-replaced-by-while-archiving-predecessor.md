---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 5
updated_at: 2026-08-22 04:39:08
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---
# Store direct replaced_by while archiving predecessor

## Claim checked

Archiving a replaced predecessor declares direct `replaced_by` to an already active successor only in the authoritative Work Journal event and derives `replacement_of` only for inverse navigation.

## Test case

Prepare an active successor at version 1 and an active predecessor at version 4, both at global tier `N`, then gather and apply one `MOVE` that preserves the predecessor's content, filename, frontmatter, and version while moving it into `archive/`. Seal the direct `replaced_by` declaration in that archival Work Journal event.

## Acceptance criteria

The resulting one-file commit message begins `replaced_by=<successor-file>@1`, records the predecessor path transition as version 4 to version 4, stores `replaced_by` only in the archival Work Journal event, stores no replacement relation in either Atom frontmatter, and derives `replacement_of=<archived-predecessor>@4` when navigating from the successor.

## Failure disposition

Reject the flow if `replaced_by` is absent, derived, or stored outside the Work Journal event; if `replacement_of` is authored; if the successor was not active first; if the predecessor remains active; if either Atom carrier stores replacement history; or if the archival `MOVE` changes the predecessor version.
