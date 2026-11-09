---
atom_id: CA-M-322
ref_id: CA-M-322
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Active
version: 14
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-322-MCP-DECISION--reload-through-isolated-implementation-generations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Reload through isolated implementation generations

## Claim

### Prose Claim

MCP hot reload is optional and disabled by default. Default startup serves tool implementations in the MCP process, without an implementation child. Apply code changes with a normal server/container restart. Only explicit opt-in enables isolated implementation generations and their existing validated switch behavior.

## Details

### Scope

server-side hot reload for the Project-local MCP gateway.

The following generation rules apply only when hot reload is explicitly enabled. When disabled, there is no implementation generation to replace or drain; preserve the same Project boundary, transport protections and callable tools. Do not advertise a working reload action in disabled mode.

1. keep the stdio gateway, protocol session, reload control **and** fixed Project binding stable.
2. load candidate code **and** dependencies in a separate local implementation process, rather than mutating live imported modules with importlib.reload.
3. initialize the candidate without starting Workflows, workers **or** source mutations; obtain its complete Tool contracts **and** validate names, schemas **and** the fixed Project binding.
4. switch new dispatch to the candidate **only** after validation succeeds; preserve the old generation for admitted calls.
5. drain retired generations **after** their admitted calls finish; expose a bounded drain failure rather than silently terminating uncertain effects.
6. when preparation fails, discard the candidate **and** keep the current generation. when a published generation later fails, report affected calls honestly; never replay a mutating call automatically.
7. serialize reload requests **and** suppress duplicate request IDs; an unchanged implementation frontier is a no-op.
