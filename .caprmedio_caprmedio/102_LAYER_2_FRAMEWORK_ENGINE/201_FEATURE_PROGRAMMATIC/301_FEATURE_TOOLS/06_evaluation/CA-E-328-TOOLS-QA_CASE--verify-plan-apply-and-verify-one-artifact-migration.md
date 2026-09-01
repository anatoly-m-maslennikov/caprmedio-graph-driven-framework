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
    - CA-M-210
---
# Verify plan apply and verify one artifact migration

## Claim checked

CA-M-210 applies only the exact approved unchanged migration plan and proves every carrier, reference, Projection, and Journal postcondition.

## Applicable when

Apply whenever generic Artifact migration planning, execution, or verification changes.

## Test case

Plan a two-carrier migration with one reference rewrite and one affected Projection, approve its digest, then change one source before apply. Observe rejection; restore the source, apply the approved plan, and replay all declared postconditions.

## Acceptance criteria

The stale attempt changes nothing; the valid attempt matches every approved mapping and rewrite, rebuilds the affected Projection, appends attributable Journal evidence, and reports no residual, unexpected, or unmapped state.

## Failure disposition

Reject the migration method and preserve plan digest, precondition mismatch, transaction effects, rollback state, postcondition replay, and discrepancy report.
