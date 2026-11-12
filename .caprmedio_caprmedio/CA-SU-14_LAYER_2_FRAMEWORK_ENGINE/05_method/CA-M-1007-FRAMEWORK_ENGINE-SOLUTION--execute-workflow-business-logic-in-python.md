---
identity:
  atom_id: CA-M-1007
  ref_id: CA-M-1007
context:
  role: method
  form: solution
  container:
    scope_unit: CA-SU-14
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:57:03.818531+00:00'
destination:
  file:
    name: CA-M-1007-FRAMEWORK_ENGINE-SOLUTION--execute-workflow-business-logic-in-python.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
---
## Summary

Execute Workflow business logic in Python

## Claim

### Prose Claim

Author executable business logic and Action order in one Python entry point in the Workflow Atom's Formal Claim. Use descriptive names and named parameters. Bind each Action call to a declared Step and Action. Run reviewed Python from an admitted Workflow revision with typed invocation input and the read data it needs through the Engine interface. Keep effectful I/O in Actions. Derive any execution diagram from the same Workflow logic.

Before dispatch, the Engine binds the Project and the exact Workflow, Step, and Action revisions. It validates invocation input, invokes Actions, and accumulates outcomes and effects. Actions call adapters and recheck the input and source revisions they act on. On Action failure, stop further dispatch and return the failure and recorded effects. Engine components use the internal API. AI Agents use MCP.
