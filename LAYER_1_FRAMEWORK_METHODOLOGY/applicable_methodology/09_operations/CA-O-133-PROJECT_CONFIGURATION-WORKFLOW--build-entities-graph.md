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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-133-PROJECT_CONFIGURATION-WORKFLOW--build-entities-graph.md
  source_atom_id: CA-O-133
  source_atom_revision: 15
  source_sha256: e9167783144f995dfbd91f37b6970ffc78512a38fb46cb97c59c58fe16ccf424
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
