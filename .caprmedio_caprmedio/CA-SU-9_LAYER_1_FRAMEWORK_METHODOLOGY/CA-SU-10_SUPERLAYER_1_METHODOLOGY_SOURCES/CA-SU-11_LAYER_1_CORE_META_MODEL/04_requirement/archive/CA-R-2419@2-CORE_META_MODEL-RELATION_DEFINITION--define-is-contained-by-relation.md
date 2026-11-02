---
atom_id: CA-R-2419@2
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax <+ Relation//IS_CONTAINED_BY
relations: {}
version: 2
updated_at: 2026-10-30 17:30:45 +0400
---
## Summary

Define IS_CONTAINED_BY Relation

## Claim scope

The direct Part-to-Whole containment direction.

## Claim

IS_CONTAINED_BY is the direct containment direction: `Part +> Whole`. CA-R-1368
defines the Containment Relation Pair, including `Whole <+ Part` as CONTAINS,
its strict derived inverse. The direct fact is stored once; no independently
stored reverse fact is introduced.

### Formal claim

```text
Entity/Graph Syntax <+ Relation//IS_CONTAINED_BY
```

## Notation for subject

```text
Part +> Whole
```

## Details

This direct-reference Definition reuses CA-R-1368's pair meaning, endpoint
authority, and non-inheriting containment semantics. It does not add a second
full definition, an endpoint rule, a carrier rule, or an independently authored
CONTAINS fact.

This Draft proposes `+>` for the direct direction. Bare `>` and `<` are
superseded within this proposal only; this Draft does not admit the notation
into Current sources, a parser, a schema, or runtime behavior.

Current predecessor pin: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2419-CORE_META_MODEL-RELATION_DEFINITION--define-is-contained-by-relation.md`, Atom `CA-R-2419`, version `1`, SHA-256 `6950ece60456cdca9131a3106d781a67631fed15e633c06dbba53aea95d87570`. Its Current governed Subject path `Entity/Graph Syntax > Relation//IS_CONTAINED_BY` is preserved here as history, not proposed metadata.
