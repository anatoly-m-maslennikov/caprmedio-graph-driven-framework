---
atom_id: CA-R-2487
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 8
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Entity Definition
---

## Summary

Define CFEL

## Claim

CFEL (CAPRMEDIO Formal Expression Language) is the formal notation for
Subject addresses and fenced Formal Claims. CFEL is a model component beside
Graph and Carrier: Graph contains Nodes and Relations; CFEL addresses and
constrains them. CFEL syntax neither creates a Node, Relation, Property,
Carrier fact, Workflow step, nor evaluator result.

CFEL uses these graph-address forms:

- `X/Y` selects a narrower Primary Node; `X//Name` selects an existing
  instance of a Primary Node.
- `X.p` addresses Property p borne by X. In a Subject only,
  `X/(.p := V)` combines an admitted Property value with selection of X;
  `:=` is not a Formal-Claim value assignment.
- `Part +> Whole` and `Whole <+ Part` are opposite written views of one
  containment fact. `X >| Axis` and `Axis |< X` are opposite written views
  of one classification fact. `@X` references an already declared target.
- Parentheses group one expression. `;` separates complete expressions;
  a line break has no conjunction or disjunction meaning.

In Formal Claims, `X: Y` admits Y as an allowed value of X regardless of X's
kind or preceding path; it is not assignment. `=` and `!=` test conditions,
and `==` states a required or derived conclusion. `in` and `not in` are the
admitted membership tests. Numeric comparison and addition use the separately
defined `>`, `>=`, `<`, `<=` and `+`; they are distinct from Relation
operators. Property occurrence, direct-value, immediate-name
and recursive-name counts are distinct:

```CFEL
p{:occurrence}: [value format]{:value count};
p.*[name format]{:immediate name count};
p.**[name format]{:recursive name count};
p.*[name format]{:immediate name count}: [value format]{:value count}
```

`{:n}`, `{:n+}` and `{:n..m}` state allowed cardinality bounds on their
qualified selection; `{=n}` tests a count condition, `{>n}` tests whether the
actual count is greater than n using the existing numeric `>`, and `{==n}`
concludes a required or derived count. These test/conclusion forms are not
allowed bounds. A Relation has independent outgoing and
reverse cardinalities: `Source {:forward}((RELATION)){:reverse} Target`.
Omitted annotations are unspecified, not zero. `[format]` applies to direct
values; a name selector is not a value selector. A `p.**` count aggregates
selected distinct descendant Property identities below p within each selected
bearer, independently of direct values and other bearers.

The following named constructs are admitted only with the semantics in their
own CFEL Rules: `IF`/`THEN`, `UNIQUE`, `DETERMINES`, `COUNT`, `MAX`,
`LOOKUP`, `FENCED_LABELS`, and `?=`. `>>` is delivery notation with the
semantics of the delivery Rule; `!(selectors)` excludes branches from a
delivery selection. `Kind//$x` binds an existing selected instance and `$x.p`
reads its Property. Each non-graph CFEL operator has its own Declaration;
an operator is not a binary Node Relation. A Requirement/Declaration describes
a canonical or derived Relation direction; it does not authorize a second
stored inverse fact.

The reusable metadata family `@Operator//Name == "notation literal"` binds a
declared operator descriptor to its token or bounded construct spelling. Its
quoted right side is metadata, not an executed CFEL expression, value assignment,
state creation, or a new model entity.

Every Relation Declaration supplies Semantics. Relation Declarations use the
existing `==`, `>|`, and named-Relation tokens for short-notation,
Direct/Derived, and counterpart metadata.

A graph Relation connects declared model entities or declared instances,
including Carrier and CFEL; it is not limited to `Node/**`. A literal remains a
Property or allowed value, not a graph endpoint. A non-graph CFEL operator is
not itself a graph Relation, but its declared operator descriptor is a model
entity that may be a graph endpoint; an operator glyph or literal operand does
not create another model entity. Each Relation Declaration supplies Semantics and a
formal Host/Target signature with typed selectors whose universe is known, or
with declared variables bound to that universe. Within a Relation Declaration
Formal Claim only, `$host ((RELATION)) $target` is the reusable generic
signature: its untyped variables range over that declared entity-or-instance
universe and exclude literals. It declares neither a Relation fact nor instance
data. Known endpoint kinds remain typed selectors. This binding applies within Relation Declarations.

Concrete directional alternatives describe the same canonical Relation fact:
`Step ((IS_CONTAINED_BY)) Workflow` and
`Workflow <((IS_CONTAINED_BY)) Step`. The bare forward form
`Step ((IS_CONTAINED_BY)) Workflow` remains valid. In reverse writing,
normalization swaps canonical Source/Target and the two written endpoint count
slots. This syntax does not grant an inverse Relation permission. The Relation Declaration states the Host, Target and counterpart direction. `HAS_INVERSE` remains distinct from the confirmed
canonical-Relation-versus-derived-view policy; this Definition does not
introduce a placeholder Relation, metadata Node, or evaluator.

In RMED Claims, all formal content is a fenced block labelled `CFEL`. CFEL
body syntax and Markdown-fence-label parsing are separate concerns. This Definition
describes the admitted language contract; it does not claim a complete parser
or evaluator. An unimplemented construct remains an adoption and conformance
gap, not evidence that the construct has different semantics.

This Definition does not convert a Format, Bool value, or any other value
into an instance selected by `//`. Such an instance selection requires the
existing source binding that declares it. No value-format-to-instance rewrite
is implied by the CFEL overview.

## Details

Non-executable Relation-metadata illustration:

```text
((REL)) == <declared short notation>
((REL)) >| <Direct or Derived classification>
((REL)) ((counterpart Relation)) ((COUNTERPART))
```

