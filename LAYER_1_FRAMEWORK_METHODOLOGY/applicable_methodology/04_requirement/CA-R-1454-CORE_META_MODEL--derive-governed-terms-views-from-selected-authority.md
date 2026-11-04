---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Terms Graph)'
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Method)/(.Header.Form: Term Definition)'
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Projection
version: 32
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1335@31
  - CA-R-1319
  - CA-R-1437
atom_id: CA-R-1454
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1454-CORE_META_MODEL--derive-governed-terms-views-from-selected-authority.md
  source_atom_id: CA-R-1454
  source_atom_revision: 32
  source_sha256: fcb5de2427dd003ac6d18a49268e3594a5263d9d1442eeaf3efd60560810c642
  original_relations_sha256: 8e132c01045800f67488d18acbb3aa8f36eb62c00d1c6ed57e3afc55b5abc32f
---
## Summary

Derive governed Terms views from selected authority

## Claim

### Prose Claim


governed-only Terms Graph views for a requested source selection.


for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319-CORE_META_MODEL--define-governed-term **and** CA-M-114-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms from Term Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Type is identified by its defining source Claim **and** that, where applicable, conforms to the governing Entity Definition constraints; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335@31-CORE_META_MODEL-DEFINITION--define-terms-graph **and** the source Relation authority under CA-R-1437-CORE_META_MODEL--keep-one-source-for-each-relation-fact **without** introducing another graph kind **or** independent vocabulary authority.

the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Term Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** the shared Relation Type definitions; a governed-only filter alone does **not** create another Type or alter its identity.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their endpoint identity and classes, shared Relation Type identity, any graph-qualified reference **or** context, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.

## Details

The dedicated lexical meaning owner is a Method Atom of Type Term Definition under CA-R-1319 and the admitted Method Type declaration. This adjusts only the selected lexical authority filter and its exact-source trace. Entity Definition constraints and source Relation authority retain their existing roles. These conditions govern a requested optional view; they require no dictionary Projection, extractor, lookup, or Terms Graph implementation and do not make a derived view a prerequisite of lexical meaning.
