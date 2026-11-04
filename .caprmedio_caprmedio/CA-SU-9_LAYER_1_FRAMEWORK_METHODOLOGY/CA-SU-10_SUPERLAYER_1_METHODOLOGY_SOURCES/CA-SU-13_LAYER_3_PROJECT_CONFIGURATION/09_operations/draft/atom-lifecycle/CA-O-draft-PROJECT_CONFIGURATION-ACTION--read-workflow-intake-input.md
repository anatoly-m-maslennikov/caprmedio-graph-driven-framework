---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-04 22:27:14 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
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

Read the intake dictionary supplied with the bound MCP request. Do not infer, supplement or read input from another Project, Run, request, file, environment or historical context.

Validate the Project and Run binding and validate the dictionary against the receiving Workflow's declared input fields. The Action does not ask for additional input or mutate a carrier.

### Outputs

Return the validated intake dictionary unchanged. On failure, return the explicit error and actual completed results under [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md).
