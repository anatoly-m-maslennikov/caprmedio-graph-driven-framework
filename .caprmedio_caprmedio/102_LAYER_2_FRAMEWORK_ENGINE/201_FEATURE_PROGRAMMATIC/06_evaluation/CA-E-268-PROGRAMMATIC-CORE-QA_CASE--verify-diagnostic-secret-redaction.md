---
atom_id: CA-E-268
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - diagnostic-redaction
  depends_on:
    continuant:
      - PROGRAMMATIC
      - Logging Policy
version: 3
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-163
  derived_from:
    - CA-A-053
---
# Verify diagnostic secret redaction

## Claim checked

One PROGRAMMATIC diagnostic path sanitizes a sensitive input before its record
is exposed to the declared sink.

## Applicable conditions

Apply when a diagnostic path could receive sensitive or secret-bearing input.
Paths whose declared inputs contain no such value are not applicable.

## Test case

Supply one secret-bearing input to one declared diagnostic path.

## Acceptance criteria

Pass only when the exposed record retains the diagnostic context while omitting
or irreversibly redacting the secret-bearing value.

## Failure disposition

Stop the diagnostic path and correct its sanitization boundary before release.
