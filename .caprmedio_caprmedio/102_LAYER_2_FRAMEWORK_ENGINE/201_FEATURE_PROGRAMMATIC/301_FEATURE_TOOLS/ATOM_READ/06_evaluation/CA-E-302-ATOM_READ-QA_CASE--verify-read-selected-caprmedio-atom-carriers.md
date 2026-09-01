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
    - CA-M-184
---
# Verify read selected caprmedio atom carriers

## Claim checked

CA-M-184 resolves exact Atom selectors uniquely and returns faithful requested carrier views without mutation.

## Applicable when

Apply to any ATOM_READ realization before it is accepted as the canonical Atom reader.

## Test case

Use one valid Atom addressed separately by path, filename, stem, and ID, plus one missing selector and one deliberately ambiguous stem. Request content-only, metadata-only, and combined views while recording the source bytes.

## Acceptance criteria

All four valid selectors resolve to the same carrier; returned content equals its body; metadata contains raw frontmatter plus correct derived placement and lifecycle facts; missing and ambiguous selectors remain explicit; source bytes do not change.

## Failure disposition

Reject the realization and preserve each selector, its observed resolution, returned fields, and the source-byte comparison.
