---
identity:
  atom_id: CA-R-3016
  ref_id: CA-R-3016@1
context:
  container:
    scope_unit: CA-SU-14
  role: Requirement
  form: Requirement
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Execution/Workflow Run
  tier: 3
state:
  status: archived
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-3016@1-REQUIREMENT--each-session-can-get-its-active-workflow-runs-and-history.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/099_archived
author: Anatoly Maslennikov
---

## Summary

Each session can get its active Workflow Runs and history

## Claim

### Prose Claim

Each session must list its own active Workflow Runs and retrieve their recorded history within its selected Project.

Bind each Run to the initiating Project and client session, represented by runtime context `session_id`, and retain that association through continuation. Default session reads select that exact pair; they must not return or continue another session’s Runs. Active means nonterminal under the existing executor state and transition rules. Reading a list or history does not execute, resume or repeat work.

History comes from the existing Project Journal/Event Records with their recorded Run association. Terminal Runs remain available through history under the existing history rules. Query logs, cached query results and their TTL do not define Workflow Run history. The capability is independent of the harness and LLM provider. This Requirement adds no limit on concurrent Runs or new Run Status vocabulary.
