---
atom_id: CA-P-2290@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Workflow
  depends_on:
  - Requirement
  - Method
  - Evaluation
  - Delivery
  - Tool
  - Subject/Domain/Node/Continuant/Projection
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 3
updated_at: 2026-10-24 06:12:43 +0400
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2291
tier: 3
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

