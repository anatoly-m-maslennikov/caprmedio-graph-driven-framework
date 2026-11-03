---
atom_id: CA-O-130
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Workflow//Revert Changes Workflow
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 15
updated_at: 2026-10-27 19:59:46 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-130-PROJECT_CONFIGURATION-WORKFLOW--revert-approved-changes.md
  source_atom_id: CA-O-130
  source_atom_revision: 15
  source_sha256: 6f76dc31b9493cd6d6641332a5e6d9dd8b5cf11083c67a68b3ce0f768bc237f2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Revert approved changes

## Operation

Revert Changes **means** the reusable Workflow graph whose entry **and** only node is CA-O-132.

The graph has no next-Step route **and** no retry loop. the node's result selects one terminal outcome:

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
