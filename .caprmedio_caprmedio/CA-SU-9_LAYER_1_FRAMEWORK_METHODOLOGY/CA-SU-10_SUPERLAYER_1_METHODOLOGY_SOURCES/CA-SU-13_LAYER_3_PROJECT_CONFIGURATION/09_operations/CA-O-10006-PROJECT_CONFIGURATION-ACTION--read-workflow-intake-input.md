---
identity:
  atom_id: CA-O-10006
  ref_id: CA-O-10006
context:
  container:
    scope_unit: CA-SU-13
  role: Operations
  form: Action
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10006-PROJECT_CONFIGURATION-ACTION--read-workflow-intake-input.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Read Workflow intake input

## Claim scope

One bound Workflow Run and its MCP intake dictionary.

## Claim

### Inputs

The bound Project, Workflow Run, request and MCP intake dictionary.

### Fixed parameters

None.

### Effect

At MCP entry, read the dictionary bound to the Project Run and invocation; when called by a Workflow, read its actual caller-bound dictionary, never the parent MCP query. Validate only that binding and the dictionary envelope. Do not infer, supplement, validate fields or mutate a carrier.

### Outputs

Return the dictionary unchanged. Return an explicit failure if the binding or dictionary envelope is invalid.
