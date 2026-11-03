---
atom_id: CA-R-2471
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Use distinct graph notation for Node relations

## Claim

In Subject addresses and Formal Claims, `X/Y` selects a narrower declared kind and `X//Name` an instance of a declared kind. A Property cannot narrow or instantiate. `X.p` addresses a Property borne by X; an unchanged inherited Property is resolved to its existing declaration rather than redeclared or given another bearer. In Subject addresses, `X/(.p := V)` admits V as a Property value and selects the whole Primary Node X where p equals V. The case does not exclude other allowed values from X.p. `(Node, Node.**)` selects Node and its recursive dependent Properties; it is not a narrowing assertion. Shared Node rules are declared once and inherited by applicable narrower Nodes.

`Part +> Whole` and `Whole <+ Part` are opposite written views of one composition fact, not narrowing. `X >| Axis` and `Axis |< X` are opposite views of one classification fact. `:` marks an allowed value. `=` tests a condition; `==` sets a value. Parentheses group expressions; `in (a, b)` expresses membership. `@X` refers to the existing target without copying or reparenting it.

For `Source {:n}((RELATION)) Target`, the cardinality constrains the allowed number of Relation instances at the written left-hand Source. Constrain a counterpart endpoint in its own applicable Declaration; a reverse written view does not grant permission or a cardinality. `{:n}` states an allowed cardinality. The same notation can constrain Properties, instances and Relations. Repeated references in a rule, including its conditions and conclusions, bind the same selected member. An omitted cardinality annotation leaves that cardinality undefined; it is not an implicit zero or permission.

`(Node, Node.**)` selects model Entities in the Node branch; it does not limit other declared Entities. `(Node//, (Node//).**)` is the instance-layer selector. `Node//` selects Node instances including instances of narrower kinds. `(Node//).**` selects recursive Property occurrences of a Node instance; it does not independently instantiate a Property kind. The two layers have separate permissions. Repeated instance matches count once by identity.

Subjects remain addresses and do not contain complete Formal Claims. In Subjects, `:=` combines allowed value and condition, including `Atom.Status := Draft` and `Atom/(.Role := Method)`; it does not write an instance value. Formal Claims retain separate `:` and `=` meanings. The withdrawn `..` form is not adopted; `::` has no assigned meaning here.

## Dependent selection

- `x.*`: immediate dependents.
- `x.**`: all dependents recursively.

A Property's full path determines its identity. Sibling names must be unique.

## Expression lists

Separate complete expressions with `;`. A line break is layout. Boolean groups remain one expression.

## RMED

RMED names these Roles:

- Requirement.
- Method.
- Evaluation.
- Delivery.

## Formal content

A fenced block labelled CFEL carries formal content inside Claim. In RMED Claims, all formal content must use that fence. The label replaces a separate Formal Claim heading.

## Inherited Node selection

- `Node.**` selects recursive dependent Properties.
- `(Node//).**` selects their occurrences on a Node instance.
- Node rules are inherited by applicable narrower Nodes.
- Commas combine selectors within one expression.
- Semicolons separate expressions.
