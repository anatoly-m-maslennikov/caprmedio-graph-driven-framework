---
atom_id: CA-R-2471
ref_id: CA-R-2471
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 10
updated_at: '2026-11-11 16:04:42 +0400'
carrier_destination:
  file:
    name: CA-R-2471-CORE_META_MODEL-RULE--use-distinct-graph-notation-for-node-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Use distinct graph notation for Node relations

## Claim

### Prose Claim

In Subject addresses and Formal Claims, `X/Y` selects a narrower declared kind and `X//Name` an instance of a declared kind. A Property cannot narrow; it can have instances borne by corresponding data bearers. `X.p` addresses a Property borne by X; an unchanged inherited Property is resolved to its existing declaration rather than redeclared or given another bearer. The Subject `X/(.p := V)` identifies the selected Primary Node X. Inside a Formal Claim, use `X/(.p in (V))` for the corresponding selection condition. A declaration of the value states `X.p :: V;` separately. `(Node, Node.**)` selects Node and its recursive dependent Properties; it is not a narrowing assertion. Shared Node rules are declared once and inherited by applicable narrower Nodes.

`Part +> Whole` and `Whole <+ Part` are opposite written views of one composition fact, not narrowing. `X >| Axis` and `Axis |< X` are opposite views of one classification fact. `::` admits a literal or states a Format or cardinality constraint, according to its right operand. `=` tests a condition; `==` sets a value. Parentheses group expressions; `in (a, b)` expresses membership. A bare Entity name refers to the existing target without copying or reparenting it.

For `Source {::left}((NAME)){::right} Target`, each optional bound constrains Relation instances at its written endpoint. Reversing the written view swaps the bounds. A Node-specific Claim addresses its active Node and its own bound; a Relation Declaration can state both intrinsic endpoint bounds. The opposite view requires its own applicable permission; a reverse written view does not grant permission. `{::n}` states an allowed cardinality. The same notation can constrain Properties, instances and Relations. Repeated references in a rule, including its conditions and conclusions, bind the same selected member. An omitted named Property occurrence cardinality does not require presence; applicable value constraints determine presence. Other omitted cardinalities are undefined, not implicit zero or permission.

`(Node, Node.**)` selects model Entities in the Node branch; it does not limit other declared Entities. `(Node//, (Node//).**)` is the instance-layer selector. `Node//` selects Node instances including instances of narrower kinds. `(Node//).**` selects recursive Property instances borne by a Node instance. Each is an instance of its corresponding model Property and has no independent Carrier. The two layers have separate permissions. Repeated instance matches count once by identity.

A Declaration states its Model identity and applicable placement in the Formal Claim. Use a named Relation for narrowing or containment. A complete Property path identifies its bearer, and a typed instance address identifies its kind. State a Property’s applicable format and cardinality at that path. State any required qualification in the expression. Subjects identify the Atom’s topic.

An allowed-value declaration states its complete qualified literal admission in the Formal Claim. When the declaration constrains instances, a separate `FOR EACH` expression binds its participants and supplies the instance scope.

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

A Formal Claim is a declared child of an ordinary RMED Claim and contains formal content in a fenced block labelled CFEL. Formal content in an ordinary RMED Claim belongs in Formal Claim. Prose Claim contains ordinary Markdown. A heading in a Markdown value does not declare a Property by itself. Unknown headings, including `##` headings, within Prose Claim remain part of that value and do not terminate it.

## Inherited Node selection

- `Node.**` selects recursive dependent Properties.
- `(Node//).**` selects their occurrences on a Node instance.
- Node rules are inherited by applicable narrower Nodes.
- Commas combine selectors within one expression.
- Semicolons separate expressions.
