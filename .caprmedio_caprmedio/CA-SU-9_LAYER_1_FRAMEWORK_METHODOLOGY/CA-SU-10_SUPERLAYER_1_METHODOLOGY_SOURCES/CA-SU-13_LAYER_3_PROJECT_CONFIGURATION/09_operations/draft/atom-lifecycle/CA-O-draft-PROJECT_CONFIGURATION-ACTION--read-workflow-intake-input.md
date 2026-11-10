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

At MCP entry, read the dictionary bound to the Project Run and invocation; when called by a Workflow, read its actual caller-bound dictionary, never the parent MCP query. Validate only that binding and the dictionary envelope. Do not infer, supplement, validate fields or mutate a carrier.

### Outputs

Return the dictionary unchanged. [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--govern-atom-lifecycle-identity-and-version.md) governs failures.
