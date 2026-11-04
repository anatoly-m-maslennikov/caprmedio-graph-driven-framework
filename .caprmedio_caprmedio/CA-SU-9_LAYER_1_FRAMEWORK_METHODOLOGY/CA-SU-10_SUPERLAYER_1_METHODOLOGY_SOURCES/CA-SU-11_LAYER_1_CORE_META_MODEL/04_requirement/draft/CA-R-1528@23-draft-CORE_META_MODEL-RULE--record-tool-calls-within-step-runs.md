---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Event Record
version: 23
updated_at: 2026-11-05 02:06:39 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1528
status: Draft
tier: 2
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1528@23-draft-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Record Tool calls within Step Runs

## Claim

### Prose Claim


Tool Calls that occur within Step Runs.


a Tool Call **means** an invocation of a Tool during execution; **when** it occurs within a Step Run, its execution evidence **must** remain associated with that parent Step Run **in** the canonical Project Journal.

## Details

- retain the invoked Tool, supplied inputs, actual result **or** error, **and** parent Step Run association. preserve call identity **and** timing sufficient **to** distinguish separate attempts; do **not** report an attempted **or** uncertain effect as confirmed completion.
- use authorized references **or** protected representations for secret **or** sensitive inputs under their governing rules; execution tracing does **not** authorize copying secrets into the Journal.
- a Step Run for a leaf Step that runs an Action executes its **`=1`** declared Action through its **`=1`** Action Run. a containing Step Run launches no own Action; its nested Step Runs retain their own Step execution. Tool calls remain execution details associated with their parent Step Run, **not** automatically new Steps, Action definitions, **or** Workflow nodes; this tracing rule does **not** grant Tool-call permission.
- a view **may** display Workflow Run, containing **and** leaf Step Runs, **and** Tool-call evidence as a nested trace; derive the view from the canonical records rather than creating another independently maintained execution history.
- preserve actual ordering **and** parentage **without** inferring concurrency permission, Workflow routing, **or** a new Step Run for **every** Tool call.
