---
identity:
  atom_id: CA-O-10015
  ref_id: CA-O-10015@1
context:
  container:
    atom: CA-O-10016
  role: Operations
  form: Step
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Step
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
relations:
  RUNS:
  - CA-O-10004
state:
  status: Archived
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10015@1-PROJECT_CONFIGURATION-STEP--request-draft-input.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/archived
---
## Summary

Request Draft input

## Claim scope

One correction-input binding within [Atom Lifecycle_Create Draft](../CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft.md).

## Claim

### Kind

Input.

### Inputs

Accumulated `parameters`, `requested_input`, intermediate results, warnings, `projectContext`, and the bound Workflow Run and current Step.

### Fixed parameters

None.

### Runs

The Action [Present intermediate results and request input](../CA-O-10004-PROJECT_CONFIGURATION-ACTION--present-intermediate-results-and-request-input.md).

### Outputs

The called Action's waiting response or resumed correction dictionary, with its results and warnings. Merge a resumed dictionary only into fields named in `requested_input`; preserve all other caller parameters. The captured `targetStatus` cannot be replaced by corrections.
