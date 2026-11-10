---
atom_id: CA-R-1605
ref_id: CA-R-1605
container:
  scope_unit: CA-SU-20
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
tier: 0
status: Archived
version: 16
updated_at: 2026-11-09 19:30:15 +0400
carrier_destination:
  file:
    name: CA-R-1605@16-APPS-SCOPE_CONTRACT-RULE--coordinate-workflow-runs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
claim_target_scope_unit: APPS
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-1522
---

## Summary

Coordinate Workflow Runs

## Claim

WORKFLOW_ORCHESTRATOR **must** own synchronous **and** asynchronous Workflow Run coordination, including interactive Step suspension, result submission, continuation, recovery, **and** next-Step selection from applicable methodology.

## Details

### Methodology-conforming execution boundary

WORKFLOW_ORCHESTRATOR **must** be the APPS Scope Unit that provides a conforming executor of the applicable methodology Workflow model under CA-R-1519 **and** CA-R-1520.

- for each accepted request, Tools remain realizations of individual methodology Actions under CA-R-1516.
- support Programmatic Actions **and** Agentic Steps. the Operator selects caller-coordinated execution **or** independent execution through an admitted worker adapter. independent execution launches isolated Agents **and** records their admitted results **without** requiring a live main session. caller-coordinated execution returns the Action prompt **and** invocation envelope through MCP. **only** admitted results permit progress; retain coordination state rather than requiring the session **to** remember the procedure.
- applicable Workflow definitions, input bindings, result conditions, **and** continuation rules determine execution. the application **must not** maintain a second independently authored Update-to-Replace rule **or** another Workflow-specific policy.
- the application's RMED specifies its execution behavior; Workflow definitions are governed inputs, **not** a requirement **to** use those Workflows **to** build the application.
- the application implements the methodology conformance requirements. its existence is **not** a backward Demand from FRAMEWORK_METHODOLOGY **to** FRAMEWORK_ENGINE.

The application is one immediate unordered APPS Scope Unit. Its declaration does not install a service **or** replace an existing specialized execution component.
