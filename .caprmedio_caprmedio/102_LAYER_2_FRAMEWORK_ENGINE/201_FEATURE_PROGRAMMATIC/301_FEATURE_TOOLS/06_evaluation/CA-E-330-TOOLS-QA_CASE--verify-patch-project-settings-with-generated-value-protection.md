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
    - CA-M-212
---
# Verify patch project settings with generated-value protection

## Claim checked

CA-M-212 changes only approved operator-owned Project Settings keys and rejects generated, unknown, or stale targets.

## Applicable when

Apply whenever the Project Settings schema, ownership classification, or patch mechanics change.

## Test case

Seal one settings carrier and request changes to one operator-owned key, one generated key, and one unknown key. Observe rejection, then apply only the operator-owned change and compare every key and byte-level diff.

## Acceptance criteria

The mixed patch changes nothing and identifies both prohibited keys; the valid patch changes exactly the approved key, preserves all unrelated and generated values, remains schema-valid, and has no undeclared diff.

## Failure disposition

Reject the realization and preserve schema, ownership map, requested operations, dry-run diff, final carrier, and undeclared-change comparison.
