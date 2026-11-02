---
atom_id: CA-A-draft
content_role: Analysis
type: Specification Proposal
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax
version: 1
updated_at: 2026-10-30 06:45:02 +0400
relations: {}
tier: 3
---
## Summary

Notation baseline for intuitive symbol review

## Question

Which short keyboard notations make these meanings easiest to read correctly?

## Scope

Latest Operator-agreed meanings, including Draft changes. Latest human input
supersedes earlier wording. This is review input, not Current adoption or
evidence of parser support.

## Approach

Use this baseline explicitly; do not infer meanings from other languages.
The Astra-max comparison is complete. The Operator then selected the
Composition and Classification spellings below and clarified two-sided
Relation cardinality. Use compact English-keyboard symbols while balancing
visual readability and intuitive understanding. No qualification replacement
has been selected; `/`, `()` and `.` retain their meanings.

## Results

### Meaning baseline

| Notation | Meaning |
|---|---|
| `X/Y` | Y is narrower than X and inherits X's applicable features and constraints. |
| `Part +> Whole` | Part is part of Whole. The pointer faces the Whole; containment supplies no inheritance. |
| `Whole <+ Part` | Whole has Part: the reverse written view of the same containment fact. The pointer still faces the Whole. |
| `X >\| Y` | X has Classification Y. The pointer faces the Classification endpoint, marked by the bar. This is axis applicability, not membership in a particular group. |
| `Y \|< X` | Y is the Classification applicable to X: the reverse written view of the same fact. |
| `X.Y` | Y is a Property borne by X. |
| `X: Y` | Y is an allowed value of X, regardless of X's kind or preceding path. This is not assignment and does not imply that X is a Property. |
| `X/(.Y: Z)` | An X qualified by its own Property Y and allowed value Z. The qualified X inherits from X; Y does not become a subtype of X. |
| `K//Name` | The named instance Name of kind K, not a narrower kind. |
| `[format]` | Declared Format of a Property's direct values. |
| `x.y[format]{cardinality}` | Format and count of the Property's direct values: `{n}` exactly n, `{n+}` at least n, `{n..m}` inclusive range. |
| `Source {f}RELATION{r} Target` | Two independent directional counts: f constrains links from each Source toward Target; r constrains reverse links from each Target toward Source. An omitted side is unspecified. These do not count Relation arity. |
| `@` | Call/reference to an already declared Entity; it does not declare a new Entity. |
| `()` | Logical grouping of the enclosed expression, including relative Property qualification. |
| `Source ((RELATION_TYPE)) Target` | A named Relation with its declared direction and endpoints. The double-parenthesis form is a distinct compound notation. |

### Examples and boundaries

```text
Atom.Status >| Status Group: Draft <+ Draft
Atom.Status >| Status Group: Archived <+ Archived
Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)

Step {1}+>{1+} Workflow
Workflow {1+}<+{1} Step
```

Status Group classifies Atom Status values. Each group contains the Status
values shown on its right. `*` ranges only over admitted Atom Status values.
These three groups are mutually exclusive and exhaustive within that domain.
The wildcard mapping is Formal claim text; it does not introduce an executable
Boolean or query grammar for Subjects.

The last two lines are equivalent: each Step belongs to exactly one Workflow,
and each Workflow has one or more Steps. Reversing the written direction
swaps the two count positions. Missing counts remain unspecified; property
value counts remain separate. This supersedes the former Relation convention
where a single postfix count always counted outgoing links from the left.

`Atom/(.Type: Method)` denotes the whole qualified Atom, which inherits from
Atom. This notation example alone does not admit Method as a Type value;
the admitted Content Role example is `Atom/(.Content Role: Method)`.

Containment retains direct IS_CONTAINED_BY and derived CONTAINS.
`>|` retains HAS_CLASSIFICATION, and `|<` is its selected reverse view.
Choosing that view introduces no separately authored reverse fact or new
canonical inverse Relation Type name. The selected spellings replace bare
`>` / `<` containment and the earlier `::` axis spelling. The selected
Composition pointer faces the Whole, superseding the opposite direction in
the FPF report's earlier conditional `+>` candidate; that report stays unchanged.

### Authorized adoption and migration

The Operator requests: update/review/fix the full Term/Property proposal,
promote the reviewed closed batch to Active, then migrate Current notation.
The scope includes the 125-Draft packet and required notation owners; it
preserves the accepted Property relation and Method-owned Term definitions.

Classification is not a new Entity kind. HAS_CLASSIFICATION and
IS_CLASSIFIED_BY are named Relation instances under Graph Syntax; a generic
Classification word definition, if needed, belongs to Terms. No inverse pair
is inferred merely from listing those two Relation names.

Review and repair stale successors from their live Current owners before
promotion. Use the admitted lifecycle/identity-allocation path, preserve
archived/history bytes, migrate only reviewed expressions, update parser and
consumers together, and rebuild derived projections. A source/promotion
record alone does not establish implementation or migration success.

### Source alignment

The table incorporates generic `:`, `@` for an already declared Entity,
logical grouping `()`, the selected symbol pairs and two-sided Relation
cardinality. The repaired full proposal now has a 130-Draft adoption closure,
including the 125-Draft register and five required notation owners. Older
Current wording remains migration work; it does not override the latest human
decisions. Draft preparation does not establish Current adoption.

Approved AST support and its graph, lookup and validator callers are prepared
in source. Ten focused parser tests pass. Installed runtime activation,
Current publication and migration have not occurred. Broader test runs have
separate filesystem limits; they are not an all-green certification.

Supporting Drafts: [notation](../../04_requirement/draft/CA-R-1931@17-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md),
[HAS_CLASSIFICATION](../../04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-classification.md),
and [Format/cardinality](../../04_requirement/draft/CA-R-2243@3-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality-notation.md).

## TLDR

The selected pairs are `Part +> Whole / Whole <+ Part` and
`X >| Y / Y |< X`. Relation counts constrain both directions independently;
Property value counts stay postfix. Source parser checks pass; adoption and
Current notation migration remain pending actual lifecycle execution.
