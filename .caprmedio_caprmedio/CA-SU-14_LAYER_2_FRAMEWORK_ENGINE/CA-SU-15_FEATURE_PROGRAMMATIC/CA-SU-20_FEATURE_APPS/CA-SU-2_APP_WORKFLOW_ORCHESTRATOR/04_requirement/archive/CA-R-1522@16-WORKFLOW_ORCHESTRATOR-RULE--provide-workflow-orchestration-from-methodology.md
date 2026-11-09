---
atom_id: CA-R-1522@16
ref_id: CA-R-1522@16
container:
  scope_unit: CA-SU-2
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action.Execution Kind
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Invocation Context
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - CAPRMEDIO_MODEL <+ Projection/(.Form := Applicable Methodology)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
status: Archived
version: 16
updated_at: 2026-10-27 19:59:57 +0400
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-1522@16-WORKFLOW_ORCHESTRATOR-RULE--provide-workflow-orchestration-from-methodology.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/04_requirement/archive
---
## Summary

Provide Workflow orchestration from methodology

## Claim

### Prose Claim

WORKFLOW_ORCHESTRATOR **must** be the APPS Scope Unit that provides a conforming executor of the applicable methodology Workflow model under CA-R-1519 **and** CA-R-1520.

- the application owns coordination of an accepted request across its Workflow Runs; Tools remain realizations of individual methodology Actions under CA-R-1516.
- support Programmatic Actions **and** Agentic Steps. the Operator selects caller-coordinated execution **or** independent execution through an admitted worker adapter. independent execution launches isolated Agents **and** records their admitted results **without** requiring a live main session. caller-coordinated execution returns the Action prompt **and** invocation envelope through MCP. **only** admitted results permit progress; retain coordination state rather than requiring the session **to** remember the procedure.
- applicable Workflow definitions, input bindings, result conditions, **and** continuation rules determine execution. the application **must not** maintain a second independently authored Update-to-Replace rule **or** another Workflow-specific policy.
- the application's RMED specifies its execution behavior; Workflow definitions are governed inputs, **not** a requirement **to** use those Workflows **to** build the application.
- the application implements the methodology conformance requirements. its existence is **not** a backward Demand from FRAMEWORK_METHODOLOGY **to** FRAMEWORK_ENGINE.

The application is one immediate unordered APPS Scope Unit. Its declaration does not install a service **or** replace an existing specialized execution component.
