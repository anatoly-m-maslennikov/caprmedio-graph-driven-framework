---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-205
---
# Verify reconcile work journal coverage from sealed evidence

## Claim checked

CA-M-205 recovers missing Journal coverage only when sealed evidence supplies every required event fact and does so idempotently.

## Applicable when

Apply whenever Journal coverage recovery logic or required event fields change.

## Test case

Provide two uncovered subject changes: one with complete sealed carrier, commit, Initiative, author, action, revision, digest, and session evidence; the other missing session evidence. Reconcile twice without changing the fixture.

## Acceptance criteria

The first run appends exactly one complete recovered event for the evidenced change and reports the other as blocked; the second run appends nothing; no existing Journal line is edited.

## Failure disposition

Reject the realization and preserve both evidence bundles, coverage decisions, appended event, blocked fields, Journal before-and-after digests, and second-run result.
