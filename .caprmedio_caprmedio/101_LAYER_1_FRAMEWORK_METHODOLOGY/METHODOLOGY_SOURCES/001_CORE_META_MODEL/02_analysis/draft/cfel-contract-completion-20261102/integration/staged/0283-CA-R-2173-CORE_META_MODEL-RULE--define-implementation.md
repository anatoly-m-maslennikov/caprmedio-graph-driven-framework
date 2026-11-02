---
atom_id: CA-R-2173
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Package/Implementation
  passive: []
version: 8
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
---
## Summary

Define Implementation

## Claim

Implementation **means** the actual Code, Prompts, Documentation and Resources that realize RMED for a Project. Directly edited Implementation can be authoritative for what is actually implemented.

## Semantics

Implementation is not a Projection merely because it realizes RMED. Its logical artifacts remain distinct from their Carriers and from the Runtime in which technical execution occurs.

A Projection is a non-authoritative output produced from a declared source selection through a Workflow: source of truth → Workflow → Projection. Changes to a Projection belong in its authoritative sources, followed by a rebuild through its Workflow. A generated view of Implementation is a Projection; that does not make its directly edited sources Projections.

## Details

CA-R-2535 defines Projection and its source-only editing boundary. CA-R-1568 permits a derived view to be delivered as an Implementation output without classifying Implementation as a whole as Projection.
