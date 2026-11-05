---
atom_id: CA-D-333
ref_id: CA-D-333
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Scope Unit Graph)
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Carrier
tier: 2
status: Active
version: 35
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-333-CORE_META_MODEL-DECISION--serialize-scope-unit-graph-projection-generation-metadata.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize Scope Unit Graph Projection Generation Metadata

## Claim

### Prose Claim


a retained Project Scope Unit Graph Projection for compatibility.


**if** a Project Scope Unit Graph Projection is retained for compatibility, its Carrier **must** serialize Updated At, generator identity **and** digest, exact consumed Project Structure **and** Settings source states, **and** the source bindings **and** distinct Directory Carrier observations needed **to** explain emitted values **and** unresolved findings. this compatibility format does **not** require production **or** refresh of a separate structural Projection.
