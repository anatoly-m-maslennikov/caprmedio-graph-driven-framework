# Candidate #3 — Object, Term, Selection

Status: Candidate; not adopted Core authority.

Saved: 2026-10-11, Asia/Tbilisi.

Updated: 2026-10-12, Asia/Tbilisi — optional Atom Semantics.

Basis: the Operator's latest decisions in this conversation. This document
supersedes the wording of candidate #2 presented in chat, which was not saved.
The [older saved candidate](operator.entity-graph.candidate.json), captured
706-identity review, source pins and receipts remain unchanged.

This is a full conceptual model, not a completed remapping of every old Subject.
It does not change authoritative Atoms, Project Structure, parsers, storage keys,
native relation admission or runtime state.

## 1. Base model

```text
Entity
  /Object
    /Occurrent
    /Continuant
  /Term
  /Selection
```

- **Entity:** the umbrella for the things represented by this model.
- **Object:** something whose identity, state or relations we track.
- **Term:** a name with a meaning in its context.
- **Selection:** an expression choosing existing Entities, such as Objects or Terms.

Terms describe meaning. Objects represent things. Selections choose things.

These are model categories, not a claim that Terms or Selections do not exist.
A Term can name an Object kind or a concept that has no additional Object node.
The Term and the Object it names are not interchangeable.

General and CAPRMEDIO-project entries are two views of this same model, not two
sources of truth. General means reusable across projects. Project-specific means
CAPRMEDIO as the product being developed, not framework-wide rules merely used
by this project.

### Notation

- `/`: broader kind to narrower kind.
- `.`: bearer to dependent Object.
- `:`: Property to allowed value, not assignment.
- No `@` relation operator. An archived Atom ID may end in `@<Version Number>`;
  that is an ID suffix, not Subject relation syntax. Delivery policies define
  storage conventions.

Indentation outside a taxonomy is grouping or ownership, not an inferred `/` edge.
The relation meanings shown here are candidate meanings, not newly admitted
native relation names.

## 2. Objects

### 2.1 General Objects

```text
Object
  /Occurrent
    /Execution
      .Execution ID
      /Action Run
      /Step Run
      /Workflow Run
    /Session

  /Continuant
    /Artifact
      /Atom
        .ID
        .Summary
        .Status
        .Substance
        .Substance Scope
        .Semantics
        .Details
        .Content Role
        .Type
        .Governance Locus
        .Global Tier
        .Local Tier
        .Version Number
        .Updated At
      /Projection
        .Source References

    /History
      /Revision
      /Journal
        .Record

    /Scope Unit
      .ID
      .Name
      .Label
      .Structural Level
      .Type
        : Ordered
        : Unordered
      .Local Order
      .Navigational Order Number

    /Actor
      .Actor Type
        : Operator
        : AI Agent
      .Name

    /Carrier
      .Carrier ID
      /File Carrier
        .Filename
        .Path
      /Directory Carrier
        .Path

    /Relation
      .Relation Type
      .Source Reference
      .Target Reference
```

An Occurrent happens or unfolds in time. A Continuant keeps its identity through
time. Duration and having a file do not decide the classification: a temporary
file is a Continuant Carrier; a long-running Workflow Run is an Occurrent.

#### Artifact and dependent Objects

- An Artifact is one governed lifecycle unit.
- An Atom is the smallest independently governed Artifact.
- A Projection is derived and does not become authority for its source facts.
- Properties are dependent Objects. They need a bearer, not a separate Carrier
  or independent lifecycle.
- An Atom may be represented by one folder and one file with different roles:
  the folder organizes children; the file contains its classic content. This
  does not require every Atom to have both.
- Each Object instance has one representation. A Projection instance is not
  another representation of its source instance.

The tree shows available fields, not a new universal mandatory schema. Summary
and Status are mandatory for every Atom. Other fields are conditional; existing
role or Type rules can require them.

Substance is the primary content. Claim, Objective, Question, Issue and Operation
are role-specific labels. Substance Scope may be omitted only when Substance
covers the whole governed Subject AND the whole owning Scope Unit. Otherwise it
is explicit. General Details are optional; typed required content remains required.

Atom content has distinct purposes:

- **Substance:** what the Atom states.
- **Substance Scope:** where that content applies.
- **Semantics:** optional meanings of the Terms and values this Atom defines
  within its stated scope.
- **Details:** examples, rationale and supporting explanation; not another
  competing place to define meanings.

Semantics is governed content, not commentary. It shares the Atom's authority,
scope, Status, Version and lifecycle. It supports the same authority unit;
unrelated or independently governed Claims are not hidden in this section.

Define a meaning once in its owning Atom's Semantics. Other Atoms reference
that meaning rather than copy or silently redefine it. Referring to a Term does
not make the referring Atom another definition owner.

Illustrative content for the Atom governing Status, not adopted Status definitions:

```text
Semantics
  Draft: not yet accepted for active use.
  Archived: retained, but outside the current active view.
```

This can replace separate definition Atoms whose only job is to repeat a meaning
that belongs to this same authority unit. Keep a separate definition Atom when
the meaning needs independent scope or governance. No existing definition Atom
is retired or deleted by this candidate update.

An Atom subtype inherits Atom obligations. It does not need duplicate definitions
of those obligations. Inheriting a Carrier obligation does not mean sharing one
physical Carrier. General D policies can cover multiple Properties and Objects.

Content Role, Type, tiers and internal/external/relational Governance Locus remain
Properties or classifications, not additional Object roots. I remains actual
Implementation; this candidate creates no Implementation Atoms.

#### History

- History means preserved information, not the events themselves.
- Revision is a preserved historical state, not the change that produced it.
- Journal records changes, executions, decisions and outcomes.
- Journal also qualifies as Artifact. It is one Object with both classifications,
  not two copied Journal nodes.
- History is not below Artifact. Revision is neither an Artifact nor an
  Artifact-borne Property; no recursive Revision-of-Revision rule is introduced.
- A Journal Record is a dependent stored record. It is not the event it describes.
- Git preserves Atom contents and versions. Journals register what happened.

#### Scope Unit, Actor, Carrier and Relation

- Scope Unit owns Atoms and child Scope Units; it is outside any individual Atom.
- Actor identifies who performs work. Name is optional; an unnamed Actor Type
  names a generic role, not a uniquely distinguished performer.
- Carrier identifies what carries a representation. Its filename/path is a
  location, not identity. General D policies govern field/storage mappings.
- Relation remains the selected connection concept. An ordinary relation fact
  is an edge; describing a declaration does not require a second independently
  managed node for every edge. Each declaration stays with its declaring Object.
- Status changes do not silently erase relations. Impact checking and repair
  are separate work; unresolved relations are reported before being relied on.

#### Identity, versions and lookup

| Item | Identity or reference |
| --- | --- |
| Current, non-archived original Atom | `Atom.ID`: `(project prefix)-(Content Role first letter)-(number)` |
| Archived Atom state | the same base ID + `@` + Version Number, e.g. `CA-P-123@3` |
| Scope Unit | `Scope Unit.ID`: `(project prefix)-SU-(number)` |
| Carrier | Carrier ID; not filename/path |
| Execution | Execution ID |
| Actor | Actor Type + optional Name; individual unnamed distinctions deferred |
| Dependent Object | bearer identity + dependent name |
| Historical Atom lookup | version-qualified ID, e.g. `CA-P-123@3` |
| Other unversioned Artifact state | Artifact ID + Updated At |

Example dependent identity: `atom(atom_id="CA-R-123").status` within the selected
source or Projection view. `Atom` is the Object kind. Lowercase `atom(...)` remains
distinct case-sensitive selector syntax, not an alias or an enumeration operation.

The semantic display names are `Atom.ID` and `Scope Unit.ID`. This does not rename
storage keys or the `atom_id` selector argument.

```text
Current / Active Atom
  Atom.ID = CA-P-123

Archived version 3
  Atom.ID = CA-P-123@3

Archived version 4
  Atom.ID = CA-P-123@4
```

The part before `@` is the stable base/lineage ID. The complete archived ID
identifies one historical state. This supersedes the earlier candidate wording
that allowed multiple archived originals to carry the same unqualified Atom ID.
The suffix must agree with Version Number; it is not another independent counter.

Every Atom update increments Version Number by one: 1, 2, 3, 4. The previous
version becomes archived history; the new current version is Active in the
agreed source-version transition. Archived history does not permanently archive
the base ID or transfer its Status to future versions.

Across non-archived original authoritative Atom folders together, at most one
original carries a base ID. Archived originals are distinguished by their full
version-qualified IDs. Default lookup covers Active originals; historical lookup
uses an ID such as `CA-P-123@3`. Existing non-archived status containers remain
inside the current-original uniqueness boundary. Drafts have no assigned Atom
IDs; no Draft semantic deduplication policy is added.

Projected instances still belong to separate views; an original and its derived
copy do not become one Object merely because they share a base ID. Active copies
use the source base ID; Archived copies qualify it with their source Version
Number. Within one view, the complete ID distinguishes archived versions.

Scope Unit ID stays stable when Label, Name or path changes. Metadata folder names
retain `(project prefix)-SU-(number)-(LABEL)-(NAME_NAME)`. Project-root delivery
folder names stay as they are. Carrier ID syntax/assignment remains authoring work.

### 2.2 CAPRMEDIO project Objects

These are concrete project components, occurrences or specializations of the
general model. They do not introduce another root for every feature.

#### Project Scope Units

Ownership outline from [Project Structure](../../../project_structure.toml):

```text
CAPRMEDIO Project
  Framework Methodology
    Methodology Sources
      Core Meta-model
      Installed Extensions
      Project Configuration
    Applicable Methodology production
  Framework Engine
    Programmatic
      Tools
      Project Tools
      Apps
        Workflow Orchestrator
      MCP
    Agentic
      Skills
      Prompts
  Operator Documentation
  Core Extensions
  Releases
  Community Extensions
  Field
```

This is an ownership outline, not a new Project Structure declaration. Actual
accepted child units come from Project Structure, not from arbitrary folders.

#### Project Artifacts and History

```text
Authoritative Artifacts
  Project Settings
  Project Structure
  Framework Instance Settings
  Original project Atoms
    Core Meta-model Atoms
    Extension Atoms
    Project Configuration Atoms
    Product RMED and Operations definitions

Derived Projections
  Applicable Methodology
    projected Atom members
  Objects Graph — proposed name for the former Entities Graph
  Atom Subjects Graph
  Terms Graph
  Scope Unit Graph
  Requirement Lineage Map
  Implementation Overview
  Realization Graph
  compiled Prompts and context documents

Implementation Artifacts
  methodology compiler
  graph builders
  discovery and Atom-operation Tools
  Workflow Orchestrator implementation
  MCP implementation
  ca entry Skill
  Prompt/Skill definitions
  release and installation packages

Project History
  Project Work Journal
  preserved Artifact Revisions

Project Carriers
  source files and directories
  configuration files
  package files
  databases and other stored representations
```

A component's specification, executable implementation, actual run and derived
output are different things. A source file does not prove a running service,
installed Extension or completed execution. Graph App and Codex Plugin remain
planned product candidates, not automatically accepted Scope Units or live components.

#### Applicable Methodology

```text
Core + installed Extensions + Project Configuration
  → select the source Atoms
  → project each selected source Atom one-to-one
  → place projected members in Active or Archived according to applicability
  → record applicability and conflict-resolution decisions
```

Each derived member preserves its source base/lineage ID, Version Number and
relative source link. Its own ID follows the Active/Archived format above;
the source reference still identifies the exact original source state. This
refines the earlier literal-ID-copy rule for Archived projected members, without
creating another source Atom or incrementing the source Version Number.
Exact source-state provenance must not be reduced to an unversioned link.
The whole Projection has one lifecycle and its own rebuild tracking.

Not every member is Active. Excluding a projected member does not mutate its
original source. Conflict resolution can create a new authored original Atom
in Project Configuration; that original can then be projected one-to-one.
Multiple originals are not merged into one projected Atom.

The Journal records the Atom IDs projected to Active, projected to Archived,
or created in Project Configuration. Git preserves their contents and versions.
An applicability exclusion and an archived historical version are different.

The production Scope Unit and the delivered Applicable Methodology Projection
are separate Objects. The Projection does not replace Core, Extension or
Configuration source authority. This later design direction is not claimed to
be already adopted by the active-only compilation wording in current Core.

#### Project Occurrents

When they actually happen:

```text
Executions
  Applicable Methodology compilation
  graph construction
  Atom lookup, update or validation
  context and Prompt assembly
  implementation and evaluation work
  release and installation
  service startup and operation

Sessions
  Operator–Agent sessions
  bounded delegated sessions
```

Reusable procedures are O Atom definitions. Their performances are Executions.
Ad hoc work does not require a new O Atom; the Operator decides repeatability.
A service startup does not, by itself, create a Workflow Run.

## 3. Terms

### 3.1 General Terms

Terms name both Object kinds and concepts without additional Object nodes.
These groups organize vocabulary; they are not new native Term hierarchies.

```text
Object-kind names
  Object, Continuant, Occurrent
  Artifact, Atom, Projection
  History, Revision, Journal
  Scope Unit, Actor, Carrier, Relation
  Execution, Session

Content concepts
  issue, question, objective, rationale
  required outcome
  method
  evaluation criterion
  delivery convention
  operation semantics
  constraint

Classification vocabulary
  Content Role and Type names
  tier names
  internal, external, relational
  registered Status and other allowed values
  Relation Type names

View and authoring concepts
  applicability, coherence, precedence
  hierarchy, ownership, inheritance
  validation, grouping, layout, ordering
  notation and serialization conventions
```

For example, `Atom` names an Object kind; `Method` names a Content Role/concept.
A particular Method Atom is an Object. Naming Method does not create a separate
Method Object root. A Term's meaning can be defined in its owning authoritative
Atom's Semantics without making the Term and that Atom the same instance.

The Terms Graph can derive these definitions from Semantics, retaining the
source Atom ID, Version Number and definition scope. It remains derived, not
another definition authority. Already separate definitions remain source facts
until their replacement is explicitly approved; this document does not claim
Semantics extraction or duplicate/conflict checking is implemented.

Registered allowed-value domains and admitted nodes remain preserved. A raw
scalar is not automatically a new Term or Object. `:` retains its allowed-value
meaning; it is not assignment syntax.

A label or alias does not create another Object. Syntax characters, selector
keywords/keys and identifier literals are not automatically Terms either.
The Terms Graph is distinct from the Objects Graph; no new cross-graph native
relation is admitted by this document.

### 3.2 CAPRMEDIO project Terms

```text
Product and component names
  CAPRMEDIO
  Core Meta-model
  Applicable Methodology
  methodology compiler
  Workflow Orchestrator
  MCP and ca
  Objects Graph and Terms Graph

Methodology concepts
  source eligibility and selection
  source frontier
  applicability and coherence
  conflict resolution and precedence
  one-to-one Atom derivation
  source authority and derived output

Graph concepts
  Subject interpretation
  supported relation admission
  hierarchy versus bearer qualification
  inherited obligations
  R skeleton, M methods, E checks, D delivery

Harness and delivery concepts
  context selection and Prompt assembly
  discovery and execution routing
  approvals, recovery and reconnection
  naming, folder and field conventions
  release criteria and installation/promotion rules
  temporary versus persistent storage
```

These are project vocabulary and governed meanings, not additional Object roots.
For example, compilation rules belong in Method/Operations Atom Substance; an
actual compiler invocation is an Execution, and its saved output is a Projection.
This list is a candidate vocabulary grouping, not proof that every Term already
has an admitted definition in current Core.

## 4. Selections

### 4.1 General Selections

```text
Objects selected by identity
  one original Atom by ID
  one historical Atom state by ID + Version Number
  one dependent Object through its bearer

Objects selected by conditions
  Active Atoms
  Atoms with a Content Role or Type
  Atoms owned by a Scope Unit
  Atoms targeting a Scope Unit
  subtree-owned or subtree-targeting Atoms
  Atoms linked through a declared relation
  applicable Methods, Evaluations or Delivery rules

Terms selected by conditions
  Terms defined in selected sources
  Terms naming selected Object kinds
  registered values in a selected allowed-value domain
```

A Selection chooses existing Entities; it does not create a new Object for the
set. Its expression uses Terms, identifiers and syntax, but is not itself one Term.
Resolved members retain their identities and provenance.

The Selection must make its source/view and filters clear. For Scope Units,
ownership, targeting and applicability are not interchangeable. Current state,
Active originals, historical states and projected copies are different views.
Inputs used for an actual operation must retain the required source/state evidence.

A saved selection definition may be an Atom or another Artifact. A separately
identified, tracked materialization may be a Projection Object. Its definition,
expression, resolved membership and materialized output are not interchangeable.

### 4.2 CAPRMEDIO project Selections

```text
Core and methodology selections
  Active original Core R Atoms
  source Atoms selected for Applicable Methodology compilation
  projected members currently Active or Archived
  source Atoms involved in a reported conflict

Scope and support selections
  applicable M Atoms for one stated Scope Unit boundary
  E Atoms supporting one Requirement
  D rules for one delivery environment
  affected relations after an Atom change

Graph and harness selections
  Subjects from the selected Core source view
  Terms and allowed relations for one graph view
  context needed for one operation or delegated Step
  available Tools or Operations in a selected project context

Release selections
  exact source/input set selected for a release
  package members selected for installation
```

Operations can retrieve, filter, check or compile these selections without
inventing another collection Object. A selected set is not automatically an
accepted input frontier, a completed Run or a Projection.

## 5. Connections between the branches

```text
Term → names a meaning → Object kind or another concept
Selection → uses → Terms, identifiers and conditions
Selection → chooses → existing Objects or Terms
Artifact → contains a governed definition of → Term or Selection
Atom.Semantics → defines meaning for → Terms and values in scope
Execution → processes → selected inputs
Projection → materializes a derived result from → selected sources
```

These arrows explain model roles; they do not register native edges. Ordinary
Object connections still include ownership, GOVERNS/DEPENDS_ON, carrying,
derivation, and historical recording with their separately governed endpoints.

Example:

```text
Method
  → Term naming a role/concept

A particular M Atom
  → Object

All applicable Ms for this Scope Unit
  → Selection

A saved prompt compiled from those Ms
  → Projection Object

Running the prompted work
  → Execution Object
```

## 6. Adoption boundary

- This document broadens the candidate meaning of Entity. It does not claim the
  current Core definition or any Object/Term/Selection profile already matches it.
- Current `subjects.governs` still resolves one canonical Entity under current
  authority. This candidate does not admit an arbitrary Selection as that target.
- Existing `atom(...)` syntax remains non-enumerating and case-sensitive.
- `Atom.ID` and `Scope Unit.ID` are candidate semantic display names only;
  storage/selector keys are unchanged.
- The Active/base and Archived/version-qualified Atom ID formats are candidate
  identity rules only. Existing archive contents, filenames, ID validation,
  lookup and relation references have not been migrated.
- Objects Graph is a proposed display name; tools, paths and APIs retain their
  current names until separately authorized migration.
- Property fields are not a replacement schema; role/Type-required content is
  not silently removed. Registered value domains are not discarded.
- Optional `Atom.Semantics` is a candidate content field. Current Atom schemas,
  authoring rules, definition Atoms, Terms extractors and validators are unchanged.
- Omitted or unreviewed legacy labels are unclassified, not deleted or invalid.
- No new native Object/Term/Selection instances or relations are admitted.
  This document creates no parser changes, Core revisions, Journal events or
  runtime effects.
- If adopted later, correct authoritative Subjects first; content alignment
  follows the separately approved sequence and source-pinned checks.

The prior source-pinned 706-identity review remains separate evidence. Candidate
#3 records the latest conceptual direction; it is not a claim of fresh exhaustive
review, live execution, implementation completeness or native admission.
