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
    - CA-M-209
---
# Verify construct and transition one generic artifact carrier

## Claim checked

CA-M-209 executes exactly one declared generic carrier operation as a complete rollbackable transaction under a governing public Tool.

## Applicable when

Apply whenever generic construction, rename, or lifecycle-transition mechanics change.

## Test case

Prepare one active Artifact with two incoming references. Request a registered lifecycle transition while also requesting a rename in the same operation; observe rejection. Then request only the lifecycle transition and inspect destination, metadata, references, source, and transaction residue.

## Acceptance criteria

The mixed operation changes nothing; the single transition reaches the registered destination, removes the source, updates both references and required metadata, preserves identity, and leaves no partial or temporary state.

## Failure disposition

Reject the realization and preserve requested operation set, transition registry entry, source and destination states, reference map, and rollback evidence.
