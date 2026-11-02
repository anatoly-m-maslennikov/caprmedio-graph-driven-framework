---
atom_id: CA-R-2461@2
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:25:49 +0400
subjects:
  governs: Entity/Graph Syntax <+ Relation//HAS_CLASSIFICATION
  depends_on:
  - Entity
  - Entity/Graph Syntax <+ Relation
relations: {}
---
## Summary

Define HAS_CLASSIFICATION

## Claim scope

Entities used as applicable Classification axes.

## Claim

HAS_CLASSIFICATION is the directed Relation from an Entity to another Entity
used as an applicable Classification axis. `X >| Y` means that X has Classification Y; `Y |< X`
is the reverse written view of that same fact. The pointer faces the
Classification endpoint, marked by the bar. A following `: Z` declares Z as
an allowed value of the qualified left expression under the generic colon rule.

### Formal claim

```text
Entity/Graph Syntax <+ Relation//HAS_CLASSIFICATION
```

## Notation for subject

```text
X >| Y
Y |< X
```

## Semantics

`Atom.Status >| Status Group` applies the Status Group Classification to Atom
Statuses. The applicable mapping assigns each admitted Status its group;
the Relation to the axis alone does not assign every allowed group at once.

This Relation differs from IS_CLASSIFIED_BY membership in a particular
classifier. It does not itself declare narrower-kind inheritance or structural
containment. The selected `>|` and `|<` spellings replace the earlier `::`
axis spelling. They do not repurpose the separate `::>` / `<::`
classification-membership proposal.

The reverse spelling adds no separately authored reverse fact. A canonical
inverse Relation Type name has not been selected by choosing its notation.

## Details

The Operator approved HAS_CLASSIFICATION, clarified that Status Group classifies
Atom Statuses rather than Atoms directly, and then selected
`something >| its classification / its classification |< something`.
The latest spelling supersedes `::`; it retains the underlying Relation meaning.

Classification is a reusable Term or role here, not a new Entity kind.
The named Relation instances are declared under
`Entity/Graph Syntax <+ Relation//HAS_CLASSIFICATION` and
`Entity/Graph Syntax <+ Relation//IS_CLASSIFIED_BY`; the latter retains its
separately defined membership meaning. Coordinated notation consumers remain
pending. The Operator's later `X/(.Y: Z)` qualification uses the existing
Property concept rather than a separate Classification Property category.
This Draft does not promote the operator,
implement a parser or introduce a stored `status_group` field.
