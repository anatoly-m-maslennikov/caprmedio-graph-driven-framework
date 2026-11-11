---
atom_id: CA-R-2244
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:32:39 +0400
---
## Summary

Define Graph Syntax

## Claim

Graph Syntax defines how Entity Definitions express specialization,
named-instance, dependent-property, allowed-value, containment, existing-kind
reference, named-relation, value-format, and cardinality constructs. Its
structural parts are Relation, Format, and Cardinality. Syntax neither
executes a Workflow nor creates an Entity instance.

The colon declares a literal allowed value; it is not assignment. YAML null
and an empty string are values for counting, while Format and prose decide
admissibility. Advanced formulas and bracketed conditions remain separate.

### Formal claim

```text
Entity/Graph Syntax > Relation
Entity/Graph Syntax > Format
Entity/Graph Syntax > Cardinality
```

```text
specialization: /
named_instance: //
dependent_property: .
allowed_value: :
containment: >
existing_kind_reference: @(...)
cardinality: {n}, {n+}, {n..m}
inverse: declared and derived, never independently stored
```

## Semantics

`/` supplies specialization and inheritance. `//` expresses a named instance
of a kind. `.` identifies a dependent property, `:` an allowed value, and `>`
structural containment. A named relation reads left endpoint to right endpoint;
the opposite view uses its declared derived inverse in the same notation.

Formal constraints belong in the Definition Claim. Semantics explains their
meaning without adding a second Claim.

## Details

Named Relation Types require their own R/Type: Relation Definition authority.
The fenced `content.notation_for_subject` property is used only where a
Relation Type has a short Entity notation; no such short notation is invented
for a relation that uses the general named form. This Draft specifies no
parser, evaluator, function, formula expression, or bracketed condition.
