---
atom_id: CA-E-543@4
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: WORKFLOW_OPERATIONS/RUN_SUPPORT/outcomes
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Journal
  - Evaluation
relations:
  evaluation_for:
  - CA-R-1823
tier: 3
---
# Summary

Verify truthful selected Run terminal outcomes

## Scope

Terminal and recording-pending outcome evidence for actual selected Runs.

## Claim

Selected Run outcomes use the admitted Event Type mapping and never hide a
no-op, cancellation, interruption, failed append, or partial effect.

## Test case

Run focused fixtures for successful effect, successful no-op, confirmed
zero-effect failure, actual authorized cancellation, interrupted pending Run,
and a failure with one performed or uncertain effect.

## Acceptance criteria

- Each actual start has one truthful terminal classification when settled, with
  `Completed`, `Failed`, or `Abandoned` event evidence as applicable; an
  interrupted Run remains pending rather than guessed terminal.
- No-op has no invented Artifact mutation. Confirmed zero-effect failure is
  distinct from partial; each partial case retains its known/uncertain effects.
- Cancellation retains an actual reason/effects and is not emitted for an
  unstarted denial. Safe result/effect references and redaction facts remain
  inspectable without secret material.
- A terminal result reports its actual in-memory terminal/effect outcome even
  with Event ID absent or recording pending; that diagnostic does not invalidate
  completion or authorize replay.

## Details

The fixture supplies explicit effect observations for every failure/cancellation
case; absence of an observation is preserved as uncertainty rather than
classified as confirmed zero effect. The checked assertion is the Claim above.

## Failure disposition

Reject invented Event Types, false completion, erased partial effects, or a
terminal assertion lacking its actual evidence and receipt state.
