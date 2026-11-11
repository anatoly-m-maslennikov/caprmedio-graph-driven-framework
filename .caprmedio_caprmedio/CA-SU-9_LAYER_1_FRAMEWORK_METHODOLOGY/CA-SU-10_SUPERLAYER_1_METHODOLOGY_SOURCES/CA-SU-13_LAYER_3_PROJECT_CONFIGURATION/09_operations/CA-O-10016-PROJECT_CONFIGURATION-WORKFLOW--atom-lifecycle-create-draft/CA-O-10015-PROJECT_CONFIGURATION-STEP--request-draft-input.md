---
identity:
  atom_id: CA-O-10015
  ref_id: CA-O-10015
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
  status: Active
  version: 2
  updated_at: '2026-11-11 17:36:30 +0400'
destination:
  file:
    name: CA-O-10015-PROJECT_CONFIGURATION-STEP--request-draft-input.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10016-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-create-draft
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

The called Action's waiting response or resumed correction dictionary, with its results and warnings. Merge the supplied corrections into the retained caller parameters. A caller can supply only the requested fields and can also correct other caller inputs. Preserve fields the caller omits and retain the internally captured `targetStatus`. Validate the merged input before applying effects.
