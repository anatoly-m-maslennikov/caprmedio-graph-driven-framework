---
atom_id: CA-E-636
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Implementation/Code/Tool
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Engineering/Execution Control/Failure Handling
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
relations:
  evaluation_for:
  - CA-R-1834
tier: 4
---
# Summary

Verify reversal partial failure and logging diagnostics

## Scope

Functional Project/MCP cases for REVERT_CHANGES effect uncertainty, partial effects, admitted cancellation, actual Run failure and plain Journal logging diagnostics.

## Claim

Every realization **must** retain exact actual effect uncertainty, failure and Run state; only confirmed zero-effect, zero-uncertainty execution failure may be `failed`.

## Details

Inject an execution failure before the first effect with confirmed zero applied and zero uncertain completion: expect `failed`, exact failure evidence, and no inverse/replay. Inject a timeout at the first effect with zero confirmed applied but unknown completion: expect `partial_failure`, an `uncertain` effect, and an explicit remaining boundary. Inject failure after one confirmed effect: expect `partial_failure`, completed/failed/unattempted effects, preserved history/reference evidence, and no automatic compensation.

Inject actual Run-start failure: expect `blocked`, `run_start_failed` and no target effect. Inject actual terminal Run bookkeeping failure after an effect: preserve the independently observed target outcome and exact effect account, report `run_error`, and make no claim of terminal Run persistence. Inject Journal append failure before or after an effect: expect ordinary logging diagnostics, unchanged actual Run/target outcomes and no pending-recording/recovery channel or second effect invocation. Do not require a prior Journal record, chain, canonical receipt, deduplication or logging retry.

For an admitted cancellation at a confirmed safe boundary, execute first through the real exposed MCP route with a Workflow and its dispatched O131 Action, then cancel before the next effect. The result must be `canceled` and non-success; its account must name exact `completed`, `unattempted`, and `uncertain` effects, with no invented completed result. Verify the standalone O131 Action case separately: it has a distinct Action Run identity and no fabricated Workflow or Step parent. Preserve the actual `Abandoned` Run state, actual lineage and exact account; any logging failure is reported honestly, not made into a Journal completion gate. Cancellation must invoke neither automatic rollback nor inverse/replay of completed or uncertain effects. A later continuation may attempt only the recorded `unattempted` effects, and only after fresh exact Operator approval and current target/hash/affected-reference/authority/permission checks admit a new manifest; it must never reuse cancellation or a log entry as that authority.

Acceptance verifies the full MCP result, mutation trace, effect invocation count, preserved provenance, actual Run state and logging diagnostics, not a Journal-proof schema. This is an executable-test specification, not runtime evidence.

### Sources

- CA-R-1834; CA-D-536; CA-D-537; CA-O-130 v1; CA-O-131 v2; CA-O-132 v1.
