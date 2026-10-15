---
subjects:
  governs: "Execution/Step Run"
  depends_on:
    ["Step", "Execution/Workflow Run", "Action", "Journal.Record", "Agentic Step Execution Context", "Tool", "Tool Call"]
version: 6
updated_at: "2026-10-15 12:12:51 +0000"
relations: {}
atom_id: "CA-R-1511@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
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
