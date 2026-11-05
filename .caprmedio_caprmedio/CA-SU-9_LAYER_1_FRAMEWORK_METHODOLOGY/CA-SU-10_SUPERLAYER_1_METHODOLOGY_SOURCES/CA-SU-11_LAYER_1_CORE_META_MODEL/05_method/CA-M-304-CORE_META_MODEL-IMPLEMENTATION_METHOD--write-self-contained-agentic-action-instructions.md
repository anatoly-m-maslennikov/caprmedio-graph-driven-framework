---
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Prompt Authoring
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Prompt Authoring
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action).Execution Kind: Agentic'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  method_for:
  - CA-R-1789
  - CA-R-1790
  - CA-R-1791
  - CA-R-1792
  - CA-R-1793
atom_id: CA-M-304
ref_id: CA-M-304
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-M-304-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-self-contained-agentic-action-instructions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
---
## Summary
Write self-contained agentic Action instructions

## Claim

### Prose Claim

derived instructions that present an Agentic Action for execution.


**to** present an Agentic Action for execution, organize its derived instruction around the declared responsibility rather than assumed session memory.

- state the requested outcome, relevant context, exact targets, inputs, available evidence, **and** governing references.
- distinguish already performed effects from proposed changes, **and** existing permissions from decisions still needed.
- state the expected result **and** how **to** report uncertainty, failures, partial effects, **or** a request for Operator input. do **not** treat a suggested correction as permission **to** apply it.
- keep the instruction limited **to** the bound Action. leave next-Step selection **and** cross-Workflow handoff coordination **to** the executor using the governing Workflow.
- use understandable wording **and** structured points under CA-M-444-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning; reference governing definitions rather than copying another authoritative procedure into the prompt.
- keep internal Tool calls as execution detail under CA-R-1528-CORE_META_MODEL-RULE--record-tool-calls-within-step-runs. **when** an operation needs independently governed routing, checks, **or** approval boundaries, express it as an explicit Step during Workflow authoring rather than inventing Workflow nodes from runtime calls.
