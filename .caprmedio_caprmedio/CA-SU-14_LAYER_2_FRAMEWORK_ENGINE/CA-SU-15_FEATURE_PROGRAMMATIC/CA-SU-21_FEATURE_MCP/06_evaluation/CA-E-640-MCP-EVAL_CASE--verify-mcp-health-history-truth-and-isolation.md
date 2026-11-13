---
atom_id: CA-E-640
ref_id: CA-E-640
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status
    Presentation
tier: 5
relations:
  evaluation_for:
  - CA-R-2446
status: active
version: 16
updated_at: '2026-11-12T17:04:45.745146+00:00'
carrier_destination:
  file:
    name: CA-E-640-MCP-EVAL_CASE--verify-mcp-health-history-truth-and-isolation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Verify MCP health history truth and isolation

## Claim

### Prose Claim

Accept the health increment only when isolated functional checks demonstrate preserved machine readiness, truthful bounded Tool/Workflow observations, escaped safe HTML and no diagnostic-GET execution effects. A green gateway check or scheduler success alone is not functional Tool/Workflow acceptance.

## Details

### Scope

The changed MCP health route, bounded Gateway observer and HTML representation under CA-R-2446.

- Use disposable independent Project fixtures and an isolated ASGI app or distinct nonproduction listener/state; never the production MCP port or mutable live Atoms as oracle.
- Verify default/JSON/* Accept keeps the ready-boolean shape and 200/503 semantics; explicit HTML has the same readiness status; missing/dead generation is 503; hostile Host/Origin retains 421/403 and causes no Tool/reload effects.
- Exercise real Gateway routing for returned, rejected, failed, partial and uncertain observations with no replay. Unknown or unobserved outcomes are explicit. Verify typed lifecycle outcomes for completed, awaiting correction, canceled, failed or blocked, and partial work. A returned RPC alone does not establish successful execution.
- Verify known Workflow identities and separate scheduler_status from actual outcome/disposition, including scheduler SUCCESS with interrupted_pending or unknown. Health reads do not poll DBOS/Docker, invoke providers, replay calls or change records.
- Overflow both histories: at most 32 observations each, deterministic eviction, bounded fields, concurrent-call isolation, since-start scope and restart reset; make no cross-process completeness claim.
- Inject hostile names, diagnostics, credential-like arguments and path-bearing provider exceptions. HTML must escape them and expose only admitted safe fields/error categories, with no raw arguments/results/secrets/paths/provider messages; healthy and failed views use one snapshot contract.
- Retain exact candidate/fixture bindings and actual outcomes. Focused passes do not replace normal local-release gates or prove installed adoption; verify the installed page after authorized release.
