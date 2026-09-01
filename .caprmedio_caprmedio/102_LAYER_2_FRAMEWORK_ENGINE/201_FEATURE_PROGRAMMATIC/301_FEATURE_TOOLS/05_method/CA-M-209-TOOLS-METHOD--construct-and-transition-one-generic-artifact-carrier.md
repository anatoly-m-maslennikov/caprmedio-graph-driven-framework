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
    - CA-R-1132
    - CA-R-1133
    - CA-R-1134
  derived_from:
    - CA-A-058
---
# Construct and transition one generic Artifact carrier

## Applicable when

Use this Method when a Content-role-specific Tool delegates generic carrier construction, rename, or registered lifecycle-transition mechanics.

## Procedure

1. Accept exactly one declared operation: construct a new carrier, rename an existing carrier, or execute one registered lifecycle transition.
2. For construction, derive the ID, canonical filename, destination, metadata, and body and reject every overwrite or identity collision.
3. For rename, validate active grammar, compute all direct-reference rewrites, and preserve an explicit old-to-new path map.
4. For lifecycle transition, require a registered source-to-destination transition, create its destination directory lazily, and update required metadata and references.
5. Seal all affected carriers, expose the complete transaction plan, then apply and verify it as one rollbackable unit only under a governing public Tool.

## Outcome

One generic carrier operation completes with valid identity, references, placement, and lifecycle, or leaves the repository unchanged.

## Failure or stop

Reject mixed operations, undefined lifecycle transitions, collisions, ambiguous references, stale carriers, and requests that treat this helper as public Atom semantics.
