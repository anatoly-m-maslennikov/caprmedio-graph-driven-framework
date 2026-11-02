---
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution
  depends_on:
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1528@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
- a leaf Step Run executes its **`=1`** declared Action through its **`=1`** Action Run. a containing Step Run launches no own Action; its nested Step Runs retain their own Step execution. Tool calls remain execution details associated with their parent Step Run, **not** automatically new Steps, sub-steps, Action definitions, **or** Workflow nodes; this tracing rule does **not** grant Tool-call permission.
- a view **may** display Workflow Run, containing **and** leaf Step Runs, **and** Tool-call evidence as a nested trace; derive the view from the canonical records rather than creating another independently maintained execution history.
- preserve actual ordering **and** parentage **without** inferring concurrency permission, Workflow routing, **or** a new Step Run for **every** Tool call.
