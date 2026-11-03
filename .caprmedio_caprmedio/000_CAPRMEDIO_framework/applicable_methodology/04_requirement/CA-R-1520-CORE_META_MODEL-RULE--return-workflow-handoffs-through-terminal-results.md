---
subjects:
  active: Entity/Object/Occurrent/Execution/Workflow Run
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Atom
  - Entity/Object/Continuant/Actor/Operator
  - Journal
  - Atom.Status
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1520
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1520-CORE_META_MODEL-RULE--return-workflow-handoffs-through-terminal-results.md
  source_atom_id: CA-R-1520
  source_atom_revision: 22
  source_sha256: e9700688139e312db77362a5678a08d7cec16fc242ef916f695b5ba501d81af1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Return Workflow handoffs through terminal results

## Claim scope

Workflow handoffs to another Workflow.

## Claim

**when** a Workflow declares a handoff **to** another Workflow, its Run **must** end with a terminal result sufficient for the executor **to** evaluate **and** start the continuation separately.

## Details

### Handoff result

- identify the completed Run, the reason for handoff, **and** the continuation Workflow **or** the methodology rule that selects it.
- provide the target identities **and** observed Revisions, required inputs **and** parameters, proposed changes, completed checks **and** their applicability, **and** a complete account of effects already performed, **if** **any**.
- distinguish a requested continuation from an authorized, started, **or** completed continuation. an incomplete result **must not** trigger guessed execution.

### Run boundary

- the ending Run does **not** call the continuation Workflow, wait for it, **or** resume its own normal Steps afterward.
- the executor retains the original request **and** the association between predecessor **and** successor Runs; it rechecks applicable authority **and** input freshness **before** starting the successor.
- ending the predecessor **must not** report the requested work as complete **when** a required continuation is still pending, blocked, **or** failed.
- the handoff outcome does **not** itself add a Status value. a chain of handoffs **must not** bypass approval, refresh an exhausted retry allowance, **or** create an unbounded loop.

the handoff is a result between distinct Runs, **not** a Step route between different Workflows.
