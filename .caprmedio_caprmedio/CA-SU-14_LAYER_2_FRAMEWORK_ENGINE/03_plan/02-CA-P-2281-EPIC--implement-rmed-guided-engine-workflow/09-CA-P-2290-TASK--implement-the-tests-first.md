---
atom_id: CA-P-2290
ref_id: CA-P-2290
container:
  atom: CA-P-2281
role: Plan
form: Plan
label: Task
topics:
  main_subject: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
  dependencies:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Implementation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2291
status: Active
version: 10
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 9-CA-P-2290-TASK--implement-the-tests-first.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/2-CA-P-2281-EPIC--implement-an-rmed-guided-engine-workflow
work_sequence_number: 9
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
---
# Summary

Implement the tests first

## Objective

Provide a Step that implements the agreed E test cases using the applicable M and D projections before Requirement implementation.

## Details

Give its fresh subagent the R projection, E policies/cases, compiled Ms and Ds. Build source-authored golden fixtures and functional/integration tests at useful real boundaries. Mock external dependencies or controlled inputs, not the target Implementation itself. Verify that the tests run and distinguish a genuine unmet Requirement from a broken harness; existing correct behavior may already pass. Report projection defects and missing test inputs immediately. Split large implementation work into bounded P Tasks only when needed, with disjoint file ownership.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Executable tests match the E cases and coverage map; their baseline outcomes and harness validity are recorded without claiming an expected baseline failure is completed implementation.

