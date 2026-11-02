---
atom_id: CA-P-2289@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Workflow
  depends_on:
  - Requirement
  - Method
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Delivery
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Engineering/Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 7
updated_at: 2026-10-24 08:47:53 +0400
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2290
tier: 3
---
# Summary

Create Requirement-linked test cases

## Objective

Provide a Step that gives every selected Requirement at least one E test case covering its required behavior.

## Details

Read the R, M, E-policy and D projections. Reuse an existing suitable E case instead of duplicating it; otherwise create it through the new authoring Workflow and applicable permission rules. Its admitted content must carry content_role: Evaluation, local_tier: Standard, the currently admitted test-case Type (currently QA Case), and direct relations.evaluation_for containing the selected R identity. Full-Read a reused case and confirm its current eligible state, identity and target relation. For a created case, verify returned identity/current_state/effects and full Readback, then confirm the actual shared-Journal recording. Count coverage only from confirmed eligible non-Draft cases, never proposed data, permission failures, nonempty errors or effect_uncertain results. Reusing a case does not fabricate a creation event or mutation history. Cover each required failure predicate, using positive, failure and boundary cases where meaningful. Prefer stable functional/public-interface and integration boundaries; focused unit tests remain available for pure logic. Save the R-to-E-to-planned-executable-test coverage map, including any uncovered requirement or untestable ambiguity.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Every selected R has at least one verified current Evaluation case with the direct evaluation_for target; all required observable outcomes are covered or explicitly unresolved. New cases are authored and recorded through verified new Tools. Missing/wrong target relations, Draft/proposed cases and failed or uncertain creation results never satisfy coverage or release dependent implementation.

