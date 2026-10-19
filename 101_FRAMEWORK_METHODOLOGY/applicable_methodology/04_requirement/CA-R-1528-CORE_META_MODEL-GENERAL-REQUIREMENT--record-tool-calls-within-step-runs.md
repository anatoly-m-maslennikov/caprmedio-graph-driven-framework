---
subjects:
  governs: "Tool Call"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Tool", "Entity/Continuant/History/Journal", "Entity/Continuant/History/Journal.Record"]
version: 7
updated_at: "2026-10-15 18:44:00 +0000"
relations: {"relates_to": ["CA-R-1452", "CA-R-1509", "CA-R-1511", "CA-R-1720"]}
atom_id: "CA-R-1528"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1528-CORE_META_MODEL-GENERAL-REQUIREMENT--record-tool-calls-within-step-runs.md
  source_atom_id: CA-R-1528
  source_atom_revision: 7
  source_sha256: 1f55be7bfd830b201130356be2ff164257b5d4086f55a964115c0a35d3520d18
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Record Tool calls within Step Runs

## Scope

Tool Calls that occur within Step Runs.

## Claim

a Tool Call **means** an invocation of a Tool during execution; **when** it occurs within a Step Run, its execution evidence **must** remain associated with that parent Step Run **in** the canonical Project Journal.

## Details

- retain the invoked Tool, supplied inputs, actual result **or** error, **and** parent Step Run association. preserve call identity **and** timing sufficient **to** distinguish separate attempts; do **not** report an attempted **or** uncertain effect as confirmed completion.
- use authorized references **or** protected representations for secret **or** sensitive inputs under their governing rules; execution tracing does **not** authorize copying secrets into the Journal.
- the parent Step Run invokes its **`=1`** declared Action. its internal Tool calls are execution details, **not** automatically new Steps, sub-steps, Action definitions, **or** Workflow nodes.
- a view **may** display Workflow Run, Step Run, **and** Tool-call evidence as a nested trace; derive the view from the canonical records rather than creating another independently maintained execution history.
- preserve actual ordering **and** parentage **without** inferring concurrency permission, Workflow routing, **or** a new Step Run for **every** Tool call.
