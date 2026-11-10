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
    name: CA-O-draft-PROJECT-STEP--resolve-open-decisions.md
    path: .caprmedio_caprmedio/09_operations/draft/specification-workflows/CA-O-draft-PROJECT-WORKFLOW--review-and-refine-specifications
---

## Summary

Resolve open decisions

## Claim scope

One binding within [Review and Refine Specifications](../CA-O-draft-PROJECT-WORKFLOW--review-and-refine-specifications.md).

## Claim

### Prose Claim

#### Kind

Input.

#### Inputs

`project_root`, bound Workflow Run and current Step, one-entry `requested_input` dictionary, `findings`, intermediate results and warnings; retain original selection, proposals, mapping and accumulated `settled_decisions`.

#### Fixed parameters

None.

#### Runs

The Action [Present intermediate results and request input](../../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/draft/atom-lifecycle/CA-O-draft-PROJECT_CONFIGURATION-ACTION--present-intermediate-results-and-request-input.md).

#### Outputs

Return waiting response or correction dictionary. Merge only the answer to that question into `settled_decisions`; preserve original context, proposals and mapping. Present one unresolved question at a time.
