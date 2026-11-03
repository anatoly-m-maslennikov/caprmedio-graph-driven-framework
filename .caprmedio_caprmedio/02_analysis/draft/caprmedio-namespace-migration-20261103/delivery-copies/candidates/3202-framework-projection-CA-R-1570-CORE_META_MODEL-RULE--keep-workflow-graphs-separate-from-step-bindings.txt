---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)/Step
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Action
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
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
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md
  source_atom_id: CA-R-1570
  source_atom_revision: 26
  source_sha256: afb17764efefa06835d173a00216603393d2acb9c10b2831501a315d0823c113
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Workflow graphs separate from Step bindings

## Claim scope

a Workflow graph scheme.

## Claim

A Workflow graph scheme **must** identify Step references, declared order, structural Relations, entry points, and terminal outcomes.

The graph references Step bindings and called definitions. Its declared graph determines control flow; folder nesting and file order **must not** replace it.
