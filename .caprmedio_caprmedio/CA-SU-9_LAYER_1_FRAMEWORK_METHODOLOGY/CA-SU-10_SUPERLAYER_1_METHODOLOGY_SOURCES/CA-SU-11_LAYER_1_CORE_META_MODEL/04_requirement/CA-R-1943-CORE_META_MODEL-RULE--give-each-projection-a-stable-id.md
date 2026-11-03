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
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
version: 15
updated_at: 2026-11-02 00:18:22 +0400
relations:
  depends_on:
  - CA-R-2535
tier: 3
role: Requirement
form: Rule
---
## Summary

Give each Projection a stable ID

## Claim

### Prose Claim


Projection identity across rebuilds.


Every Projection has one Projection ID. The same Projection Type, named source selection and source of truth identify the same Projection and keep the same ID across rebuilds.

## Details

- A different Type, named source selection or source of truth identifies a different Projection and requires a different ID.
- Changes to source contents, source Versions, the artifacts selected by the same selection, generated content or Updated At do not change the Projection ID.
- A change to the current Scope Unit name or Carrier path alone does not change the Projection ID.
- Projection ID identifies the derived view, not any source Atom. It does not make the Projection authoritative.
