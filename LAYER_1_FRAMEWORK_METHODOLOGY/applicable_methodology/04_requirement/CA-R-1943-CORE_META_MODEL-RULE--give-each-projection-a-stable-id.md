---
atom_id: CA-R-1943
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection.ID
  passive:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Projection.Form
  - CAPRMEDIO_MODEL <+ Projection.Scope Unit
  - CAPRMEDIO_MODEL <+ Projection.Source.Named Selection
  - CAPRMEDIO_MODEL <+ Projection.Source.Atoms
version: 16
updated_at: 2026-11-04 07:51:19 +0400
relations:
  depends_on:
  - CA-R-2535
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1943-CORE_META_MODEL-RULE--give-each-projection-a-stable-id.md
  source_atom_id: CA-R-1943
  source_atom_revision: 16
  source_sha256: cb7d14ede2018974e6ffd21074d5fec576273c08d8ab053ac9e14829e516024d
  original_relations_sha256: 6878e685139e7f8ef4f489b6e750cc91c96c00e957ae6a05bdf9168f28ce7685
---
## Summary

Give each Projection a stable ID

## Claim

### Prose Claim


Projection identity across rebuilds.


Every Projection has one Projection ID. Its Form and Scope Unit determine its ID, and its ID determines its Form and Scope Unit. Rebuilding the same Projection retains that ID.

## Details

- A different Form or Scope Unit identifies a different Projection and requires a different ID.
- Changes to the Named Selection, its selected sources, source contents or Versions, generated content or Updated At do not change the Projection ID. Source.Named Selection describes the sources; it is not an identity component. Where Source.Atoms is recorded, each value identifies an Atom with its explicit Version.
- A change to the current Scope Unit name or Carrier path alone does not change the Projection ID.
- Projection ID identifies the derived view, not any source Atom. It does not make the Projection authoritative.
