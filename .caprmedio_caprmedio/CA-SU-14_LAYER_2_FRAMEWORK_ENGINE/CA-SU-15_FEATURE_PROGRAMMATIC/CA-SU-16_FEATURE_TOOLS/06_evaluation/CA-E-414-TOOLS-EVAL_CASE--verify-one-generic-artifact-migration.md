---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
version: 21
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-R-1140
  - CA-O-033
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-414
ref_id: CA-E-414
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
---
# Verify one generic Artifact migration

## Claim checked

CA-O-033 read-only replays an applied generic migration plan **and** reports **every** residual, unexpected, **and** unmapped state.

## Applicable when

apply whenever generic migration postcondition comparison, evidence attribution, **or** discrepancy classification changes.

## Test case

use one applied migration plan whose current evidence **contains** one residual old identity, one unexpected carrier mutation, **and** one unmapped reference. replay postconditions **and** compare **every** carrier, typed reference, Projection, **and** Work Journal carrier **before** **and** **after** the replay.

## Acceptance criteria

the result separately reports **all** three discrepancies with their attributable evidence. no carrier, reference, Projection, **or** Work Journal evidence changes during verification.

## Failure disposition

reject the realization **and** preserve plan postconditions, observed evidence, discrepancy classifications, digests **or** revisions **before** **and** **after** replay, **and** no-mutation proof.
