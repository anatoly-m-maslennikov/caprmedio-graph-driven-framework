---
atom_id: CA-R-2487
ref_id: CA-R-2487
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 16
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-2487-DECLARATION--define-cfel.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define CFEL

## Claim

### Prose Claim

CFEL (CAPRMEDIO Formal Expression Language) is the formal notation for
Subject addresses and fenced Formal Claims. CFEL is a model component beside
Graph and Carrier: Graph contains Nodes and Relations; CFEL addresses and
constrains them. CFEL syntax neither creates a Node, Relation, Property,
Carrier fact, Workflow step, nor evaluator result.

An `IF` membership condition can bind an unbound variable to each matching member of its declared selection; a variable already bound in the surrounding scope is tested against membership without rebinding. A parenthesized multi-line `THEN` body uses the same binding in each complete expression.

A `FOR EACH $x[<Kind>, (conditions)]: (...)` expression constrains every matching instance. A selector can omit conditions or use one simple condition without parentheses. The body groups complete expressions separated by semicolons. The binding is available in the selector conditions and its body. Within that scope, `$x.p` and `x.p` read the same participant Property. Nested bindings use distinct names. An empty selection satisfies the universal constraint. The header colon delimits the body.

In a Formal Claim, `#model` and `#instances` are ordering comments for the model and instance expressions that follow; they do not assert graph facts. A `$variable` explicitly binds an anonymous selected Entity or instance; repeated occurrences in its scope select the same identity. A typed selector supplies its universe; use model variables where model entities are intended. These bindings introduce no new binding operator.

CFEL uses these graph-address forms:

- `X/Y` selects a narrower Primary Node; `X//Name` selects an existing
  instance of a declared kind, including a Property instance borne by its data bearer.
- `X.p` addresses Property p borne by X. The Subject `X/(.p := V)` identifies the selected kind. A Formal Claim
  can select that scope with `X/(.p in (V))`. A declaration of the value states
  `X.p :: V;` explicitly.
- `Part +> Whole` and `Whole <+ Part` are opposite written views of one
  containment fact. `X >| Axis` and `Axis |< X` are opposite written views
  of one classification fact. A bare qualified address references its declared entity or instance. No `@` reference operator is required; `@N` identity/version tags retain their separate meaning.
- Parentheses group one expression. `;` separates complete expressions;
  a line break has no conjunction or disjunction meaning.

Text values use double quotes when needed to distinguish literal text from CFEL syntax; otherwise an unambiguous value may remain bare, including a multiword value such as `Scope Contract`. For example, `"A/B"` is text containing a slash. A name or path used as a reference retains its declared identity; a text value does not become a model reference. Within double-quoted text, `\"` represents a literal double quote and `\\` represents a literal backslash. Reject every other escape and any incomplete trailing backslash; JSON escape rules are not imported. This applies to values in Formal Claims and Subject selectors.

In Formal Claims, `X :: Y` admits the literal Y at the complete qualified address X. A declaration with an allowed-value Main Subject states the equivalent literal admission in its own Formal Claim. Literal admissions combine by OR within the applicable domain, including inherited values. Bracketed Formats and cardinalities constrain that domain and combine by AND. With no applicable literal admissions, the applicable constraints govern the value. `=` and `!=` test conditions, and `==` states a required or derived conclusion. `in` and `not in` are the
admitted membership tests. Numeric comparison and addition use the separately
defined `>`, `>=`, `<`, `<=` and `+`; they are distinct from Relation
operators. Property occurrence, direct-value, immediate-name
and recursive-name counts are distinct:

`{::n}`, `{::n+}` and `{::n..m}` state allowed cardinality bounds on their
qualified selection; `{=n}` tests a count condition, `{>n}` tests whether the
actual count is greater than n using the existing numeric `>`, and `{==n}`
concludes a required or derived count. These test/conclusion forms are not
allowed bounds. A Relation has independent outgoing and
reverse cardinalities: `Source {::forward}((RELATION)){::reverse} Target`.
A named Property has at most one occurrence per corresponding bearer; its applicable value constraints determine whether it is required. A present Property has a value, including nonempty child structure for a structural parent. `p :: {::0..1}` specifies a direct-value count with its applicable inherited format. Other omitted annotations are unspecified, not zero. `[format]` applies to direct
values; a name selector is not a value selector. A `p.**` count aggregates
selected distinct descendant Property identities below p within each selected
bearer, independently of direct values and other bearers.

The named constructs `IF`/`THEN`, `UNIQUE`, `DETERMINES`, `COUNT`, `MAX`,
and `FENCED_LABELS` are admitted with the semantics in their own CFEL Rules.
`LOOKUP(R, q)` and `?==` are admitted CFEL operators with their own operator
Declarations; the `?==` ordered-assignment Rule supplies its chain semantics.
Boolean `AND` and `OR` combine conditions; parenthesize mixed AND/OR
expressions to state their grouping explicitly. `>>` is delivery notation with the
semantics of the delivery Rule; `!(selectors)` excludes branches from a
delivery selection. `Kind//$x` binds an existing selected instance and `$x.p`
reads its Property. Each non-graph CFEL operator has its own Declaration;
an operator is not a binary Node Relation. A Requirement/Declaration describes
a canonical or derived Relation direction; it does not authorize a second
stored inverse fact.

The reusable metadata family `Operator//Name == "notation literal"` binds a
declared operator descriptor to its token or bounded construct spelling. Its
quoted right side is metadata, not an executed CFEL expression, value assignment,
state creation, or a new model entity.

A direct Relation Declaration owns shared meaning and endpoints. A derived inverse Declaration retains the reverse HAS_INVERSE binding and its own alias, when present. A qualified or other non-inverse derived view retains its source, endpoint transformation and qualification; derivation alone does not imply unconditional endpoint reversal. `alias(Relation//NAME) == "token"` binds exact Relation names to lexical notation. `Relation//DIRECT <--> Relation//DERIVED` binds distinct inverse Relations in the direct Declaration. It never equates their identities. These metadata forms do not create literal-to-Node graph links.

A graph Relation connects declared model entities or declared instances,
including Carrier and CFEL; it is not limited to `Node/**`. A literal remains a
Property or allowed value, not a graph endpoint. A non-graph CFEL operator is
not itself a graph Relation, but its declared operator descriptor is a model
entity that may be a graph endpoint; an operator glyph or literal operand does
not create another model entity. Each direct Relation Declaration supplies shared meaning and a
formal Host/Target signature with typed selectors whose universe is known, or
with declared variables bound to that universe. Within a Relation Declaration
Formal Claim only, `$host ((RELATION)) $target` is the reusable generic
signature: its untyped variables range over that declared entity-or-instance
universe and exclude literals. It declares neither a Relation fact nor instance
data. Known endpoint kinds remain typed selectors. This generic Relation signature binding applies within Relation Declarations; typed bindings can also select model entities where their universe is declared.

Concrete directional alternatives describe the same canonical Relation fact:
`Step ((IS_CONTAINED_BY)) Workflow` and
`Workflow <((IS_CONTAINED_BY)) Step`. The bare forward form
`Step ((IS_CONTAINED_BY)) Workflow` remains valid. In reverse writing,
normalization swaps canonical Source/Target and the two written endpoint count
slots. This syntax does not grant an inverse Relation permission. The Relation Declaration states the Host, Target and applicable counterpart direction. `HAS_INVERSE` applies to inverse Relations; a qualified non-inverse derived view retains its source, transformation and qualification.

In RMED Claims, all formal content is a fenced block labelled `CFEL`. CFEL
body syntax and Markdown-fence-label parsing are separate concerns. This Definition
describes the admitted language contract; it does not claim a complete parser
or evaluator. An unimplemented construct remains an adoption and conformance
gap, not evidence that the construct has different semantics.

This Definition does not convert a Format, Bool value, or any other value
into an instance selected by `//`. Such an instance selection requires the
existing source binding that declares it. No value-format-to-instance rewrite
is implied by the CFEL overview.

`Relation//IS_DECLARED_BY` is the qualified derived view of a GOVERNS fact whose source is a Requirement/Form Declaration; it reverses that selected fact while retaining the qualification. It is not a general inverse of GOVERNS or a permission for every Relation.
### Formal Claim

```CFEL
# model
p{::occurrence}:: [value format]{::value count};

p.*[name format]{::immediate name count};

p.**[name format]{::recursive name count};

p.*[name format]{::immediate name count}:: [value format]{::value count}
```

