---
subjects:
  governs: Entity/Graph Syntax <+ Relation//CONTAINS
  depends_on:
  - Entity/Graph Syntax <+ Relation//IS_DERIVED_RELATION_OF
  - Entity/Object/Continuant/Governing Objects/Atom.Enabled Relations.Contains
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Graph Syntax <+ Relation//IS_CONTAINED_BY
version: 28
updated_at: 2026-10-30 17:27:35 +0400
relations: {}
atom_id: CA-R-1368@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Relation Definition
---
## Summary

Define Containment Relation Pair

## Claim scope

The `CONTAINS` and `IS_CONTAINED_BY` Relation Type instances, and direct
containment links that use that pair.

## Claim

`CONTAINS` is the derived counterpart of `IS_CONTAINED_BY`.

the Containment Relation Pair **means** direct containment
`Part +> Whole` through `IS_CONTAINED_BY` from Part to Whole **and** the
strictly derived inverse `Whole <+ Part` through `CONTAINS` from Whole to Part.
The direct IS_CONTAINED_BY fact is stored once; CONTAINS introduces no
independently stored reverse fact. Containment is non-inheriting.

### Formal claim

```text
Entity/Graph Syntax <+ Relation//IS_CONTAINED_BY
Entity/Graph Syntax <+ Relation//CONTAINS
```

## Semantics

For this pair, the derived CONTAINS view reverses the endpoints of the stored
IS_CONTAINED_BY fact. It does not classify the Part as a narrower kind of the
Whole and does not transfer inherited features between containment endpoints.

Endpoint permissions are separate constraints, not part of this definition.
Existing Scope Unit capability is described by CA-R-1757; CA-R-1656, CA-R-1756
and CA-R-1660 govern parent cardinality, immediate ownership and
structural-parent direction. Atom containment capability and its default are
governed by CA-R-1945, with the existing Plan, Workflow and Step permissions in
CA-R-1990, CA-R-1991 and CA-R-1992. Containment does not make a contained Atom
part of the containing Atom's Claim or change its owning Scope Unit. This
definition does not implement or require a construction graph projection.

## Notation for subject

```text
Whole <+ Part
```

## Details

This Draft proposes `+>` and `<+` for this pair. Bare `>` and `<` are
superseded within this proposal only; this Draft does not admit either new
notation into Current sources, a parser, a schema, or runtime behavior.

Current predecessor pin: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1368-CORE_META_MODEL--define-containment-relation-pair.md`, Atom `CA-R-1368`, version `27`, SHA-256 `edd3f3ef9b93c037534c9b5e93b9d1cdb33754f9fa52e91c0c24f793ed49bb37`. Its Current governed Subject path `Entity/Graph Syntax > Relation//CONTAINS` is preserved here as history, not proposed metadata.
