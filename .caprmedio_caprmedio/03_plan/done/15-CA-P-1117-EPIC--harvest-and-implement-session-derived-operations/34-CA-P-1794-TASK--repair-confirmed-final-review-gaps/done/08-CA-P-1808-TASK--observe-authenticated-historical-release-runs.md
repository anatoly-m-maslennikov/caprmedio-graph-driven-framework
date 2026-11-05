---
atom_id: CA-P-1808
ref_id: CA-P-1808
container:
  atom: CA-P-1794
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release
  dependencies:
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Action Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Execution Identity/Source Binding
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1794
  relates_to:
  - CA-C-513
  - CA-R-1807
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 8-CA-P-1808-TASK--observe-authenticated-historical-release-runs.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/34-CA-P-1794-TASK--repair-confirmed-final-review-gaps/done
work_sequence_number: 8
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Observe authenticated historical Release Runs

## Objective

repair the read-only Release-host observer so a current-source change does not prevent reading exact authenticated saved Run evidence.

## Details

- preserve the frozen request identity, exact Release route, retained transport binding, namespace and worker availability checks before database access.
- keep current-source guards on dispatch and actual recovery; an observation is not a new admission, grant, replay or status rewrite.
- use bounded regression fixtures and independently review the separation before root checks the actual historical N12 status through MCP.

## Definition of Done

focused tests prove truthful historical observation after source drift, pre-client refusal of foreign or tampered bindings and unchanged strict dispatch/recovery guards; independent review accepts the change and the live N12 observer returns its actual recorded state.

## Result

the 15-case Release-host backend suite passes, and independent review accepts the private observation/effect split. status and recovery-status preserve exact frozen identity, retained transport/availability checks and pre-client tamper/foreign refusals; actual dispatch and recovery retain strict current-source validation. after the explicit restart of the identified idle Release-host worker, live MCP reads historical N12 with its eight completed and three interrupted terminal Runs and 22 durable receipts. scheduler SUCCESS remains distinct from the actual interrupted-pending work outcome; no replay, effect or release success is inferred.
