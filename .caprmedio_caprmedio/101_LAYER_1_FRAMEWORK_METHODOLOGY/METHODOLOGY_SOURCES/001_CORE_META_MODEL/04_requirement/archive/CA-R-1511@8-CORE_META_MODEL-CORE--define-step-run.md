---
subjects:
  governs: "Entity/Node/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/History/Journal.Record", "Agentic Step Execution Context", "Tool", "Tool Call"]
version: 8
updated_at: "2026-10-19 15:53:19 +0400"
relations: {}
atom_id: CA-R-1511@8
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Define Step Run

## Scope
actual executions of Steps within Workflow Runs.

## Claim

a Step Run **means** **`=1`** actual execution of **`=1`** Step within **`=1`** Workflow Run, invoking the Step's **`=1`** referenced Action with the bound parameters **and** inputs for that run.

- separate executions of the same Step are distinct Step Runs; they reuse the Step **and** Action definitions.
- an Agentic Step Run records its resolved invocation context under CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context. its internal Tool-call evidence is associated with this Run under CA-R-1528-CORE_META_MODEL-GENERAL-REQUIREMENT--record-tool-calls-within-step-runs; a Tool call **or** repeated delivery of a pending invocation does **not** itself create another Step Run.
- the Step Run is distinct from its definition **and** from its Journal Records. a recorded attempt **or** failure **must not** be represented as successful completion.

## Details
