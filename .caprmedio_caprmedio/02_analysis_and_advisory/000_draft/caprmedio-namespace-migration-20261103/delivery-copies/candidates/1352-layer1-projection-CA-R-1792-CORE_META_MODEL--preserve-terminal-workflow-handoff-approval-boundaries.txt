---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Journal
version: 18
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1792
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1792-CORE_META_MODEL--preserve-terminal-workflow-handoff-approval-boundaries.md
  source_atom_id: CA-R-1792
  source_atom_revision: 18
  source_sha256: 3d48d6b376318460324227397e758e445f822097832b7f85031a6f398e9da13b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve terminal Workflow handoff approval boundaries

## Claim scope

a terminal Workflow handoff from an Agentic Step Invocation.

## Claim

a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.
