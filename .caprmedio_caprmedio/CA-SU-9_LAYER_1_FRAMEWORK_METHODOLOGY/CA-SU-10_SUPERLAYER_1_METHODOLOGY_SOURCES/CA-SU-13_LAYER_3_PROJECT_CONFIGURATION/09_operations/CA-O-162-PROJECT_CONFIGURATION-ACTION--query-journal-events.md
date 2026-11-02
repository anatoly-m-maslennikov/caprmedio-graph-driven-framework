---
atom_id: CA-O-162
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 19:59:47 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Event
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
relations:
  depends_on:
  - CA-R-1850
tier: 3
---
# Summary

Query Journal Events

## Operation

The Journal Event query Action **must** read one stable snapshot of the selected Project's canonical Events Journal, evaluate only its bounded literal filter grammar, and return Event IDs by default or only caller-selected Event fields or full Events on request.

## Details

The Action consumes the exact pre-dispatch sealed byte-prefix frontier. A
standalone Action captures that frontier before its own Run evidence.

The Action reuses CA-R-1850's one shared literal filter grammar. It neither writes Events nor creates a competing Journal, Projection, SQL interpreter, arbitrary-code evaluator, credential reader, mutation authority, or invented Run. It reports exact malformed, missing, duplicate, incomplete, changed-source, coverage, pagination, and filter diagnostics rather than skipping or passing them.
