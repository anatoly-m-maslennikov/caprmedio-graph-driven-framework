---
atom_id: CA-O-089
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Action//Implementation Failure Diagnosis
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
version: 17
updated_at: 2026-10-27 19:59:45 +0400
relations: {}
tier: 3
---
# Summary

Diagnose implementation test failures

## Operation

Implementation Failure Diagnosis **means** the Agentic Action that explains failed implementation checks **before** choosing a recovery route.

- inputs: the selected P/Plan item, actual failure output, failing candidate, prepared tests, execution phase, current R/E/D **and** Method bindings, complete relevant inputs, **and** applicable confidence/permission gates.
- inspect the failing assertion, expected behavior, code path, test setup, **and** reproducibility. a failing test alone does **not** prove an implementation defect **or** a missing Method.
- return `expected_initial_failure` **only** **when** a correct prepared test exposes selected behavior **not** implemented yet; retain that test's initial failure evidence. this is normal test-first progress, **not** a failed repair retry **or** a reason **to** invent a corrective Method.
- return `implementation_defect` for incorrect production code **or** `test_implementation_defect` for incorrect executable test code, with evidence, affected work, **and** proposed correction. **every** admitted repair still passes through retry control.
- return `authority_change_required` for incorrect, missing, **or** conflicting governing expected behavior; return `environment_blocker` for unavailable execution prerequisites outside the admitted correction; return `unresolved` **when** evidence **or** confidence is insufficient.
- do **not** modify code, governing Atoms, Status, **or** test expectations. report failures honestly; do **not** relabel an unexplained failure as expected merely **to** proceed.

- accept actual confirmed code-review findings as diagnosis input as well as failed checks; inspect their evidence and classify under the same existing results. Do not fabricate test failures or classify unfinished review as a defect. Preliminary pending checks cannot be an accepted-candidate claim.

## Details
