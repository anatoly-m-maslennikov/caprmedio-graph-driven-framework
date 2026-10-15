---
subjects:
  governs: "Execution/Step Run"
  depends_on:
    ["Execution/Step Run", "Execution/Workflow Run", "Step", "Action", "Atom/Content Role: Operations/Type: Action/Execution Kind", "Agentic Step Execution Context", "Atom", "Operator", "Journal"]
version: 2
updated_at: "2026-10-15 12:23:20 +0000"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1790"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Retain Agentic Step executor state **and** routing

## Scope

execution coordination during dispatch **or** resumption of an Agentic Step, involving the executor together with the participating session **or** separate Agent context.

## Claim

the executor **must** retain execution state **and** select subsequent Steps from the Workflow's declared transitions. the participating session **or** separate Agent context performs the requested Action; it need **not** reconstruct **or** remember what the Workflow will do next.

## Details
