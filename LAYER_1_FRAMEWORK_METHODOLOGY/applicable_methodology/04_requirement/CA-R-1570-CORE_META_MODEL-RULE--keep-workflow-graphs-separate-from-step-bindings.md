---
atom_id: CA-R-1570
ref_id: CA-R-1570
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
tier: 2
status: Active
version: 26
updated_at: 2026-11-02 17:54:42 +0400
carrier_destination:
  file:
    name: CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md
  source_atom_id: CA-R-1570
  source_atom_revision: 26
  source_sha256: 0108807fb3de910b62bcbcb991aed7d7cb43a9f5dc85bdda1b01fac02a1b4247
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Workflow graphs separate from Step bindings

## Claim

### Prose Claim


a Workflow graph scheme.


A Workflow graph scheme **must** identify Step references, declared order, structural Relations, entry points, and terminal outcomes.

The graph references Step bindings and called definitions. Its declared graph determines control flow; folder nesting and file order **must not** replace it.
