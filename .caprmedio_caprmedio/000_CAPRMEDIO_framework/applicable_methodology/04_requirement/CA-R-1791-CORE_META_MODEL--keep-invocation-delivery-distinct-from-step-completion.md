---
subjects:
  active: Entity/Object/Occurrent/Execution/Step Run
  passive:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Entity/Object/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - Entity/Object/Continuant/Actor/Operator
  - Journal
version: 18
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1791
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1791-CORE_META_MODEL--keep-invocation-delivery-distinct-from-step-completion.md
  source_atom_id: CA-R-1791
  source_atom_revision: 18
  source_sha256: 732479725b39154227e6e50dd3fc6fb944c0f6427172ac3ef0bc1475df90b549
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Invocation delivery distinct from Step completion

## Claim scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.
