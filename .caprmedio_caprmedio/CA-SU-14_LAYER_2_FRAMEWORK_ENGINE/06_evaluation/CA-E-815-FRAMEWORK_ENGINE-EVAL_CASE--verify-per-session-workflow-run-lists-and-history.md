---
identity:
  atom_id: CA-E-815
  ref_id: CA-E-815
context:
  container:
    scope_unit: CA-SU-14
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Execution/Workflow Run
  tier: 5
state:
  status: active
  version: 2
  updated_at: '2026-11-12T17:12:05.980453+00:00'
destination:
  file:
    name: CA-E-815-FRAMEWORK_ENGINE-EVAL_CASE--verify-per-session-workflow-run-lists-and-history.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation
relations:
  evaluation_for:
  - CA-R-3016
author: Anatoly Maslennikov
---
## Summary

Verify per-session Workflow Run lists and history

## Claim

### Prose Claim

Exercise the generic session contract through two client-adapter fixtures without harness/provider branches in the runtime. Create Runs for two client sessions in one Project and one session in another Project. Each default listing selects only its Project and session. An explicit Project-wide listing includes both sessions in that Project. Continue or cancel a waiting Run by exact ID from another session, including after the initiating client disconnects. Preserve the original association. Reject another Project, unknown IDs and terminal IDs. Listing performs no operation effects.

Complete a Run, reconnect its session, and check that it leaves the active list while its recorded history remains associated with that Run. History reads must not resume an ended Run, repeat an effect or append invented events. Query-result expiry and query-log cleanup must not erase Run history. Missing or mismatched bindings must not select another session. Use the existing executor’s state transitions and history retention rules.
