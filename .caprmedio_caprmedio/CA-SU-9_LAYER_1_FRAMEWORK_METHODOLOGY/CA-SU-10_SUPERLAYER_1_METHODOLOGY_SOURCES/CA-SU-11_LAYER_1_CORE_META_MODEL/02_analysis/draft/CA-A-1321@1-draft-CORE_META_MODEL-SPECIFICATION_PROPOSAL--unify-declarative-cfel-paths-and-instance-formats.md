---
atom_id: CA-A-1321
version: 1
status: Draft
role: Analysis
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
updated_at: 2026-11-05 03:55:43 +0400
carrier_destination:
  file:
    name: CA-A-1321@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--unify-declarative-cfel-paths-and-instance-formats.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Unify declarative CFEL paths and instance Formats

## Purpose

CFEL declares constraints, relationships and required values. Workflows and adapters perform changes. The notation below is a proposed successor; Current syntax remains active until its source revisions, review and migration are complete.

## Latest Operator input

- `/` expresses containment, like a folder path.
- `//` expresses narrowing with inheritance.
- A full Scope Unit path is one string built from actual declared Names, for example `/FRAMEWORK_ENGINE`. Project root is `/`.
- `[format, conditions]` constrains a value. Primitive formats include `int`; Model kinds also supply object Formats.
- `<Node>` explicitly refers to a Model-defined object kind. This spelling is accepted.
- `$<Node>` selects an anonymous instance; `$x[<Node>]` names an instance participant.
- A specific Model Relation uses the same filtered form: `$x[<Relation>, (.Name = IS_PROPERTY_OF)]`. The final user correction rejects `IS_PROPERTY_OF[<Relation>]`; the old `Relation//IS_PROPERTY_OF` instance meaning is not retained in the proposed syntax.
- CFEL consists of declarative statements, rather than a program with mutable variables or procedural calls.
- Allowed-value `:` becomes `::` everywhere in CFEL, including `{::1}` and `{::0+}`. Subject `:=` remains unchanged. YAML separators and literal colons retain their meanings.

## Current and proposed notation

| Meaning | Current | Proposed direction |
|---|---|---|
| Broader kind to narrower kind | `Node/Continuant/Atom` | `Node//Continuant//Atom` |
| Whole contains part | `Whole <+ Part` | `Whole/Part` |
| Typed instance participant | `Node//$x` | `$x[<Node>]` |
| Anonymous instance selector | `Node//` | `$<Node>` |
| Primitive Format and value conditions | `[int, 0..100]` | Same mechanism; `[int, 1+]` is a proposed positive-integer example |
| Reference to an object kind used as a Format | Bare kind in existing selector syntax | `<Node>` |
| Property access | `.` | Retain |
| Logical grouping | `()` | Retain |
| Allowed value / domain | `:` | `::` |
| Allowed cardinality | `{:n}` | `{::n}` |
| Qualified Subject selection | `:=` | Retain |
| Predicate test | `=` | Retain as a condition |
| Required value / definition | `==` described as assignment | Clarify as a declarative definition, without an action |
| Default | `?==` | Conditional definition for omission, with existing validation and no implicit Carrier write |

`Node//Atom` keeps the current path orientation: Atom is narrower than Node. The reverse notation remains a review question. Specific named Model instances are selected by Format and conditions.

## Declarative reading

- `$x` is a bound logical name, rather than a mutable program variable.
- A typed participant denotes an existing selected value or instance; it creates nothing.
- Universal quantification uses `FOR EACH $atom[<Atom>, (conditions)]:` followed by a parenthesized body. The paired `<Atom>` is retained. The selector carries the domain and conditions; `WITH` and `IN` are absent from this header.
- The participant is bound in its selector and body. It keeps one identity within that scope and is out of scope after the group. Existing no-shadowing rules remain.
- A Formal Claim states its participants, scope and constraints explicitly. `subjects.active` remains the Atom's declared focus; it supplies no implicit participant binding.
- `IF ... THEN ...` expresses implication. Current bounded-name introduction in IF remains authoritative; adding FOR EACH does not revoke that earlier decision.
- Mathematical terms describe values and invariants; they perform no I/O or business action. A conflicting supplied value fails its required-value constraint; the statement does not overwrite it. An authorized Workflow can separately change the supplied data.
- Existing explicit grouping for mixed AND/OR and quote/backslash rules remain applicable.

Illustrative successor expressions:

```CFEL
# model
CAPRMEDIO_MODEL/Node//Continuant//Atom;

# instances
$x[<Node>];
$atom[<Atom>, (.Header.Status = Active)];
$relation[<Relation>, (.Name = IS_PROPERTY_OF)];
$n[int, 1+];
```

## Allowed-value decision

The Operator selected `::` for allowed values and allowed cardinalities. `:=` remains the Subject qualification operator.

```CFEL
# model
Atom.Header.Role :: Method;
Atom.Header.ID :: [string]{::1};
```

These expressions declare allowed values, rather than test or replace a stored value. `=` tests a condition; `==` states a required or derived value; `?==` supplies a default when the effective value is missing. Preserve validation and absence rules. Separate allowed-value Declarations contribute the admitted alternatives.

The accepted migration includes Formats, Property-name constraints and `{::n}` bounds. It preserves `:=`, conditions, required values, YAML separators, quoted text and literal path strings. The four defining source previews are in the Epic packet's `coverage/declarative-notation-review/allowed-value-double-colon-20261105/` directory. Their actual Drafts are listed below and have passed bounded readback; source-consumer integration and review remain required before admission.

## Related reference decisions

- A base Atom ID such as `CA-P-123` identifies the ID shared by its Versions; lookup by that base selects Current by default.
- The proposed Term “Atom Reference” also covers `CA-P-123@3` for Archived and `CA-P-123@3-draft` for Draft. This suffix is address data, not restoration of the retired `@` entity-call operator.
- Header.Container remains one ordinary Property with a full Scope Unit path or base Atom ID. It has no duplicate entry under optional Header.Relations.
- Keep IS_CONTAINED_BY and CONTAINS available for Formal Claims. Their glyph changes are part of this notation proposal.

## Migration boundary

1. Resolve the remaining grammar questions one at a time.
2. Create and review defining Requirement/Declaration Drafts and affected RMED successors. List their actual IDs here after creation.
3. Update the Epic while retaining all 23 acceptance groups and external checks.
4. Push the reviewed source checkpoint before the mechanical migration.
5. Migrate by parsed context. Named-instance `//`, narrowing `/`, literal path strings and quoted text have different meanings.
6. Rebuild and verify all seven MODEL views against the final Source Versions.
7. CA #3 owns implementation, parser, fixtures and test execution. Workbench and Workflow owners retain their sources.

## Open design questions

- Reverse containment and narrowing traversal notation.
- Definitions and default cases must retain absence, validation and conflict safeguards in the revised operator sources.
- Complete the reviewed Scope Unit path source adoption and migration. Paths use actual declared Names, with Project root `/`; the old `/~ENGINE/...` was illustrative.

## Rationale

Containment paths resemble folder paths. Narrowing uses a separate separator. Formats share one mechanism for primitive values and Model object kinds. Angle brackets make the Model reference visible. Named participants express identity across constraints without introducing a program.

## Draft packet

Actual allowed-value notation Drafts:

- CA-R-2777@1-draft: `::` operator; replaces R2592 on adoption because its Summary changes.
- CA-R-2243@13-draft: allowed cardinalities.
- CA-R-2471@8-draft: notation distinctions.
- CA-R-2487@14-draft: CFEL overview.
- CA-R-1321@36-draft: Subject expression consumers.
- CA-R-2588@6-draft: default Relation cardinality consumers.
- CA-R-2778@1-draft: FOR EACH universal quantification.
- CA-R-2248@6-draft: object kinds as Formats.
- CA-R-2604@4-draft: typed bindings, anonymous selection and scope.
- CA-R-1931@19-draft: rebased separator and recursive-Step examples; legacy scope and coherence holds remain.

R2487@14-draft is rebased to include the typed-selector and FOR EACH changes while retaining the allowed-value changes.

These Drafts require source-consumer integration and review before promotion and contextual migration. Typed object-Format and binding Drafts have passed independent actual-Draft readback; coordinated adoption remains. The quantifier Draft alone does not admit those dependencies. Other proposed path and instance changes have no admitted successor yet. Existing source-repair Drafts remain separately tracked in CA-A-1318.

## Accepted quantifier shape

```CFEL
FOR EACH $atom[<Atom>, (.Header.Status = Done)]:
(
expression1;
expression2;
)
```

This is a syntax illustration. Its conditions and body are supplied by the authored Claim. The colon after the header introduces the group; `::` remains the allowed-value operator.
