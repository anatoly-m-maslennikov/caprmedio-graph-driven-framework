---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Entity
version: 23
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
atom_id: CA-R-1351
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Give Primary Entity Occurrences No Bearer

## Claim scope

Primary Entity occurrences referenced by a Subject.

## Claim

a Primary Entity referenced by a Subject **must** have **`=0`** outgoing IS_PROPERTY_OF Relations.

## Details

This successor preserves the existing Primary Entity constraint and immutable Summary. It changes the Relation reference to the approved canonical IS_PROPERTY_OF name; it does not remove Primary Entity semantics or create a new primary-kind branch. Zero outgoing Relations here does not prohibit being the target bearer of incoming Property Relations.

### Current source pin and pending adoption

Proposed N+1 successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1351-CORE_META_MODEL--give-primary-entity-occurrences-no-bearer.md`, Version 20, SHA-256 `58b6e1292608a312620fa9fed36f88bdf2b67790309053056cf6a6e5fafc2879`. Current bytes remain unchanged. The new Relation names depend on the pending IS_PROPERTY_OF / HAS_PROPERTY Relation Definition Drafts; this source does not admit them through a renamed token alone. This preparation performs no runtime change, generated-view refresh or promotion.
