---
atom_id: CA-R-1809
ref_id: CA-R-1809
role: Requirement
current_scope_unit: WATCH_EXECUTION
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:03 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
form: Rule
tier: 3
container:
  scope_unit: CA-SU-8
carrier_destination:
  file:
    name: CA-R-1809-WATCH_EXECUTION-RULE--wait-for-execution-updates.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-8_TOOL_WATCH_EXECUTION/04_requirement
---
# Summary

Wait for execution updates

## Scope

the WATCH_EXECUTION capability for Tool/WATCH_EXECUTION.

## Claim

the WATCH_EXECUTION Tool **must** return correlated execution updates after a caller's cursor, including completion, failure, interruption, handoff, progress, and evidence-recording changes.

## Details

- implement the methodology Action CA-O-117-PROJECT_CONFIGURATION-ACTION--wait-for-execution-updates.
- accept a supported Run ID, opaque cursor and bounded wait timeout; return a new cursor, updates, current status, timeout state, and full report reference.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
