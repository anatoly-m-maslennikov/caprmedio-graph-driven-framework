---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-864
  derived_from:
    - CA-A-058
---
# Read selected CAPRMEDIO Atom carriers

## Applicable when

Use this Method when a caller needs the current carrier content or metadata of explicitly selected Atoms.

## Procedure

1. Resolve each selector as an exact path, full filename, filename stem, or Atom ID within the configured control root.
2. Require every selector to resolve uniquely; keep missing and ambiguous selectors as explicit per-selector results.
3. Read the selected carrier bytes once and parse the raw frontmatter without rewriting it.
4. Derive identity, placement, Content role, Scope Unit, and lifecycle facts from the current path and filename.
5. Return content, metadata, or both exactly as requested, preserving selector-to-result attribution.
6. Perform no mutation or implicit repair.

## Outcome

Each selector has one attributable read result containing the requested current carrier view or an explicit resolution error.

## Failure or stop

Do not guess when a selector is missing, ambiguous, unreadable, or outside the control root; return the exact condition to the caller.
