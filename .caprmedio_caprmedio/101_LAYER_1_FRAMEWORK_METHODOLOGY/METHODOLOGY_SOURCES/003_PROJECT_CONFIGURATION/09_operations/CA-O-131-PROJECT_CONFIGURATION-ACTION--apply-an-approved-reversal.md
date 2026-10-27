---
atom_id: CA-O-131
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Approved Change Reversal'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Engineering/Traceability
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
version: 16
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1432
  - CA-R-1464
  - CA-R-1525
  - CA-D-308
  - CA-D-340
tier: 3
---
# Summary

Apply an approved reversal

## Operation

Approved Change Reversal **means** the reusable Programmatic Action that applies **only** an exact Operator-approved reversal of selected previously accepted effects, preserving required history **and** references. it is **not** internal failure rollback, a version-control reset **or** deletion of historical evidence.

1. resolve the caller's complete reversal packet: selected accepted change/event/Revision references **and** original before/after evidence; exact target identities, current Carrier/state preconditions **and** affected references; the proposed ordered reversal effects **and** expected resulting state; applicable current authority, identity/status/Carrier rules; the recorded Operator decision admitting those exact effects **and** their recovery/cancellation boundary; executor permissions/capabilities; canonical Journal **and** durable evidence location. an old snapshot, remembered approval, Git availability **or** a prior change's permission is **not** reversal authorization. unavailable selection, evidence, approval **or** supported effect returns blocked **without** target mutation.
2. check the exact current targets **and** affected references against the admitted preconditions before effects **and** on recovery. these conditions bind the expected pre-effect state **or** an explicitly admitted already-satisfied-result/no-op state; no-op does **not** bypass approval, currentness, history **or** reference checks. an unadmitted mismatch, concurrent change, changed governing binding **or** revoked permission blocks further effects; do **not** overwrite intervening work, silently substitute a source Revision **or** invent an alternative inverse. revalidation requires an admitted decision binding remaining effects **and** their compatibility with already completed work.
3. verify that the approved expected result is representable under current authority. preserve required prior Revisions, archives, accepted events **and** referenced identities; do **not** erase **or** rewrite history **to** make the past resemble the requested state. resolve lifecycle transitions from the actual Entity/qualified Atom status model. classify Atom effects under CA-R-1432; retain fixed Summary under CA-R-1464, **and** require approved new-identity replacement **when** needed rather than changing the existing identity's Summary. an admitted replacement reuses CA-O-051's ordered transition/history boundary. do **not** reuse an allocated identity for a different Atom, regress its Version, overwrite preserved prior Revision evidence, **or** invent active replacement-history Relations. an unresolved required reference, unsupported transition **or** unapproved dependent effect blocks the affected reversal.
4. when current state already satisfies the entire exact approved result **and** its reference/history conditions, return no_op with the observed evidence **and** zero applied effects. otherwise apply the admitted ordered effects through available governed capabilities, guarding each effect's current preconditions **and** retaining its actual before/after/result evidence. preserve **or** perform **only** approved affected-reference changes; inability **to** preserve a required reference is a blocker, **not** permission **to** delete it. cancellation **or** a failure stops unperformed work at the admitted safe boundary; preserve the exact completed, failed, unattempted **and** uncertain effects. no blind retry, automatic inverse of partial effects **or** widened repair is permitted.
5. return the exact selection/approval/currentness bindings, expected **and** observed result, actual effect account, history/reference disposition, durable evidence references **and** one outcome below. a recovered continuation reconciles independently retained Run/effect evidence **and** observed state **to** this same work before dispatch; it resumes **only** admitted unperformed effects **and** never reports an uncertain effect as absent **or** reapplies a completed effect.

## Details

### Outcomes

| Condition | Outcome and retained evidence |
| --- | --- |
| all selected approved effects and required preservation conditions are actually satisfied, with complete durable Run/effect evidence | reverted, with exact resulting-state and history/reference evidence |
| the complete exact approved result already holds, with complete durable Run evidence and no applied effect | no_op, with zero-change observation; no fictitious mutation |
| authority, approval, identity, currentness, reference, capability or required input is unresolved before further effects | blocked, with the exact missing decision/precondition and any completed effects; no completion claim |
| execution fails with established zero applied effects **and** zero uncertain effect completion | failed, with actual failure **and** evidence establishing zero applied effects **and** no uncertain completion |
| execution fails after **>=1** established applied effect, **or** **any** effect completion is uncertain, including **when** zero applied effects are confirmed | partial_failure, with completed/failed/unattempted/uncertain effects and the exact remaining boundary |
| the admitted cancellation is applied | canceled, with cancellation evidence, actual partial effects if any and unperformed remainder; not successful reversal |
| required independent durable Run/effect evidence is missing or uncertain | recording_blocked, with known execution outcome/effects and pending evidence; a Journal append failure alone is a `recording_error` diagnostic and does not change the actual outcome |

These outcomes do **not** authorize a new repair, broader reversal **or** automatic retry. a partial result remains incomplete even **when** some requested state has been restored. the caller/Operator resolves blocked remaining work **and** any new approval; internal rollback remains a separate admitted failure-recovery capability, **not** a substitute for this requested reversal.

### Every Action Run and durable handoff

Every actual Action execution receives a distinct Action Run identity **and** retains its exact Action definition Revision, Actor, input/approval references, start, terminal outcome, result **and** actual change/evidence references **in** the canonical Project Journal. nested invocation also retains its parent Workflow Run **and** Step Run; standalone invocation records no invented parent. admission failure, no-op, partial failure **and** cancellation are executions with their own evidence, **not** unrecorded exceptions.

Use admitted CA-R-1643 Event Types **and** CA-D-340 serialization: Started, Completed for reverted/no_op, Failed for failed/partial_failure, Interrupted for blocked **and** Abandoned for canceled. preserve actual timestamps **and** canonical event identities, append records under CA-D-308, **and** include no secrets. retain exact definition/current-state bindings under CA-R-1525; execution evidence **and** history are not independently maintained Artifact/Process logs.

Before target effects, require the admitted evidence-preservation capability **and** a mechanism that can establish independent start/effect evidence; a Journal append is not a mutation gate. if the Journal append fails, retain the actual outcome/effects and emit a `recording_error` diagnostic with pending append evidence; only missing or uncertain independent durable Run/effect evidence yields `recording_blocked`. a later explicit append may resubmit the supplied event observation; repeated supplied observations remain distinct append attempts, and normal I/O diagnostics report append failures, without a deduplication or receipt-check gate; independent effect evidence is reconciled separately. recover the append **without** repeating effects. the handoff names exact remaining work **and** evidence uncertainty; only confirmed canonical receipts establish that the Run was journaled.
