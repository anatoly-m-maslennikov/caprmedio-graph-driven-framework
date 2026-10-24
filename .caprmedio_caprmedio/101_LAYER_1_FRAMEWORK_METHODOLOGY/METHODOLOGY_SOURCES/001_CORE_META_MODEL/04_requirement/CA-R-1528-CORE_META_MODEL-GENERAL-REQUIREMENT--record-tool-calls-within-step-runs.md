---
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Execution Trace/Tool Call Evidence
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1452
  - CA-R-1509
  - CA-R-1511
  - CA-R-1720
atom_id: CA-R-1528
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Rule
tier: 2
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
