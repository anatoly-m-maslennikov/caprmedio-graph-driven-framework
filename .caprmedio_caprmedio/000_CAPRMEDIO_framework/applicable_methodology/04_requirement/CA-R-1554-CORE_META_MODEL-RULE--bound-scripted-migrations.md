---
atom_id: CA-R-1554
ref_id: CA-R-1554
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
tier: 2
status: Active
version: 23
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1554-CORE_META_MODEL-RULE--bound-scripted-migrations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1554-CORE_META_MODEL-RULE--bound-scripted-migrations.md
  source_atom_id: CA-R-1554
  source_atom_revision: 23
  source_sha256: 9b34b3173dfa44ffa15fc6312c98fa27272605784f8235c261a64269c42f556b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bound Scripted Migrations

## Claim

### Prose Claim


AI Agent participation in Scripted Migrations.


an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.
