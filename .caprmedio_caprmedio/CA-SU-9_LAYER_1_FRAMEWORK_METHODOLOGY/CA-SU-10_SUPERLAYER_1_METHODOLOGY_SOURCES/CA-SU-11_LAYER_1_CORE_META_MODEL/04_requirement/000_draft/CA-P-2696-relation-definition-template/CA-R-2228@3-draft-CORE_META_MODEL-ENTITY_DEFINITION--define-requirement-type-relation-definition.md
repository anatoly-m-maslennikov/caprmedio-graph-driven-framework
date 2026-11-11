---
atom_id: CA-R-2228@3-draft
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Relation Definition'
version: 3
relations: {}
tier: 1
updated_at: 2026-10-29 15:24:34 +0400
---
## Summary

Define Requirement Type Relation Definition

## Claim

Relation Definition is an Entity Definition with a relation-specific template. Its stored Type remains Relation Definition, and it counts toward exactly-one Entity Definition ownership for the Relation Types it defines. This does not introduce a subtype hierarchy or an additional subtype property. A Relation Type definition remains distinct from a real source-Type-target connection and from the Entity Definition describing generic Relation structure.

Define the main Relation direction once: its canonical name, meaning and direction. Declare its derived counterpart only by name and a short reference to that main direction, for example: `CONTAINS is the derived counterpart of IS_CONTAINED_BY`. The counterpart reuses the main direction's definition through that short reference. Do not create a separate full Definition or repeat meaning, endpoint constraints, cardinalities or other operative rules for the counterpart; derive its reverse view from the main direction. Store only the direct facts.

The definition follows the required direct prose Claim and optional R Formal claim contract. Its content.notation_for_subject property has zero or one string value, represented by a fenced code block under ## Notation for subject. When an admitted short Entity operator exists, that section is required and states its exact notation. Other named Relations use the general ((RELATION_TYPE)) form and may omit the section. Examples and Semantics do not override the Claim's declared direct/derived meaning.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Relation Definition.Content.notation_for_subject[string]{0..1}
```

## Details

The main/counterpart template applies DRY to one coherent Relation pair. The counterpart is visible for navigation and definition lookup; it is not independently authored as a second primitive fact. The required-if-short-notation condition stays in prose; advanced bracketed conditions remain deferred.
