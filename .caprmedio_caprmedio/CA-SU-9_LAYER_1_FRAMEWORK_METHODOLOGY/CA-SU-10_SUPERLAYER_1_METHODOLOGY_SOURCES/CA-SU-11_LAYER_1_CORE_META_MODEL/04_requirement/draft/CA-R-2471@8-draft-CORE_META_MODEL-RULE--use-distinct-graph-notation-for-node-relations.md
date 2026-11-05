---
atom_id: CA-R-2471
ref_id: CA-R-2471@8-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
version: 8
updated_at: 2026-11-05 00:49:39 +0400
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2471@8-draft-RULE--use-distinct-graph-notation-for-node-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Use distinct graph notation for Node relations

## Claim

### Prose Claim

In Subject addresses and Formal Claims, `X/Y` selects a narrower declared kind and `X//Name` an instance of a declared kind. A Property cannot narrow; it can have instances borne by corresponding data bearers. `X.p` addresses a Property borne by X; an unchanged inherited Property is resolved to its existing declaration rather than redeclared or given another bearer. In Subject addresses and filtered Node expressions in Formal Claims, `X/(.p := V)` admits V as a Property value and selects the whole Primary Node X where p equals V. The case does not exclude other allowed values from X.p. `(Node, Node.**)` selects Node and its recursive dependent Properties; it is not a narrowing assertion. Shared Node rules are declared once and inherited by applicable narrower Nodes.

`Part +> Whole` and `Whole <+ Part` are opposite written views of one composition fact, not narrowing. `X >| Axis` and `Axis |< X` are opposite views of one classification fact. `::` marks an allowed value. `=` tests a condition; `==` states a required or derived value. Parentheses group expressions; `in (a, b)` expresses membership. A bare Entity name refers to the existing target without copying or reparenting it.

For `Source {::left}((NAME)){::right} Target`, each optional bound constrains Relation instances at its written endpoint. Reversing the written view swaps the bounds. A Node-specific Claim addresses its active Node and its own bound; a Relation Declaration can state both intrinsic endpoint bounds. The opposite view requires its own applicable permission; a reverse written view does not grant permission. `{::n}` states an allowed cardinality. The same notation can constrain Properties, instances and Relations. Repeated references in a rule, including its conditions and conclusions, bind the same selected member. An omitted named Property occurrence cardinality does not require presence; applicable value constraints determine presence. Other omitted cardinalities are undefined, not implicit zero or permission.

`(Node, Node.**)` selects model Entities in the Node branch; it does not limit other declared Entities. `(Node//, (Node//).**)` is the instance-layer selector. `Node//` selects Node instances including instances of narrower kinds. `(Node//).**` selects recursive Property instances borne by a Node instance. Each is an instance of its corresponding model Property and has no independent Carrier. The two layers have separate permissions. Repeated instance matches count once by identity.

Subjects remain addresses and do not contain complete Formal Claims. In Subjects and filtered Node expressions in Formal Claims, `:=` combines allowed value and condition, including `Atom/(.Header.Role := Method)` and `Workflow/(.Purpose := Runtime)`; it does not write an instance value. Outside these selections, `::` and `=` retain their separate allowed-value and condition meanings. The withdrawn `..` form is not adopted.

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
