---
identity:
  atom_id: CA-M-414
  ref_id: CA-M-414
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Observability <+ Logging
    dependencies:
    - MODEL//CAPRMEDIO <+ Journal
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)
    - MODEL//CAPRMEDIO <+ Carrier
    - MODEL//CAPRMEDIO <+ Event Record
  tier: 4
relations:
  child_of:
  - CA-M-415
  DERIVED_FROM:
  - CA-A-053
state:
  status: Active
  version: 17
  updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-414-PROGRAMMATIC-DIRECT_POLICY--emit-structured-operational-diagnostics.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---

## Summary

Emit structured operational diagnostics

## Claim

### Prose Claim

emit structured operational diagnostics for PROGRAMMATIC work under the active
Logging Policy **in** `CAPRMEDIO-GOV-REQU-315`, including its ERROR, WARNING, INFO,
**and** DEBUG meanings. this Method applies that authority **to** PROGRAMMATIC
diagnosis; it does **not** own the level vocabulary, level meanings, **or** Journal
meaning.

## Details


### Applicable when

apply **when** a Tool, App backend service, **or** MCP component reports normal
operation, degraded operation, failure, recovery, **or** diagnostic detail.

### Procedure

1. select ERROR, WARNING, INFO, **or** DEBUG according **to** the active Logging Policy;
   do **not** introduce a fifth shared severity.
   Apply CA-M-396 to failure classification: invalid input or Project
   artifacts produce WARNING diagnostics and an explicit request-output error;
   ERROR is reserved for a genuine blocking failure of the runtime itself.
   A refused request or failed business Workflow is not by itself an ERROR-level
   runtime failure. Preserve partial results under CA-M-405, use the shared
   boundary under CA-M-396, and leave business lifecycle recording with CA-M-399.
2. emit records through one project-owned logging abstraction **and** schema.
   include timestamp, level, component, operation, outcome, **and** the canonical
   action **or** event identity **when** one exists.
3. include actionable, contextual, sanitized fields **and** keep DEBUG bounded **to**
   diagnosable need.
4. materialize sink **and** runtime settings **in** configuration **or** Implementation,
   govern carrier placement **and** encoding through Delivery, **and** preserve actual
   required business-lifecycle evidence through Journal Records **and** diagnostic evidence through
   the applicable production-log Carriers. For the selected Docker runtime, write
   structured technical diagnostics to **stderr** for Docker's local logging driver;
   Project-bound records carry the validated Project prefix from the existing bound
   Project selection and canonical prefix-field validation, never a guessed path,
   container, process or caller identity. Unbound host and service records keep
   their existing host context without a Project prefix; do not invent a binding. This uses the selected immutable settings view; it
   adds no settings carrier and makes no claim of full SettingsReader conformance.
   Configure bounded local rotation as `max-size=10m` and `max-file=3`, with Docker
   logging `mode=non-blocking` and `max-buffer-size=1m`; when that buffer is full,
   new technical messages may be dropped so logging cannot stall primary work.
   Docker logs are removed with the container. Do not create a separate local log
   directory or place technical diagnostics in the business Journal. Operations
   defines the reusable behavior; it does **not** make emitted records O Atoms.
5. declare retention, loss, **and** back-pressure behavior at those bounded
   materialization **and** operational boundaries.
6. make logging failure observable **without** silently breaking primary work.

#### Bounded-scan warnings

When a bounded scan isolates a schema-invalid Atom and continues with a warning,
emit a structured warning through the diagnostic stream configured above with the
validated Project prefix, repository-relative path, and reason, and preserve the
incomplete result (`complete: false`) in the operation response.

### Outcome

Operators can diagnose component behavior **without** exposing secrets, confusing
operational diagnostics with governed Journal history, **or** relying on an
undeclared sink behavior.

### Failure or stop

stop emission **or** release of the affected diagnostic path **when** required context
cannot be sanitized, a logging failure is hidden, **or** the component would use
the Journal as a substitute logging sink.

### Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
