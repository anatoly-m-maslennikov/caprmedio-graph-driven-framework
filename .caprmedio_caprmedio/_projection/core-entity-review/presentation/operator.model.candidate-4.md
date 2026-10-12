# Candidate #4 — Occurrent, Continuant, Carrier

Status: Candidate; not adopted Core authority.

Saved: 2026-10-12, Asia/Tbilisi.

Basis update: the Operator agreed exactly three roots: Occurrent, Continuant
and Carrier. Continuant contains Object, Actor, History, Projection and Selection;
it explicitly excludes Carrier. Earlier identity, content, Terms and source-authority
decisions are retained below.

Basis: the Operator's latest decisions in this conversation. This full candidate
supersedes the prospective taxonomy in [Candidate #3](operator.model.candidate-3.md).
Candidate #3, the [older saved candidate](operator.entity-graph.candidate.json),
the captured 706-identity review, source pins and receipts remain unchanged.
A new FPF review with different questions is planned, not executed. Its Plan must
be shown and approved first; no fresh analytical PASS or adoption is claimed.

This is a full conceptual model, not a completed remapping of every old Subject.
It does not change authoritative Atoms, Project Structure, parsers, storage keys,
native relation admission or runtime state.

## 1. Base model

Entity — umbrella, not a fourth root

```text
Occurrent
  /Execution
  /Session

Continuant
  /Object
  /Actor
  /History
    /Revision
    /Journal
  /Projection
  /Selection

Carrier
```

- **Occurrent:** actual work happening, such as a run, session or running application.
- **Continuant:** what remains identifiable apart from a live occurrence.
- **Carrier:** what bears a representation, such as a file, folder or database entry.

These are three non-overlapping branches in this CAPRMEDIO candidate.
Continuant explicitly excludes Carrier. This is the agreed local convention,
not a claim that every ontology uses these words in the same way.

Under Continuant:

- **Object:** source-authoritative content about what, how or other project concerns,
  including Atoms and governing configurations.
- **Actor:** who performs work, separate from Object.
- **History:** preserved states and records about what happened.
- **Projection:** derived content, including compiled graphs and documents.
- **Selection:** a rule or expression choosing existing items from sources or views.

“Ephemeral” means an actual occurrence, not a short retention period.
A live run cannot be stored as the run itself; a log or snapshot is a record
about it. Ending a run does not turn that run into History.
A temporary file remains a Carrier; a long-running session remains an Occurrent.
Temporary Selection expressions and Projections do not become Occurrents merely
because they are later discarded. No invariant-based classification is introduced.

Terms describe meanings in source uses, allowed-value domains and derived Terms
Graph entries; they are not another root. A Term can name an Entity kind, an Actor
role or another concept without a new Entity node or authoritative definition layer.
The Term and the thing it names are not interchangeable. Neither are an Actor Type
name and the Actor performing work.

General and CAPRMEDIO-project entries are two views of this same model, not two
sources of truth. General means reusable across projects. Project-specific means
CAPRMEDIO as the product being developed, not framework-wide rules merely used
by this project.

### Notation

- `/`: broader kind to narrower kind.
- `.`: bearer qualification for a dependent entity or component. Actual
  Properties remain dependent Objects.
- `:`: Property to allowed value, not assignment.
- No `@` relation operator. `@<Version Number>` is filename punctuation only;
  it is neither part of an Atom ID nor Subject relation syntax. Delivery
  policies define storage conventions.

Indentation outside a taxonomy is grouping or ownership, not an inferred `/` edge.
The relation meanings shown here are candidate meanings, not newly admitted
native relation names.

## 2. Occurrents, Continuants and Carriers

### 2.1 General model

```text
Occurrent
  /Execution
    .Execution ID
    /Action Run
    /Step Run
    /Workflow Run
  /Session

Continuant
  /Object
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
      .Owning Scope Unit
      .Target Scope Unit
    /Governing Configuration
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
    /Relation
      .Relation Type
      .Source Reference
      .Target Reference
  /Actor
    .Actor Type
      : Operator
      : AI Agent
    .Name
  /History
    /Revision
    /Journal
      .Record
  /Projection
    .Source References
  /Selection

Carrier
  .Carrier ID
  /File Carrier
    .Filename
    .Path
  /Directory Carrier
    .Path
  /Database Carrier
```

An Occurrent happens or unfolds in time. The record describing it is a different
item under History. A Carrier bears the representation of content; it is neither
the content nor the live occurrence. File retention and execution duration do
not decide the branch. Database forms remain governed by D policies; this tree
does not add a storage schema or require a Carrier node for every field.

#### Artifact and dependent Objects

- Artifact describes one governed lifecycle unit. It is used for source and
  derived records, not a taxonomy parent that places History or Projection
  under Object.
- An Atom is the smallest independently governed Artifact.
- Governing Configuration is source-authoritative configuration that is not an
  Atom, including `project_structure.toml`. Project Configuration Atoms remain
  Atoms; a configuration file is not made an Atom merely because it governs.
- Properties are dependent Objects. They need a bearer, not a separate Carrier
  or independent lifecycle. Their bearer may be an Object, Actor, Journal or
  Projection; the bearer does not thereby inherit the Object classification.
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

Keep three distinct scope meanings:

- `Atom.Owning Scope Unit`: where the Atom belongs.
- `Atom.Target Scope Unit`: the unit addressed by a relational Atom.
- `Atom.Substance Scope`: the exact governed boundary.

The first two are Atom-borne references, not new Scope Unit kinds. The old combined
lookup context is a source-specific Selection, not a fourth scope. These semantic
names do not rename storage keys or content.

Atom content has distinct purposes:

- **Substance:** what the Atom states.
- **Substance Scope:** where that content applies.
- **Semantics:** optional explanation of what Terms and values mean in this
  Atom's content and scope.
- **Details:** examples, rationale and supporting explanation; not another
  competing place to define meanings.

Semantics is governed content, not commentary. It shares the Atom's authority,
scope, Status, Version and lifecycle. It supports the same authority unit;
unrelated or independently governed Claims are not hidden in this section.

Semantics explains the source case; it does not make this Atom the sole owner
of a Term's meaning. The Terms Graph compiles meanings from real uses across
the selected source Atoms, including their Semantics where present. No separate
layer of Term-definition Atoms is required by this candidate. See section 3.3
for compilation, reuse and conflict handling. Existing Definition Atoms are
not retired or deleted by this candidate update.

An Atom subtype inherits Atom obligations. It does not need duplicate definitions
of those obligations. Inheriting a Carrier obligation does not mean sharing one
physical Carrier. General D policies can cover multiple Properties and Objects.

Content Role, Type, tiers and internal/external/relational Governance Locus remain
Properties or classifications, not additional Object roots. I remains actual
Implementation; this candidate creates no Implementation Atoms.

#### History and Projection

```text
History
  /Revision
  /Journal
    .Record

Projection
  .Source References
```

- History means preserved information, not the events themselves.
- Revision is a preserved historical state, not the change that produced it.
- Journal contains records about actual happened changes, Executions, decisions
  and outcomes. Executions themselves are never Journal contents.
- A Journal is a History lifecycle unit. Describing it as an Artifact does not
  classify it as an Object or create a copied Journal node.
- Revision is not an Atom, a separately governed Artifact or an Artifact-borne
  Property; no recursive Artifact.Revision or Revision-of-Revision rule is
  introduced.
- A Journal Record is a dependent stored History record about an event. It is
  not the event it describes; the Journal remains History.
- Git preserves Atom contents and versions. Journals register what happened.
- Projection is a separate derived artifact, not an Object subtype or History
  merely because it is saved. It does not become authority for its source facts.

#### Scope Unit, Carrier and Relation

- Scope Unit owns Atoms and child Scope Units; it is outside any individual Atom.
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
| Original Atom, current or archived | stored `Atom.ID`: `(project prefix)-(Content Role first letter)-(number)` |
| Historical Atom state | Atom ID + separate Version Number, e.g. `CA-P-123`, version `3` |
| Scope Unit | `Scope Unit.ID`: `(project prefix)-SU-(number)` |
| Carrier | Carrier ID; not filename/path |
| Execution | Execution ID |
| Dependent Object | bearer identity + dependent name |
| Historical Atom lookup | Atom ID + Version Number, e.g. `CA-P-123`, version `3` |
| Other unversioned Artifact state | Artifact ID + Updated At |

Example dependent identity: `atom(atom_id="CA-R-123").status` within the selected
source or Projection view. `Atom` is the Object kind. Lowercase `atom(...)` remains
distinct case-sensitive selector syntax, not an alias or an enumeration operation.

The semantic display names are `Atom.ID` and `Scope Unit.ID`. This does not rename
storage keys or the `atom_id` selector argument.

```text
Current non-archived Atom
  Atom.ID = CA-P-123
  Version Number = 4
  Status = Done

Archived version 3
  Atom.ID = CA-P-123
  Version Number = 3

Atom filename for version 4
  CA-P-123@4-SCOPE_NAME--summary.md
```

The bare ID is the stable lineage ID and remains the stored `Atom.ID`. Historical
references carry that ID and the separate Version Number. `@<Version Number>`
appears only in Atom filenames. All Atom filenames use the required form
`AtomID@Version-SCOPE_NAME--summary.md`; `SCOPE_NAME` is the Scope Unit Name,
not its Label or full path.

An ordinary identity-preserving update creates the next Version Number and
archives the older version without incrementing it again. The new non-archived
version preserves its intended Status (for example, Done or Backlog); it is not
forced to Active. A Type change creates a new Atom with a new ID and archives
its predecessor, rather than making a same-ID version change. Type is not the
only replacement trigger; the current Summary identity rule remains in force.

Across non-archived original authoritative Atom folders together, at most one
original carries a bare ID. Archived originals may share that bare ID at different
Version Numbers. Default lookup still covers Active originals; that is a
view/filter, not the definition of currentness. Current means non-archived.
Historical lookup uses Atom ID plus Version Number. Existing non-archived status
containers remain inside the current-original uniqueness boundary. Drafts have
no assigned Atom IDs; no Draft semantic deduplication policy is added.

Projected instances still belong to separate views; a source Atom Object and its
derived member do not become the same instance merely because they share a bare
ID. An Applicable Methodology projected Atom member preserves the source Atom
ID, Version Number and authored content; its projection-local Status and
provenance may differ. An
excluded member may be Archived in the Projection without becoming an archived
historical source version.

Scope Unit ID stays stable when Label, Name or path changes. Metadata folder names
retain `(project prefix)-SU-(number)-(LABEL)-(NAME_NAME)`. Project-root delivery
folder names stay as they are. Carrier ID syntax/assignment remains authoring work.

### 2.2 CAPRMEDIO project view

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

#### Project Objects, Projections and History

```text
Source-authoritative Objects
  Governing Configurations (not Atoms)
    Project Settings
    Project Structure (project_structure.toml)
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
  database carriers and other storage forms
```

A component's specification, executable implementation, actual run and derived
output are different things. A source file does not prove a running service,
installed Extension or completed execution. Graph App and Codex Plugin remain
planned product candidates, not automatically accepted Scope Units or live components.

#### Applicable Methodology

```text
Core + installed Extensions + Project Configuration
  → select current, non-archived, eligible source versions
  → project each selected source Atom one-to-one
  → place selected members in Active or Archived according to applicability
  → record applicability and conflict-resolution decisions
```

Each derived member preserves its source Atom ID, Version Number, authored
content and relative source link. The source reference identifies the exact
original source state; projection-local Status and provenance do not alter it.
Applicable Methodology admits neither every Status nor every available source:
its input is only current, non-archived, eligible selected source versions.
The whole Projection has one lifecycle and its own rebuild tracking.

Not every member is Active. Excluding a projected member does not mutate its
original source or turn it into a historical source version. Source corrections
are authored in Project Configuration and then projected through the whole
Projection lifecycle. Conflict resolution can create a new authored original
Atom there; that original can then be projected one-to-one. Multiple originals
are not merged into one projected Atom.

The Journal records Atom IDs and Version Numbers projected to Active, projected
to Archived, or created in Project Configuration. Git preserves their contents
and versions. An applicability exclusion and an archived historical version are
different.

The production Scope Unit and the delivered Applicable Methodology Projection
are separate Entities: a Scope Unit Object and a Projection. The Projection
does not replace Core, Extension or Configuration source authority. This later
design direction is not claimed to be already adopted by the active-only
compilation wording in current Core.

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
Journal entries describe actual happened performances; they are not the live
Executions shown here.

### 2.3 Actors

```text
Actor
  .Actor Type
    : Operator
    : AI Agent
  .Name
```

Actor identifies who performs work. It is a Continuant branch alongside Object,
History, Projection and Selection, not an Object subtype.
The work performed can be an Occurrent Execution; its performer remains an Actor.

Actor Type and Name remain dependent Objects borne by the Actor. Their dot
qualification does not place the Actor under Object or introduce another
Property class. Operator and AI Agent remain Actor Type allowed values, not
new Object kinds or additional Actor subtypes.

Name is optional. The existing identity convention remains Actor Type +
optional Name; individual unnamed distinctions remain deferred. An unnamed
Actor Type names a generic role, not a uniquely distinguished performer.
No new Actor identity field, selector syntax, runtime type or user type is added.

## 3. Source meanings and Terms Graph

### 3.1 General Terms

Terms are names with meanings in context. They name Entity kinds, Actor roles
and concepts without additional Entity nodes. Source meanings and registered
allowed values remain; derived entries belong to the Terms Graph Projection,
not a separate authoritative definitions layer or independent Term root.
The review category Term can still describe a source meaning or derived
vocabulary entry; it does not introduce a root branch. A source label alone
does not create a materialized Projection entry.
These groups organize vocabulary; they are not new native Term hierarchies.

```text
Entity and kind names
  Object, Continuant, Occurrent
  Artifact, Atom, Governing Configuration
  History, Revision, Journal
  Projection, Selection
  Scope Unit, Carrier, Relation
  Execution, Session

Actor vocabulary
  Actor, Actor Type
  Operator, AI Agent (Actor Type allowed values)

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
Method Object root. A source Atom's content and optional Semantics provide
evidence of how a Term is used. The Terms Graph derives definitions from those
cases without making the Term and any source Atom the same instance.

Registered allowed-value domains and admitted nodes remain preserved. A raw
scalar is not automatically a new Term, Object or Actor. `:` retains its
allowed-value meaning; it is not assignment syntax.

A label or alias does not create another Object or Actor. Syntax characters,
selector keywords/keys and identifier literals are not automatically Terms either.
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

### 3.3 Terms Graph — definitions from real cases

Source Atoms and their Semantics →
compile how Terms are used →
derive definitions in the Terms Graph Projection →
reuse the Projection when creating Atoms or other Projections →
compare source cases to find conflicts, gaps and incoherence.

The source Atoms remain authoritative. A compiled definition is part of the
Projection; it is not a new source of truth or a separate definition layer.
Terms can develop as their source cases develop. Their meanings are not fixed
by assigning each Term to one definition-owning Atom.

Each derived meaning retains the contributing Atom IDs and Version Numbers,
source passages and applicability scopes. The Projection states which sources
it covers. Missing evidence or unclear scope remains visible; compilation must
not invent a settled meaning or hide disagreements behind one definition.

Preserve different meanings in different scopes. Flag a conflict when those
meanings are incompatible for the same applicable case. Different scopes alone
do not make a conflict; uncertain overlap is an unresolved question.

For example, `*.Status` selects actual Status properties and their source uses
so the Projection can compile their shared meaning. A shared meaning does not
require identical allowed-value sets for every bearer or Atom Type. Different
allowed sets alone are not a meaning conflict. `Atom.Status` is a property;
the selection does not create missing properties such as `Scope Unit.Status`.

The Projection can inform a new Atom or another Projection. Reuse preserves
the distinction between source statements and derived interpretation; it does
not give the reused definition independent authority. Correct source content
when resolving a source conflict, then rebuild the affected Projections.

Adopting this rule requires replacing the current definition-only assumptions,
including CA-R-126 and CA-R-1319 (one Definition Atom per Governed Term),
CA-M-114 and CA-R-1454 (definition-only derivation), and the relevant authoring,
Terms Graph Operations and Evaluation rules. Preserve source traceability and
native Relation admission during that change. This candidate update does not
retire source Atoms or implement extraction, compilation or conflict checking.

## 4. Selections

### 4.1 General Selections

```text
Objects selected by identity
  one original Atom by ID
  one dependent Object through its bearer

History selected by identity or recorded references
  one historical Atom Revision by Atom ID + Version Number
  Journal records about actual happened Executions

Projections selected by identity or conditions
  a derived graph or document
  projected members in a stated source view

Objects selected by conditions
  Active Atoms (a Status view)
  Atoms with a Content Role or Type
  Atoms owned by a Scope Unit
  Atoms targeting a Scope Unit
  subtree-owned or subtree-targeting Atoms
  Atoms linked through a declared relation
  applicable Methods, Evaluations or Delivery rules

Actors selected by existing identity or conditions
  Actors with Actor Type Operator or AI Agent
  named Actors matched by Actor Type and Name

Source vocabulary and Terms Graph entries selected by conditions
  Terms used in selected sources
  Terms naming selected Entity kinds or Actor roles
  registered values in a selected allowed-value domain
```

A Selection is a Continuant rule or expression choosing existing items; it does
not create another Object for the selected set. Its expression uses Terms,
identifiers and syntax, but is not itself one Term or an authoritative definition.
Executing a selection/query is an Occurrent. A separately saved or tracked result
is a Projection, not the Selection or the live query.
Resolved members retain their identities and provenance.
Actor selection examples are conceptual; no new Actor selector grammar or
storage fields are introduced.

The Selection must make its source/view and filters clear. For Scope Units,
ownership, targeting and applicability are not interchangeable. Current
(non-archived) state, Active originals, historical states and projected copies
are different views.
Inputs used for an actual operation must retain the required source/state evidence.

A Selection may be defined inside an Atom or another Artifact. The containing
Artifact, Selection expression, query execution, resolved membership and saved
or tracked Projection output are not interchangeable.

### 4.2 CAPRMEDIO project Selections

```text
Core and methodology selections
  Active original Core R Atoms (default Status view)
  current non-archived eligible selected source versions for Applicable
  Methodology compilation
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
Source Term use → names a meaning → Entity kind, Actor role or another concept
Selection → uses → Terms, identifiers and conditions
Selection → chooses → existing items from sources or views
Actor → performs → work that is an Occurrent Execution
Source Artifact → contains source usage of → Terms, or a definition of a Selection
Atom.Semantics → explains source-case meaning for → Terms and values in scope
Terms Graph Projection → compiles meanings from → source cases
Execution → processes → selected inputs
History Revision → preserves → a historical state
History Journal → contains records about → actual happened Executions and outcomes
Projection → materializes a derived result from → selected sources
```

These arrows explain model roles; they do not register native edges. Ordinary
connections still include ownership, GOVERNS/DEPENDS_ON, carrying,
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
  → Projection

Running the prompted work
  → live Occurrent Execution

A Journal entry about that actual happened work
  → historical record, not the Execution

Who performs that work
  → Continuant Actor

A file bearing the Atom or compiled prompt
  → Carrier, not the content or its execution
```

## 6. Adoption boundary

- This document proposes exactly three roots: Occurrent, Continuant and Carrier.
  Entity is only their umbrella. It does not claim current Core or profiles already
  match this model.
- Continuant explicitly excludes Carrier. Object, Actor, History, Projection and
  Selection are siblings under Continuant, not merely display groups. Dependent
  Properties remain Objects; current Core classifications, profiles and runtime
  types are unchanged. No invariant-based classification is adopted.
- Non-Atom Governing Configuration remains source-authoritative. This does not
  convert configuration files into Atoms or change their schemas or contents.
- Live Executions and Sessions are Occurrents, not Objects. Journal records about
  actual happened Executions belong to Continuant/History; they do not contain or
  become the Executions themselves. Short retention does not make a Carrier,
  Selection or Projection an Occurrent.
- Terms retain source meanings, allowed-value domains and derived Terms Graph
  entries without an independent Term root or authoritative definition layer.
- Current `subjects.governs` still resolves one canonical Entity under current
  authority. This candidate does not admit an arbitrary Selection as that target.
- Existing `atom(...)` syntax remains non-enumerating and case-sensitive.
- `Atom.ID` and `Scope Unit.ID` are candidate semantic display names only;
  storage/selector keys are unchanged.
- Bare Atom IDs, separate Version Numbers and Atom-filename `@Version`
  punctuation are candidate rules only. Existing archive contents, filenames,
  ID validation, lookup and relation references have not been migrated.
- Objects Graph is a proposed display name; tools, paths and APIs retain their
  current names until separately authorized migration.
- Property fields are not a replacement schema; role/Type-required content is
  not silently removed. Registered value domains are not discarded.
- Optional `Atom.Semantics` is a candidate content field. Current Atom schemas,
  authoring rules, definition Atoms, Terms extractors and validators are unchanged.
- Omitted or unreviewed legacy labels are unclassified, not deleted or invalid.
- No new native Entity or vocabulary instances or relations are admitted.
  This document creates no parser changes, Core revisions, Journal events or
  runtime effects.
- If adopted later, correct authoritative Subjects first; content alignment
  follows the separately approved sequence and source-pinned checks.

The prior source-pinned 706-identity review remains separate evidence. Candidate
#4 records the latest conceptual direction; it is not a claim of fresh exhaustive
review, live execution, implementation completeness or native admission.
Reports pinned to earlier candidate revisions remain historical evidence,
not current acceptance. Re-review affected targets against this revision; do
not silently replace their candidate pins or inherit their semantic acceptance.
