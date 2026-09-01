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
    - CA-M-214
---
# Verify record one verified release outcome

## Claim checked

CA-M-214 creates a Release Record only for a fully verified successful outcome and records failed attempts only as non-release Ops evidence.

## Applicable when

Apply whenever release outcome recording or release acceptance criteria change.

## Test case

Use the same sealed version and manifest in two attempt fixtures: one missing a required verification result and one containing all passing results with exact revisions, Journal frontier, and canonical Git identity.

## Acceptance criteria

The incomplete attempt produces no Release Record and remains explicit failed-attempt evidence; the complete attempt produces exactly one immutable Release Record binding every required identity, revision, check, evidence, Journal, and Git fact.

## Failure disposition

Reject the realization and preserve both attempt frontiers, criteria, evidence maps, emitted Ops carriers, and duplicate-release scan.
