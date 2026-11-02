---
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - Subject/Graph Node/Domain/Occurrent/Execution
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1511@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Definition
tier: 1
---
# Summary
Define Step Run

## Scope
actual executions of Steps within Workflow Runs.

## Claim

a Step Run **means** **`=1`** actual execution of **`=1`** Step within **`=1`** Workflow Run. **every** executed Step, including a containing Step, has its own distinct Step Run. a leaf Step Run executes its **`=1`** referenced Action through its **`=1`** corresponding Action Run with the bound parameters **and** inputs for that run; a containing Step Run groups the actual Runs of its nested substeps and launches no own Action.

- separate executions of the same Step are distinct Step Runs; leaf Step Runs reuse the Step **and** Action definitions, while containing Step Runs reuse the Step definition and group their nested Step Runs using existing Run parentage **and** lineage.
- an Agentic leaf Step Run records its resolved invocation context under CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context. its internal Tool-call evidence is associated with this Run under CA-R-1528-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs; a Tool call **or** repeated delivery of a pending invocation does **not** itself create another Step Run.
- the Step Run is distinct from its definition **and** from its Journal Records. a recorded attempt **or** failure **must not** be represented as successful completion.

## Details
