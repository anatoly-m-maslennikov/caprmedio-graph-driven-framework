---
atom_id: CA-O-draft
container:
  scope_unit: CA-SU-00
role: Operations
form: Step
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations: {}
status: Draft
version: 1
updated_at: '2026-11-11 00:16:05 +0400'
current_scope_unit: caprmedio
destination:
  file:
    name: CA-O-draft-PROJECT-STEP--apply-lifecycle.md
    path: .caprmedio_caprmedio/09_operations/draft/specification-workflows/CA-O-draft-PROJECT-WORKFLOW--consolidate-specifications
---

## Summary

Apply lifecycle

## Claim scope

One binding within [Consolidate Specifications](../CA-O-draft-PROJECT-WORKFLOW--consolidate-specifications.md).

## Claim

### Prose Claim

#### Kind

Execution.

#### Inputs

`project_root`, exact accepted mapping, settled decisions and authorization; derive an ordered list of individual lifecycle requests, one per affected Atom.

#### Fixed parameters

None.

#### Runs

The Workflow [CA-O-127](../../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-127-PROJECT_CONFIGURATION-WORKFLOW--manage-atom-lifecycle.md).

#### Outputs

For each individual request invoke CA-O-127 once, retain its result, and stop at the first failure. Return completed results and remaining requests; never represent this as a bulk lifecycle call.
