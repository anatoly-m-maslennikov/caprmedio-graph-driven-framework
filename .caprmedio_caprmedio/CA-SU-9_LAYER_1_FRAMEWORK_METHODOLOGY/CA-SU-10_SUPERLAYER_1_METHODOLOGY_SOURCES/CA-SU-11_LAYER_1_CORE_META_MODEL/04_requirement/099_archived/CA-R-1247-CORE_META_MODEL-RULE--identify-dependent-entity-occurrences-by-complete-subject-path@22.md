---
subjects:
  governs: Entity/Object/Continuant/Term//Dependent Entity
  depends_on:
  - Entity
version: 22
updated_at: 2026-10-29 14:12:43 +0400
relations: {}
atom_id: CA-R-1247
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Identify Dependent-Entity Occurrences by Complete Subject Path

## Claim scope

Dependent Entity occurrences and their complete Subject Paths.

## Claim

**every** Dependent Entity occurrence **must** derive its source-admitted bearer-qualified identity from its complete Subject Path **without** imposing one global ordinal position on a reusable Term; distinct modeled entities **must** use distinct complete canonical names, while repeated references **to** the same entity **must** retain its same complete canonical name.

## Details

The complete Subject Path preserves source-admitted bearer qualification. Ordinal position and display placement do not create entity identity. Qualification is part of the complete property name used for collision checks. A repeated display or reference of one entity remains the same entity, and parsing a name does not introduce another graph entity.

The Operator accepted `atom.id` and `projection.id` as distinct complete qualified property names. `ID` is reusable and the terminal label need not be globally unique. Shared `Unit` components remain permitted in `Scope Unit` and `Code Unit`. This preserves complete-path identity without imposing disjoint lexical components or a new global ordinal position.
