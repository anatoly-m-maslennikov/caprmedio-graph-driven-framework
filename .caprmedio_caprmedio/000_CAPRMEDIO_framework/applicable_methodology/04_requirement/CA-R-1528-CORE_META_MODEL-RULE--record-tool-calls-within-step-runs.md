---
subjects:
  active: Entity/Object/Occurrent/Execution
  passive:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Journal
  - Entity/Object/Continuant/History/Journal > Event Record
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1528
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1528-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs.md
  source_atom_id: CA-R-1528
  source_atom_revision: 22
  source_sha256: 90ed7af7ee5dbbbe01e2c79590793100b5492def31c9dc51dbd8846cb78225fc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Record Tool calls within Step Runs

## Claim scope

Tool Calls that occur within Step Runs.

## Claim

a Tool Call **means** an invocation of a Tool during execution; **when** it occurs within a Step Run, its execution evidence **must** remain associated with that parent Step Run **in** the canonical Project Journal.

## Details

- retain the invoked Tool, supplied inputs, actual result **or** error, **and** parent Step Run association. preserve call identity **and** timing sufficient **to** distinguish separate attempts; do **not** report an attempted **or** uncertain effect as confirmed completion.
- use authorized references **or** protected representations for secret **or** sensitive inputs under their governing rules; execution tracing does **not** authorize copying secrets into the Journal.
- a leaf Step Run executes its **`=1`** declared Action through its **`=1`** Action Run. a containing Step Run launches no own Action; its nested Step Runs retain their own Step execution. Tool calls remain execution details associated with their parent Step Run, **not** automatically new Steps, sub-steps, Action definitions, **or** Workflow nodes; this tracing rule does **not** grant Tool-call permission.
- a view **may** display Workflow Run, containing **and** leaf Step Runs, **and** Tool-call evidence as a nested trace; derive the view from the canonical records rather than creating another independently maintained execution history.
- preserve actual ordering **and** parentage **without** inferring concurrency permission, Workflow routing, **or** a new Step Run for **every** Tool call.
