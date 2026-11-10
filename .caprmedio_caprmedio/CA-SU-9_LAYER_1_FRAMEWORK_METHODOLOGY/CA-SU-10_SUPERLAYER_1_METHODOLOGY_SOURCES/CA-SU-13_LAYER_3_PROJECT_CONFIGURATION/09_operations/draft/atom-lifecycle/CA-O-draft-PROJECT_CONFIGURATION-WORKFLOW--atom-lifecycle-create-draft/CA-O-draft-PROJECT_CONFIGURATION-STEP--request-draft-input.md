---
atom_id: CA-O-draft
role: Operations
form: Step
status: Draft
version: 1
updated_at: '2026-11-05 18:54:16 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Step
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Request Draft input

## Claim scope

One correction-input binding within [Atom Lifecycle_Create Draft](../CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Input.

### Inputs

Accumulated `parameters`, `requested_input`, intermediate results, warnings, `projectContext`, and the bound Workflow Run and current Step.

### Fixed parameters

None.

### Runs

The Action [Present intermediate results and request input](../CA-O-draft-PROJECT_CONFIGURATION-ACTION--present-intermediate-results-and-request-input.md).

### Outputs

The called Action's waiting response or resumed correction dictionary, with its results and warnings. Merge a resumed dictionary only into fields named in `requested_input`; preserve all other caller parameters. The captured `targetStatus` cannot be replaced by corrections.
