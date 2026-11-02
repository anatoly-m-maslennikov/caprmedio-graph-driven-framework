---
atom_id: CA-R-1931@15
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax
  depends_on:
  - Entity/Object/Continuant/Term//Dependent Entity
  - Entity/Graph Syntax > Relation//IS_BORNE_BY
  - Entity
version: 15
relations: {}
tier: 3
updated_at: 2026-10-29 08:06:42 +0400
---
## Summary

Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent

## Claim scope

a Entity Path.

## Claim

In a Entity Path, `/` separates a broader kind from its narrower kind; `//`
separates an Entity kind from a named instance; `.` separates a bearer from a
dependent property; and `:` separates a property from an allowed literal
value. `@(...)` references an existing kind in the applicable `/` or `>`
position without declaring another target. `>` separates a full whole selector
from a full structural-part selector. It denotes containment only; its direct
fact is Part IS_CONTAINED_BY Whole, and CONTAINS is derived.

`Source ((RELATION_TYPE)) Target` expresses a defined named Relation. Persist
the direct fact once and show its declared derived inverse only as a derived
view. Entity syntax neither creates target identities nor admits native facts
without defining authority. A defining Atom may introduce its governed Entity.

Cardinality uses `{n}`, `{n+}`, and `{n..m}`. It follows the complete relation
token with surrounding whitespace, for example `Whole >{1+} Part`. It counts
direct property values or immediate parts; omitted cardinality is unspecified.
Advanced functions, formulas, interpolation, and bracketed conditions are out
of scope.

### Formal claim

```text
Entity/Object/Continuant/Package > Module > Code Unit
Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
Source ((RELATION_TYPE)) Target
```

## Semantics

`/` is specialization and supplies inheritance. `>` is containment and does
not supply inheritance, sequence, or a property relation. `//` names an
instance of a kind; `.` addresses a dependent property; and `:` declares an
allowed value rather than assigning one. A reference marker preserves the
underlying operator's meaning and creates neither an alias nor a duplicate.

## Details

Each Module belongs to exactly one Package; Project Implementation is the
parentless root Package and a nested Package belongs to another Package. Step
belongs to Workflow; Step and Sub-step are distinct. Scope Unit has structural
parts expressed as `Scope Unit >@(Scope Unit)`, `Scope Unit >@(Atom)`, and
`Scope Unit >@(Projection)`.

Backslash escapes the next literal name character. Single/double quotes are
carrier serialization, not Entity delimiters. One globally unique primary
kind name and one canonical declaration path are required; migration does not
retain aliases. Term-path reconciliation remains subject to C605.
