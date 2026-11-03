---
subjects:
  active: Atom/(.Role:=Operations)/Workflow
  passive:
  - Atom/(.Role := Operations)/Step
  - Atom/(.Role:=Operations)/Action
  - Atom/(.Role:=Operations)/Workflow
version: 26
relations: {}
atom_id: CA-R-1570
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
updated_at: 2026-11-02 17:54:42 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md
  source_atom_id: CA-R-1570
  source_atom_revision: 26
  source_sha256: 5021c9779c0b0215e229649e971b3a85c06b9759f2e65b96cfead4d3b53b094e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Workflow graphs separate from Step bindings

## Claim scope

a Workflow graph scheme.

## Claim

A Workflow graph scheme **must** identify Step references, declared order, structural Relations, entry points, and terminal outcomes.

The graph references Step bindings and called definitions. Its declared graph determines control flow; folder nesting and file order **must not** replace it.
