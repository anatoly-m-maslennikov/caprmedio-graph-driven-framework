---
atom_id: CA-M-325
ref_id: CA-M-325
container:
  scope_unit: CA-SU-20
role: Method
form: Decision
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
version: 13
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-325@13-APPS-DECISION--execute-agent-proposals-in-an-isolated-service.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---

## Summary

execute Agent proposals **in** an isolated service

## Claim

### Prose Claim

This retained contract applies only when AI-Agent execution is separately admitted. It does not enable that execution or claim that its runtime implementation is present.

execute an Agentic Action by sending its bound context **to** the private Agent service **and** admitting the returned proposal through the existing worker boundary.

## Details

### Scope

the worker's replaceable Agent adapter **in** the Docker runtime.

- use a bounded JSON request carrying context, check **or** fix phase **and** timeout; admit the existing AgentOutput schema.
- provide **only** the compiled context, not Project mounts. run Codex CLI **in** a fresh dispatch directory with no inherited user configuration **or** MCP registrations.
- the dedicated Agent container provides outer isolation; the CLI can use external isolation there. native execution retains its read-only CLI sandbox.
- allow **<=1** active Agent request initially. bound request bytes, response bytes **and** execution duration.
- preserve accepted output before effects. transport loss, timeout, invalid output **or** authentication failure interrupts rather than silently retrying.
- seed an absent private runtime authentication cache from an explicitly mounted credential file. do **not** overwrite an existing refreshed cache **or** print its contents.
