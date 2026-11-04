---
atom_id: CA-R-2225
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Entity
relations:
  depends_on:
  - CA-R-2150@15
tier: 2
version: 4
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2225-CORE_META_MODEL-RULE--select-subject-graph-views-by-scope-units-and-branches.md
  source_atom_id: CA-R-2225
  source_atom_revision: 4
  source_sha256: aebd0fee87c89750833158e5f03a9be4abbee797e7b32d9dd8f62d5643f538a6
  original_relations_sha256: e5ed80c802b42a75a70b2cec6a262ed7c2e007d5530dfdb1f2db24403c6b3cb2
---
## Summary

Select Subject Graph views by Scope Units and branches

## Claim

### Prose Claim


Each focused Subject Graph Projection **must** state and use one declared selection. Scope Unit criteria select Current RMEDO source Atoms by their Local Scope Unit, with an explicit option to include descendants declared in Project Structure. Folder nesting does not determine the selected Scope Units. Subject-branch criteria select canonical target branches while retaining ancestor context and the source-backed properties needed for inheritance within the selected source set.

Multiple selected Scope Units form a union; multiple selected branches form a union. When both criteria are supplied, both restrictions apply. With neither restriction, use all Current RMEDO sources. The Projection Type determines its view, not which sources are selected.

For dependency-only results, compare exact Depends On and Governs paths inside the same selected source set. Do not silently consult sources outside that set to suppress entries. Namespace and Subject operator boundaries remain significant; a lexical prefix such as Atom must not also match AtomExtra.

## Details

The Projection records its Scope Unit and branch criteria, descendant option, named selection and source-of-truth identity. Its YAML sources list records the actual supporting source IDs and Versions. Branch views retain declared inherited-property context without claiming that omitted branches were rendered. Source and target filters do not create another entity or copy the selected members.
