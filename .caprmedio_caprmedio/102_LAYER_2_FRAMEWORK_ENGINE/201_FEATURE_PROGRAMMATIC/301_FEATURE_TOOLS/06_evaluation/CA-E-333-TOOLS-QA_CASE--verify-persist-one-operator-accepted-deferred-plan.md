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
    - CA-M-215
---
# Verify persist one operator-accepted deferred plan

## Claim checked

CA-M-215 persists a deferred Plan only from explicit operator acceptance and preserves one bounded reopenable action without completion claims.

## Applicable when

Apply whenever deferred-Plan capture or reopening metadata changes.

## Test case

Present one assistant suggestion to defer work without operator acceptance, then present the same bounded action with explicit acceptance, session, owning scope, rationale, dependencies, and reopening condition.

## Acceptance criteria

The suggestion creates no Plan; the accepted case creates exactly one Plan with the stated action and all provenance and reopening fields; it contains no implementation, active-work, or completion claim.

## Failure disposition

Reject the realization and preserve suggestion and acceptance inputs, created carrier, relation resolution, and scans for inferred acceptance or completion language.
