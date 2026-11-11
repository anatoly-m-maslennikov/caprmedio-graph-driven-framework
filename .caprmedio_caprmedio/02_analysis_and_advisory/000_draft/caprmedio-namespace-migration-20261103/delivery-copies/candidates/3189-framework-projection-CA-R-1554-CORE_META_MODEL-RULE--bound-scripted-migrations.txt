---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Selection
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1554
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1554-CORE_META_MODEL-RULE--bound-scripted-migrations.md
  source_atom_id: CA-R-1554
  source_atom_revision: 23
  source_sha256: 47dd76275f55e047deff957f689ffac9a673cf77050d1db5653a08a218471ce4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bound Scripted Migrations

## Claim scope

AI Agent participation in Scripted Migrations.

## Claim

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
