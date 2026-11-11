---
atom_id: CA-M-305
ref_id: CA-M-305
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
tier: 3
relations:
  method_for:
  - CA-R-1570
status: Active
version: 22
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-M-305-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-workflow-schemes-using-step-references.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Write Workflow schemes using Step references

## Claim

### Prose Claim


Workflow schemes using Step references.


**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, declared Step order and structural Relations, Conditional Step routing, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** leaf Step Atoms rather than reproducing them **in** the scheme; a containing Step carries its nested substeps and no own Action launch.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.
