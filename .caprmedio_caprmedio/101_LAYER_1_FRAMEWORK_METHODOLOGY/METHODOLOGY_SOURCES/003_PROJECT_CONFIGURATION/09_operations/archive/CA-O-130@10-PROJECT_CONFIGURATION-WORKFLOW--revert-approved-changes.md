---
atom_id: CA-O-130@10
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Revert Changes Workflow
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 10
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-132
  - CA-R-1525
  - CA-R-1720
  - CA-R-1643
tier: 3
---
# Summary

Revert approved changes

## Operation

Revert Changes **means** the reusable Workflow graph whose entry **and** only node is CA-O-132.

The graph has no next-Step ON_RESULT edges **and** no retry loop. the node's result selects one terminal outcome:

| From Step | Result condition | Terminal outcome |
| --- | --- | --- |
| CA-O-132 | reverted | completed |
| CA-O-132 | no_op | completed_no_op |
| CA-O-132 | blocked | blocked |
| CA-O-132 | failed or partial_failure | failed |
| CA-O-132 | canceled | canceled |
| CA-O-132 | recording_blocked | recording_blocked |

`recording_blocked` is reserved for missing or uncertain independently required durable Run/effect evidence; a Journal append failure alone yields `recording_error` and does not alter the actual outcome.

## Details

CA-O-132 owns the invocation binding; its referenced Action owns reversal behavior. admission **and** recovery retain exact Workflow/Step/Action Revisions under CA-R-1525. an unavailable **or** changed definition blocks further dispatch pending recorded revalidation; completed effects **and** original bindings remain historical evidence, **not** permission **to** replay.

Every actual Workflow Run, including admission failure, cancellation, successful no-op **and** partial failure, retains its distinct Run identity, definition Revision, parent lineage **when** applicable, input references, start, terminal outcome, result **and** actual effect/evidence references **in** the one authoritative Project Journal. this Journal append is a provenance obligation, not a dispatch gate. use CA-D-340's registered Carrier **and** CA-R-1643's admitted Event Types: Started for start, Completed for successful completion/no-op, Failed for failure, Interrupted for a blocked Run **and** Abandoned for cancellation. these terminal outcome names are **not** new Event Type values.

An unconfirmed Workflow start append does not by itself block dispatch of CA-O-132 when admission, permissions **and** target preconditions pass; retain the attempted event as a `recording_error` diagnostic with pending evidence, **without** inventing an uninvoked Action Run. completion requires independently confirmed durable Run/effect evidence, including the invoked Action Run **and** Step lineage. a Journal append failure alone preserves the actual outcome/effects and does not become `recording_blocked`; recover the missing append **without** replaying reversal effects. no fictitious Artifact change is recorded for no-op, **and** no secret enters the Journal. Artifact Change Log **and** Process Log remain derived views of the same canonical events.
