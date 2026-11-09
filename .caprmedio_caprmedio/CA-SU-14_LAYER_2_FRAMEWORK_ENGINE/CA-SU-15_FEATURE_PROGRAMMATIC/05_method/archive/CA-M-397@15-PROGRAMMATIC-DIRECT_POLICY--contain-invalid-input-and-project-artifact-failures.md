---
identity:
  atom_id: CA-M-397@15
  ref_id: CA-M-397@15
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Failure Handling
  tier: 2
relations:
  child_of:
  - CA-M-396
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-397@15-PROGRAMMATIC-DIRECT_POLICY--contain-invalid-input-and-project-artifact-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Contain invalid input and Project artifact failures

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Handle invalid input and Project artifact problems as operation-local failures: report an attributable error in the Tool, MCP or other caller-visible output, emit a sanitized technical WARNING, and keep the runtime available. Classify each failure by the structured error type, code and state defined by the applicable contract; never classify it from an arbitrary human-message substring.

## Details

1. Apply this classification to invalid requests and malformed, missing, stale, ambiguous or otherwise unusable Project artifacts and bindings. Technical ERROR severity is not permitted for these conditions, even when the affected operation cannot proceed. Validate invalid arguments before any effect and preserve the prior observable state when validation rejects them.
2. Give the response a stable error code, a safe explanation and the affected logical target or safe Project-relative path when known. A warning in logs alone is not an error answer; do not rely on exception text or logs as the only output. Human-readable text such as “restart required” is explanatory only; it does not establish a true unavailable state or another failure class without the structured type, code and state.
3. Reject unsafe or unauthorized effects at their applicable boundary. Continue only independently safe and authorized work; never select a substitute Project, repair input, bypass a guard or retry as an implicit error-handling policy.
4. Use the error/diagnostic structure of the applicable public result contract without discarding completed data. CA-M-398 governs partial-result presentation; result errors do not determine log severity.
5. Use the runtime-only blocking/ERROR distinction in CA-M-396. Return even an all-invalid result as an explicit failed or incomplete request outcome, not a crashed service or a false successful empty result.
