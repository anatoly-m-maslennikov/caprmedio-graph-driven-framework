---
atom_id: CA-O-133
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Workflow//Build Entities Graph
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Entities Graph'
version: 15
updated_at: 2026-10-27 19:59:46 +0400
relations: {}
tier: 3
---
# Summary

Build Entities Graph

## Operation

Build Entities Graph **means** the reusable Workflow whose entry **and** only node is CA-O-135, the Entities Graph Construction Step. that Step owns its Action reference **and** invocation bindings; the Action owns construction behavior. the graph uses current Workflow execution authority under CA-R-1519 **and** exact definition Revisions under CA-R-1525.

### Graph scheme

| Entry/node | Result condition | Terminal outcome |
|---|---|---|
| CA-O-135 | built **or** no_op, with the Action's required current-selection, fidelity, validity **and** independent durable Run/effect evidence conditions satisfied | complete, preserving built versus no_op **and** the exact Projection/result references |
| CA-O-135 | incomplete, conflicting, stale **or** blocked | stop with that limitation **and** its affected frontier; request the missing evidence **or** authorization |
| CA-O-135 | reported built **or** no_op but **any** required completion condition is unmet **or** unsupported | blocked; retain the actual result **and** missing condition **without** accepting completion |
| CA-O-135 | failed | failed with actual effects **and** recovery evidence |
| CA-O-135 | canceled | canceled with actual effects **and** retained evidence |

there is no next-Step edge **or** automatic revisit. these are terminal outcomes, **not** extra nodes; no Step route **to** an Action **or** terminal label is invented. a new attempt needs a separately admitted invocation; source discovery, a failed build **or** a no-op does **not** authorize a retry, source repair **or** automatic rebuild.

the Workflow Run retains the exact Step/Action bindings **and** its independent start/terminal Run/effect evidence, with Journal references under CA-R-1525, CA-R-1720 **and** CA-R-1728. missing independent durable Run/effect evidence prevents a complete Run claim even **when** a Projection was produced; a Journal append failure alone retains the actual result and emits a `recording_error` diagnostic with pending evidence, **without** replaying construction.

## Details

this one-node scheme reuses CA-R-1438's graph kind. it is distinct from a particular build, a Tool **and** a source correction Workflow. a generic rebuild route **may** select this Workflow but does **not** force it **or** create another graph authority.
