---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Terms Graph'
  depends_on:
  - Entity/Object/Continuant/Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Graph Syntax > Relation
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Projection
version: 30
updated_at: 2026-10-29 14:12:43 +0400
relations:
  child_of:
  - CA-R-1335
  - CA-R-1319
  - CA-R-1437
atom_id: CA-R-1454
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Derive governed Terms views from selected authority

## Claim scope

governed-only Terms Graph views for a requested source selection.

## Claim

for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319-CORE_META_MODEL--define-governed-term **and** CA-M-114-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms from Term Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Type is identified by its defining source Claim **and** that, where applicable, conforms to the governing Entity Definition constraints; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335-CORE_META_MODEL-DEFINITION--define-terms-graph **and** the source Relation authority under CA-R-1437-CORE_META_MODEL--keep-one-source-for-each-relation-fact **without** introducing another graph kind **or** independent vocabulary authority.

the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Term Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** the shared Relation Type definitions; a governed-only filter alone does **not** create another Type or alter its identity.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their endpoint identity and classes, shared Relation Type identity, any graph-qualified reference **or** context, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.

## Details

The dedicated lexical meaning owner is a Requirement Atom of Type Term Definition under CA-R-1319 and CA-R-2229. This adjusts only the selected lexical authority filter and its exact-source trace. Entity Definition constraints and source Relation authority retain their existing roles. These conditions govern a requested optional view; they require no dictionary Projection, extractor, lookup, or Terms Graph implementation and do not make a derived view a prerequisite of lexical meaning.
