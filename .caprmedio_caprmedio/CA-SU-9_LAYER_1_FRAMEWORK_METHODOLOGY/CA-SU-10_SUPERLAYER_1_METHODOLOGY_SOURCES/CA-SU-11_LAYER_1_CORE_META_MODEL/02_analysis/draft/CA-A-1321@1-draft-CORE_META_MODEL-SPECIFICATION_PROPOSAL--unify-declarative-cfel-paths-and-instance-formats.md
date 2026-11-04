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
updated_at: 2026-11-05 00:00:18 +0400
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
- A full Scope Unit path is one string, for example `/~ENGINE/PROGRAMMATIC/...`.
- `[format, conditions]` constrains a value. Primitive formats include `int`; Model kinds also supply object Formats.
- `<Node>` explicitly refers to a Model-defined object kind. This spelling is accepted.
- `$<Node>` selects an anonymous instance; `$x[<Node>]` names an instance participant.
- CFEL consists of declarative statements, rather than a program with mutable variables or procedural calls.

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
| Predicate test | `=` | Retain as a condition |
| Required value / definition | `==` described as assignment | Clarify as a declarative definition, without an action |
| Default | `?==` | Conditional definition for omission, with existing validation and no implicit Carrier write |

`Node//Atom` keeps the current path orientation: Atom is narrower than Node. The reverse notation and named-instance reference form remain review questions, not accepted additions.

## Declarative reading

- `$x` is a bound logical name, rather than a mutable program variable.
- A typed participant denotes an existing selected value or instance; it creates nothing.
- Universal quantification states that a constraint holds for every matching participant. `FOR EACH` is a candidate ASCII spelling, not an execution loop.
- `IF ... THEN ...` expresses implication. It should not substitute for quantification by silently introducing a participant.
- Mathematical terms describe values and invariants; they perform no I/O or business action.
- Existing explicit grouping for mixed AND/OR and quote/backslash rules remain applicable.

Illustrative successor expressions:

```CFEL
# model
CAPRMEDIO_MODEL/Node//Continuant//Atom;

# instances
$x[<Node>];
$atom[<Atom>, .Header.Status = Active];
$n[int, 1+];
```

## Allowed-value candidate

The Operator questioned `:` because YAML uses it for a stored value binding. `~` is a candidate for “allows”; it is not yet adopted. Keep the distinction between admitting a value, testing a value and defining a required value.

The decision must also cover value Formats, wildcard Property names versus values, and cardinality markers. No blanket replacement of `:` is authorized by this proposal.

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

- New spelling for existing named instances such as Relation//IS_PROPERTY_OF; `//` is being reassigned to narrowing.
- Reverse containment and narrowing traversal notation.
- Exact declarative meaning of `==` and `?==`, including conflicting or omitted supplied values.
- Allowed-value spelling, including inside cardinality bounds.
- Explicit universal quantification and scope, preserving participant identity and the no-shadowing decision.
- Complete Scope Unit path encoding, including the Project root, segment Names and the `~` marker.

## Rationale

Containment paths resemble folder paths. Narrowing uses a separate separator. Formats share one mechanism for primitive values and Model object kinds. Angle brackets make the Model reference visible. Named participants express identity across constraints without introducing a program.

## Draft packet

This Analysis Draft records the design. No Requirement Draft for the proposed notation has been created or promoted yet. Existing source-repair Drafts remain separately tracked in CA-A-1318.
