---
atom_id: CA-M-325@12
ref_id: CA-M-325@12
container:
  scope_unit: CA-SU-2
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Carrier
tier: 3
status: Archived
version: 12
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-325@12-WORKFLOW_ORCHESTRATOR-ENG_DECISION--execute-agent-proposals-in-an-isolated-service.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

execute Agent proposals **in** an isolated service

## Scope

the worker's replaceable Agent adapter **in** the Docker runtime.

## Claim

execute an Agentic Action by sending its bound context **to** the private Agent service **and** admitting the returned proposal through the existing worker boundary.

## Details

- use a bounded JSON request carrying context, check **or** fix phase **and** timeout; admit the existing AgentOutput schema.
- provide **only** the compiled context, not Project mounts. run Codex CLI **in** a fresh dispatch directory with no inherited user configuration **or** MCP registrations.
- the dedicated Agent container provides outer isolation; the CLI can use external isolation there. native execution retains its read-only CLI sandbox.
- allow **<=1** active Agent request initially. bound request bytes, response bytes **and** execution duration.
- preserve accepted output before effects. transport loss, timeout, invalid output **or** authentication failure interrupts rather than silently retrying.
- seed an absent private runtime authentication cache from an explicitly mounted credential file. do **not** overwrite an existing refreshed cache **or** print its contents.
