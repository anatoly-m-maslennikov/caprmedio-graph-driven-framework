---
identity:
  atom_id: CA-E-647
  ref_id: CA-E-647@14-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure
      Handling
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  tier: 3
relations:
  evaluation_for:
  - CA-M-396
  - CA-M-397
  - CA-M-400
state:
  status: Draft
  version: 14
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-E-647@14-draft-PROGRAMMATIC-DIRECT_POLICY--evaluate-public-operation-error-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/draft/engine-refinement-20261108
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Evaluate public operation error boundaries

## Scope

Every executable PROGRAMMATIC boundary in the image, including Tools, workflows, Apps, MCP endpoints, schedulers and background workers, synchronous or asynchronous.

## Claim

Accept a public boundary only when one shared wrapper or equivalent boundary contract is applied consistently to synchronous and asynchronous entry points and explicitly classifies invalid input or Project-artifact warnings versus real runtime faults, rather than relying on generic RuntimeError inheritance. Input and artifact problems warn technical logs and return a caller-visible error while the healthy runtime component continues; ERROR is reserved for a real blocking runtime fault, which may block the affected component. Cancellation and other control flow remain distinct, callable metadata and the native Tool or MCP contract are preserved, transport response fields may vary when that contract is preserved, and the boundary does not duplicate events, retry silently or create business Journal records. Failure class comes from the structured error type, code and state, never an arbitrary human-message substring. When both restart-required and unavailable categories are declared, ordinary text such as “restart required” does not by itself establish true unavailability.

## Details

- Exercise valid input, malformed input, missing or inconsistent artifacts, cancellation, dependency failure, unexpected runtime failure and diagnostic failure. Submit invalid structured arguments and verify rejection before any effect, with the prior observable result or state preserved.
- Verify sync and async entry points use the same wrapper or equivalent classification, preserve callable metadata and cancellation/control flow, and keep the native contract even when their transport-specific response fields differ.
- Verify technical diagnostics use stdout/stderr at the required level and business lifecycle records remain in the Journal.
- Verify warning-class failures do not terminate the healthy service or runtime component; a genuine runtime fault blocks the affected component and is ERROR.
- Treat generic exception inheritance, missing logging, unsanitized metadata, duplicate emission or unapproved retry as failure. When both restart-required and unavailable categories are declared, pair ordinary error text such as “restart required” with a true unavailable state and confirm that the structured type, code and state—not the message substring—separates them.
