---
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: "Draft"
subjects:
  governs: "Method/External Effect Boundary"
  depends_on:
    - "Method/Effect Authorization"
    - "Method/Effect Boundary"
version: 1
updated_at: "2026-10-21 01:47:52 +0400"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Bound file and subprocess effects

plan, validate, **and** bound **every** PROGRAMMATIC file mutation **or** subprocess
invocation **before** applying it; make partial failure diagnosable **and** recoverable
**without** guessing.

## Details

Candidate source: [CA-M-161](../CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component writes, replaces, **or**
removes a file, **or** invokes a subprocess.

## Procedure

1. validate the target **and** preconditions **before** mutation.
2. write replacement content through a secure temporary carrier on the
   destination filesystem, flush required bytes, **and** use an atomic replacement
   **only** **where** the supported boundary provides that guarantee.
3. invoke a subprocess with an argument array, explicit timeout, checked exit
   status, controlled environment input, **and** shell execution disabled by
   default.
4. return the target, inputs, outcome, **and** partial-failure context needed for
   diagnosis **or** recovery.

## Outcome

**every** applicable effect has a declared precondition, bounded execution
surface, observable result, **and** explicit recovery limit.

## Failure or stop

stop the effect **when** preconditions fail, an atomicity guarantee is unavailable
**and** no weaker recovery boundary is accepted, **or** subprocess completion,
timeout, **and** exit status cannot be observed.

## Sources

- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: `subprocess`](https://docs.python.org/3.14/library/subprocess.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
