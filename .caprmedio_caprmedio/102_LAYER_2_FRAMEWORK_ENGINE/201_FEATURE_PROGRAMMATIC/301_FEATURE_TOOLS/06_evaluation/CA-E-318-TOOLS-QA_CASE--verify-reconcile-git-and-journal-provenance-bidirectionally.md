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
    - CA-M-200
---
# Verify reconcile git and journal provenance bidirectionally

## Claim checked

CA-M-200 detects Git–Journal discrepancies in both directions and recovers only fully evidenced missing Journal events idempotently.

## Applicable when

Apply to any reconciliation release or after a suspected provenance-coverage gap.

## Test case

Create a bounded fixture containing one fully evidenced Git commit without a Journal event, one Journal event with no reachable commit, one duplicate event, and one digest mismatch. Reconcile twice over the unchanged frontier.

## Acceptance criteria

The first run appends exactly one recovered event for the fully evidenced commit and reports the other three discrepancy classes with all governed fields; the second run appends nothing and returns the same remaining discrepancies.

## Failure disposition

Reject the realization and preserve Git and Journal frontiers, matches, recovery evidence, appended lines, remaining discrepancies, and second-run comparison.
