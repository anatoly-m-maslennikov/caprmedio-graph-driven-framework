---
subjects:
  governs: Entity/Object/Continuant/History/Journal > Event Record
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/Projection
version: 18
updated_at: 2026-10-29 07:17:23 +0400
relations:
  evaluation_for:
  - CA-R-1528
  - CA-R-1511
atom_id: CA-E-496@18
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary

Validate nested Tool-call evidence

## Scope

Tool-call evidence within a Step Run.

## Claim

the Evaluation **must** check Tool-call evidence within a Step Run under CA-R-1528.

## Details

- an Agentic Action makes several Tool calls inside a leaf Step Run: require their actual parent Step Run, Tool identities, inputs **or** admitted protected references, results **or** errors, **and** distinguishing call evidence.
- a repeated attempt uses the same Tool **and** inputs: preserve distinct attempt identities **without** claiming a second effect **when** its outcome is unknown.
- a Tool call fails **or** its effect cannot be confirmed: retain that outcome rather than recording successful completion.
- a nested trace is rebuilt: require derivation from the canonical Journal **without** another source of execution history.
- a Tool call automatically creates a Workflow Step, a Conditional Step route, **or** a new Action definition: reject that inference.
- secret input is encountered: require its governed protected representation rather than plaintext duplication for trace completeness.

missing evidence **or** an unperformed check is **not** a passing result.
