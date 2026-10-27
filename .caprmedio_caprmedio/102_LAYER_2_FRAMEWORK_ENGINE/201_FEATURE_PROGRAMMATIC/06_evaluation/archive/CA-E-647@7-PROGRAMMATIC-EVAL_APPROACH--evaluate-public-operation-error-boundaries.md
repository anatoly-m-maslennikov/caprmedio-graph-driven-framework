---
atom_id: CA-E-647@7
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 10:48:25 +0400
subjects:
  governs: Subject/Engineering/Public Operation Error Boundary
  depends_on:
  - Subject/Engineering/Runtime Failure Classification
  - Subject/Engineering/Operation-Local Failure Containment
relations:
  evaluation_for:
  - CA-M-396
  - CA-M-397
  - CA-M-400
tier: 3
---
# Summary

Evaluate public operation error boundaries

## Scope

Every executable PROGRAMMATIC boundary in the image, including Tools, workflows, Apps, MCP endpoints, schedulers and background workers, synchronous or asynchronous.

## Claim

Accept a public boundary only when one shared wrapper or equivalent boundary contract is applied consistently to synchronous and asynchronous entry points and explicitly classifies invalid input or Project-artifact warnings versus real runtime faults, rather than relying on generic RuntimeError inheritance. Input and artifact problems warn technical logs and return a caller-visible error while the healthy runtime component continues; ERROR is reserved for a real blocking runtime fault, which may block the affected component. Cancellation and other control flow remain distinct, callable metadata and the native Tool or MCP contract are preserved, transport response fields may vary when that contract is preserved, and the boundary does not duplicate events, retry silently or create business Journal records.

## Details

- Exercise valid input, malformed input, missing or inconsistent artifacts, cancellation, dependency failure, unexpected runtime failure and diagnostic failure.
- Verify sync and async entry points use the same wrapper or equivalent classification, preserve callable metadata and cancellation/control flow, and keep the native contract even when their transport-specific response fields differ.
- Verify technical diagnostics use stdout/stderr at the required level and business lifecycle records remain in the Journal.
- Verify warning-class failures do not terminate the healthy service or runtime component; a genuine runtime fault blocks the affected component and is ERROR.
- Treat generic exception inheritance, missing logging, unsanitized metadata, duplicate emission or unapproved retry as failure.
