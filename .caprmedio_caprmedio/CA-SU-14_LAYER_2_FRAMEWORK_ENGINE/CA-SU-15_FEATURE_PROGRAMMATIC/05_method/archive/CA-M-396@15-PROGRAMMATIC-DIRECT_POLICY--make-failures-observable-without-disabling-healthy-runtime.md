---
identity:
  atom_id: CA-M-396@15
  ref_id: CA-M-396@15
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Failure Handling
  tier: 1
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-M-396@15-PROGRAMMATIC-DIRECT_POLICY--make-failures-observable-without-disabling-healthy-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
