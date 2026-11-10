---
identity:
  atom_id: CA-M-396
  ref_id: CA-M-396@16
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Failure Handling
  tier: 2
state:
  status: Archived
  version: 16
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-M-396@16-PROGRAMMATIC-DIRECT_POLICY--make-failures-observable-without-disabling-healthy-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-397
  - CA-M-400
  child_of:
  - CA-M-403
---

## Summary

Make failures observable without disabling healthy runtime

## Claim

### Prose Claim

Classify each observed failure by its actual impact, expose it through the affected operation's output or runtime failure boundary, and keep a healthy runtime available. Reserve blocking runtime failure and technical ERROR severity for a genuine failure of the runtime itself.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

1. Do not swallow exceptions, erase diagnostic errors, turn a failed result into empty success, or use an unobservable catch-and-continue path. If diagnostic emission fails, report that failure through a still-usable output without hiding the primary outcome.
2. Separate an error reported to the requester from a technical log level. A request can fail, or be partially completed, while its technical diagnostic is WARNING and the runtime remains healthy.
3. Invalid input and invalid, missing, stale or ambiguous Project artifacts do not become runtime failures because an exception is named RuntimeError, a request is rejected, or no valid result is available.
4. Only an actual runtime failure that prevents the affected runtime component from safely operating may use ERROR severity and block that component. Attribute and report the real runtime failure; do not invent a runtime fault to escalate a Project-data problem.
5. This construction principle does not bypass validation, authorization, source binding or effect safety. Refuse the affected unsafe operation while preserving unrelated runtime availability.

### Retained invalid-input and artifact controls

Handle invalid input and Project artifact problems as operation-local failures: report an attributable error in the Tool, MCP or other caller-visible output, emit a sanitized technical WARNING, and keep the runtime available. Classify each failure by the structured error type, code and state defined by the applicable contract; never classify it from an arbitrary human-message substring.

#### Details

##### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

1. Apply this classification to invalid requests and malformed, missing, stale, ambiguous or otherwise unusable Project artifacts and bindings. Technical ERROR severity is not permitted for these conditions, even when the affected operation cannot proceed. Validate invalid arguments before any effect and preserve the prior observable state when validation rejects them.
2. Give the response a stable error code, a safe explanation and the affected logical target or safe Project-relative path when known. A warning in logs alone is not an error answer; do not rely on exception text or logs as the only output. Human-readable text such as “restart required” is explanatory only; it does not establish a true unavailable state or another failure class without the structured type, code and state.
3. Reject unsafe or unauthorized effects at their applicable boundary. Continue only independently safe and authorized work; never select a substitute Project, repair input, bypass a guard or retry as an implicit error-handling policy.
4. Use the error/diagnostic structure of the applicable public result contract without discarding completed data. CA-M-405 governs partial-result presentation; result errors do not determine log severity.
5. Use the runtime-only blocking/ERROR distinction in CA-M-396. Return even an all-invalid result as an explicit failed or incomplete request outcome, not a crashed service or a false successful empty result.

### Retained shared public-boundary controls

Reuse one transport-neutral error-handling owner at public operation boundaries, applying it through a decorator or equivalent shared wrapper rather than duplicating exception classification and logging across Tools, MCP and other callers.

#### Details

##### Scope

PROGRAMMATIC public operation and process execution boundaries, including all first-party Tools, Workflows, Apps, MCP adapters, service entrypoints and background executors shipped in a delivered Docker image. The policy is not limited to AtomSearch, MCP-mediated invocation or a currently running container.

1. The shared boundary classifies known failures, emits the technical diagnostic under CA-M-396/CA-M-399, and uses the caller's declared result/error adapter. It does not invent a competing domain model or force different existing public contracts into an undocumented universal envelope.
2. Support synchronous and asynchronous operations while preserving their callable signature/metadata, await behavior and cancellation. Do not turn cancellation, process shutdown or an interrupt into successful output.
3. The operation owner supplies verified completed data, effects and error context under CA-M-405. Pass already-structured partial or failed outcomes through without erasing their data, duplicating diagnostics or reclassifying a Project artifact as runtime failure.
4. Use explicit failure classification and actual context rather than treating a Python exception base class, including RuntimeError, as proof that the runtime is broken. An unexpected failure must remain visible; never silently return success.
5. Apply the boundary once at the relevant public execution owner, not around every helper. Registration and discovery remain effect-free. Generic handling does not start Workflows, append Journals, retry, repair, roll back or replay business work.
6. Reuse the established shared logger and canonical execution/validation owners. Keep transport-specific response encoding in its adapter and business lifecycle recording with the Workflow executor.
7. Derive the affected runtime coverage from the delivered image entrypoints, executable modes and their actual dispatch owners. Wire the shared handling at those owners so direct invocation, worker execution and service execution do not bypass it. Reuse existing package inventories; do not introduce a competing runtime registry, decorate every helper or modify third-party internals. A verified process-startup/runtime failure may terminate the affected process; a failed request or business Workflow does not imply that the runtime is broken.
