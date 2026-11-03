---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Action
version: 22
updated_at: 2026-11-02 08:06:47 +0400
relations:
  method_for:
  - CA-R-1570
atom_id: CA-M-305
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-305-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-workflow-schemes-using-step-references.md
  source_atom_id: CA-M-305
  source_atom_revision: 22
  source_sha256: 140d66b3f77279aba1f1a12e2d8b18fe02966b9326c1479375094fa522892312
  original_relations_sha256: c0cf2b4b80c401bd0e2e83ae0bd314905914842bc400d929bd6a07428aa6da4d
---
## Summary

Write Workflow schemes using Step references

## Claim scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, declared Step order and structural Relations, Conditional Step routing, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** leaf Step Atoms rather than reproducing them **in** the scheme; a containing Step carries its nested substeps and no own Action launch.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.
