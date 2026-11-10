---
identity:
  atom_id: CA-R-3019
  ref_id: CA-R-3019
context:
  container:
    scope_unit: CA-SU-20
  role: Requirement
  form: Rule
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Action
    - MODEL//CAPRMEDIO <+ Package
    - MODEL//CAPRMEDIO <+ Actor/Operator
    - MODEL//CAPRMEDIO <+ Project
    - MODEL//CAPRMEDIO <+ Execution/Workflow Run
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-3019-APPS-RULE--APPS-REQUIREMENT--keep-local-application-lifecycle-bounded-and-observable.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
author: Anatoly Maslennikov
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Keep local application lifecycle bounded and observable

## Claim

### Prose Claim

an admitted local App service **must** expose supervised, bounded, **and** observable startup, shutdown, restart, cancellation, timeout, **and** recovery outcomes for its owned background work.

- the Operator **or** admitted client can distinguish starting, running, stopping, completed, failed, **and** unresolved recovery outcomes **without** inferring success from a disconnected session **or** stopped process.
- interrupted work remains subject **to** that application's declared recovery boundary; restarting the service **must not** silently lose work, duplicate effects, **or** promote transient state **to** MODEL//CAPRMEDIO <+ Project authority.
- unsupported lifecycle capabilities remain explicit rather than being reported as performed. WORKFLOW_ORCHESTRATOR retains its narrower accepted-work **and** handoff rules within its own declared boundary.

this Requirement selects no supervisor implementation, uniform retry policy, permanent server, **or** Workflow for building the application.
