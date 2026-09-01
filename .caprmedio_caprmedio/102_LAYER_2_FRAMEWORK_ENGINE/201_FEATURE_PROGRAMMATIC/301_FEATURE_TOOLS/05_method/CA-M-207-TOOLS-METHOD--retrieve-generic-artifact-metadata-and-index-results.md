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
    - CA-R-1129
    - CA-R-1135
  derived_from:
    - CA-A-058
---
# Retrieve generic Artifact metadata and index results

## Applicable when

Use this Method when framework internals need a body-free metadata view or filtered index of generic Artifacts.

## Procedure

1. Resolve exact Artifacts or a bounded index frontier from stable IDs, paths, or composable structural, layer, Tier, feature, role, subject, lifecycle, and relation filters.
2. Read frontmatter plus path- and filename-derived identity only; never load or return body content.
3. Keep absent requested fields and parse errors explicit instead of applying hidden defaults.
4. Apply filter predicates to normalized metadata and return stable IDs and paths in deterministic order.
5. Mark the output as an internal generic helper result, not a substitute for Content-role-specific Tool semantics.

## Outcome

Callers receive an attributable, deterministic, body-free metadata result for the exact selected Artifact frontier.

## Failure or stop

Return explicit per-carrier errors for malformed metadata and reject unsupported filters or ambiguous exact selectors without mutation.
