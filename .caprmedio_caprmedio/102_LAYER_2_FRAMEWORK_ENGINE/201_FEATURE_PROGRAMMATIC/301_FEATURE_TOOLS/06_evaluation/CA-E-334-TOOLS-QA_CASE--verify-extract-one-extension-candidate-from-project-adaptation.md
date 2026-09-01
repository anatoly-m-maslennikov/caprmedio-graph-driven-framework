---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-216
---
# Verify extract one extension candidate from project adaptation

## Claim checked

CA-M-216 extracts one independently identified Extension candidate with a complete attributable reusable dependency boundary.

## Applicable when

Apply whenever Project Adaptation extraction or dependency-closure rules change.

## Test case

Select two reusable adaptation Atoms whose closure includes one reusable dependency, one declared external dependency, one project setting, one secret reference, and one unresolved required dependency. Extract, then resolve the missing dependency and repeat.

## Acceptance criteria

The unresolved attempt produces no candidate; the resolved attempt includes selected Atoms and reusable closure with exact revisions, declares the external dependency, excludes settings and secrets, and has one stable candidate identity.

## Failure disposition

Reject the extraction method and preserve selection, closure graph, exclusions, unresolved dependencies, source revisions, and emitted candidate manifest.
