---
atom_id: CA-M-305
ref_id: CA-M-305@23-draft
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow >{1+} Atom/(.Header.Context.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
tier: 3
relations:
  method_for:
  - CA-R-1570
status: Draft
version: 23
updated_at: 2026-11-05 02:57:58 +0400
carrier_destination:
  file:
    name: CA-M-305@23-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-workflow-schemes-using-step-references.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/000_draft
---
## Summary

Write Workflow schemes using Step references

## Claim

### Prose Claim


Workflow schemes using Step references.


**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, declared Step order and structural Relations, Conditional Step routing, **and** terminal outcomes against those nodes.
- place each leaf Step’s single Action reference **or** Workflow call **and** its parameter/input bindings **in** that Step Atom rather than reproducing them **in** the scheme. A leaf Step RUNS exactly one Action **or** exactly one Workflow; its bindings use only previous Step outputs, the enclosing Workflow Run input, **or** values fixed by that Step. A containing Step carries its nested Steps and launches neither an Action nor a Workflow. Each binding references the selected Action or Workflow contract; it does not copy or redefine that contract.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.
