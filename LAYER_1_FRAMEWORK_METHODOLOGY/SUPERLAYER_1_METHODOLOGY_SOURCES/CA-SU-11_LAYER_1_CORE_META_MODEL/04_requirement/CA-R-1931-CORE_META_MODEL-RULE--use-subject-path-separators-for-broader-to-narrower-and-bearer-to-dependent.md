---
atom_id: CA-R-1931
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL
  passive:
  - Term//Property
  - Entity/Property
  - CFEL <+ Relation//IS_PROPERTY_OF
  - CFEL <+ Relation//HAS_CLASSIFICATION
  - Entity
  - Entity/Object/Continuant/Package <+ Module <+ Code Unit
version: 18
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Rule
---
## Summary

Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent

## Claim scope

a Entity Path.

## Claim

In an Entity Path, `/` separates a broader kind from its narrower kind; `//`
separates an Entity kind from a named instance; `.` separates a bearer from a
dependent Property; and `:` separates any `X` from its allowed literal value
`Y`, irrespective of X's kind or path. `@` calls an already declared Entity;
it is not limited to kinds and declares no target. Parentheses provide logical
grouping.

`Part +> Whole` and `Whole <+ Part` are opposite writings of the same
containment fact. Its direct fact is Part IS_CONTAINED_BY Whole, and CONTAINS
is derived. `X >| Y` and `Y |< X` are opposite writings of the same
HAS_CLASSIFICATION fact, with Entity Y used as an applicable Classification
axis rather than belonging to a separate Classification Entity kind. This Rule does not
invent an inverse canonical Relation Type for HAS_CLASSIFICATION.

`X/(.Y: Z)` denotes a narrower kind of X qualified by its own Property Y
and value Z. The leading dot inside parentheses is relative to X: `.Y`
addresses `X.Y`. The qualified X inherits X's applicable features and
constraints. The Property is the qualification condition; it does not become
a narrower kind of its bearer. This form replaces the proposed classification
Property category and the earlier bare `X/Y: Z` qualification spelling.

`Source ((RELATION_TYPE)) Target` expresses a defined named Relation. Persist
the direct fact once and show its declared derived inverse only as a derived
view. Entity syntax neither creates target identities nor admits native facts
without defining authority. A defining Atom may introduce its governed Entity.

Cardinality uses `{n}`, `{n+}`, and `{n..m}`. Direct Property values retain
their post-Property notation, for example `X.Y[format]{n}`. A Relation has two
independent directional slots: `Source {forward-count}RELATION{reverse-count}
Target`. The pre-operator slot constrains Relation instances in the written
Source-to-Target direction per Source; the post-operator slot independently
constrains the reverse count per Target. These are not distinct-target counts. For example, `Step {1}+>{1+} Workflow` requires one Workflow per
Step and one or more Steps per Workflow; its reverse writing is
`Workflow {1+}<+{1} Step`. `Property {1}((IS_PROPERTY_OF)) Bearer` requires
exactly one outgoing IS_PROPERTY_OF Relation for each Property occurrence;
postfix-only `{1}` would instead constrain the reverse count per Bearer.
Each Relation is binary and connects two endpoint nodes or node instances.
The slots count Relation instances, not Relation arity; omitted slots remain
unspecified. This Relation counting is independent of the Property's
direct-value Format and cardinality.
Advanced functions, formulas, interpolation, and bracketed conditions are out
of scope.

### Formal claim

```text
Entity/Object/Continuant/Package <+ Module <+ Code Unit
Atom/(.Content Role: Operations)/(.Type: Step) {1}+>{1+} Atom/(.Content Role: Operations)/(.Type: Workflow)
Atom/(.Content Role: Operations)/(.Type: Sub-step) {1}+>{0+} Atom/(.Content Role: Operations)/(.Type: Step)
Atom/(.Content Role: Method)
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Draft <+ Draft
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Archived <+ Archived
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)
Source ((RELATION_TYPE)) Target
```

## Semantics

`/` is specialization and supplies inheritance. `+>` and `<+` are containment
and do not supply inheritance, sequence, or a property relation. `//` names
an instance of a kind; `.` addresses a dependent Property; and `:` declares
an allowed value rather than assigning one. A reference marker calls an
already declared Entity and creates neither an alias nor a duplicate.

`X.Y` addresses Property Y, and `X.Y: Z` expresses its allowed value.
`X/(.Y: Z)` instead identifies qualified X entities. For example,
`Atom/(.Type: Method)` means an Atom with the stated Type qualification, not
the Type Property inheriting Atom's features. This syntax example alone does
not admit Method as a Type value; the existing Content Role use is written
`Atom/(.Content Role: Method)`. Every qualification still requires its own
admitted Property and allowed value. Existing Carrier keys and encodings
remain governed separately by Delivery; the notation adds no nested object.

Status Group classifies Atom Statuses through
`Atom.Status >| Status Group`. The following `<+` expressions describe each
group's Status parts. In this
mapping, `* not in (Draft, Archived)` selects admitted Atom Status values
other than Draft and Archived. It does not admit new Status values, missing
values or a general expression language. Containment does not imply
inheritance; the Property-qualified Atom kind inherits through `/`.

## Details

Each Module belongs to exactly one Package; Project Implementation is the
parentless root Package and a nested Package belongs to another Package. Step
belongs to Workflow; Step and Sub-step are distinct. Scope Unit has structural
parts expressed as `Scope Unit <+ @(Scope Unit)`, `Scope Unit <+ @(Atom)`, and
`Scope Unit <+ @(Projection)`.

Backslash escapes the next literal name character. Single/double quotes are
carrier serialization, not Entity delimiters. One globally unique primary
kind name and one canonical declaration path are required; migration does not
retain aliases. Term-path reconciliation remains subject to C605.

These Operator-approved notation changes are Draft proposals. The grammar,
authoring and evaluation consumers need coordinated reconciliation before
adoption; no Current operator or executable parser is changed here.
