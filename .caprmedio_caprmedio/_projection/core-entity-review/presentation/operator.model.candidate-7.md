# Candidate #7 — Subject model

Status: approved for full application; the initial source increment and the bounded R/M, Subject and Eng-Type definition alignment are applied and checked. Full migration is not complete.
Updated: 2026-10-24. Tool Scope declarations, bounded contract-owner moves, integer Tier increments and the Project Goal exception are applied and independently checked. Remaining Subject, Type and relation exceptions are recorded in the completion-progress document; full migration is still incomplete.

Application scope: the Operator approved Subjects, their defining rules, global property rules and Atom IDs together. UX and Design remain pending. This approval is not a migration receipt; record actual source and runtime effects separately.

Latest execution boundary: migrate Current R/M/E/D/O Atoms and Governing Configurations. C/A/P, existing Draft Atoms and existing Archived Atoms are outside this pass. The model may still define their formats and meanings; those definitions do not authorize edits to their instances. The Operator explicitly included Governing Configuration data, including Project Structure; preserve unrelated configuration values. Do not treat excluded instances as completion blockers.
The Operator confirmed that updating a Current RMEDO Atom still creates its usual new predecessor archive. This does not authorize changes to any existing Archive or Draft.

This candidate records the latest Operator decisions. It follows [Candidate #6](operator.model.candidate-6.plan.md). It replaces the single Entity-root proposal and the later separate Entity/Method Subject roots. Earlier decisions remain where this candidate does not change them. Earlier migration records remain history, not evidence that Candidate #7 is applied.

## One root: Subject

An Atom has content about something →
that something is its Subject →
the current topic branches are Domain and Engineering →
Graph supplies the global Relation and Rule subjects.

```text
Subject
	Domain
	Engineering
	Graph
		Relation
		Rule
```

This is the current reading outline. Canonical Subjects use full paths from `Subject`, as defined below. The outline alone is not a complete source-by-source migration map. UX and Design are pending and are not part of the current migration. Documentation has not been adopted as another current branch. The previously agreed Graph branch remains global; it is not a third product-topic branch.

These branches are expandable. Domain and Engineering are not an exhaustive two-way split. Do not make an Engineering topic into an independent object merely to give an Atom a Subject.

## What the branches mean

| Branch | About | Examples |
| --- | --- | --- |
| Domain | What the project means and offers | Atoms, Scope Units, public API behavior, user-visible results |
| Engineering | How it is structured, built, stored and operated | Carriers, orchestrator/worker architecture, state ownership, function purity, diagnostics |
| Graph | Connections and constraints across the model | Relation definitions and Graph Rules |

Pending examples: UX would cover journeys and interaction; Design would cover visual/UI design. They do not supply migration targets now.

An API contract and the workers implementing it concern the same feature, but different Subjects. A Carrier remains an Engineering Subject even when a user can inspect it. Visibility alone does not decide the branch.

## Graph is global

Graph/Relation defines connections.
Graph/Rule defines their permissions, requirements and constraints.

Relations can connect elements within any branch and between branches. A Graph Rule can constrain those connections. Neither is confined to Domain or to the Graph branch's own elements. Global scope does not mean every connection is allowed.

Keep Relation descriptions separate from Graph Rules. Keep Relation Types separate from actual links. Store the direct relation; derive its inverse. Adding a task does not require updating its containing Epic just to maintain an inverse list.

### One containment relation

Scope Units and Container Atoms use the same relation:

```text
Scope Unit CONTAINS Scope Unit
Scope Unit CONTAINS Atom
Container Atom CONTAINS Atom
```

Store `IS_CONTAINED_BY` on the contained item; derive `CONTAINS`. Graph Rules define the allowed endpoints and cardinality. Only permitted Atom Roles/Types can act as containing Atoms. This does not add a separate containment relation for each container kind.

## Subject is not Content Role

Subject says what the content concerns.
Content Role says what the content does.
They are independent by definition.

R defines required results: what the application produces and how it behaves at runtime.
M defines how to achieve those results, including coding policies and engineering decisions.
This distinction does not assign branches to content roles.

Any Subject branch can have R, M, E or D:

- R defines required results and runtime behavior, including delivery guarantees, error-rate limits and request-time targets such as P50 or average.
- M defines the means of achieving those results, including architecture, coding policies and engineering decisions. A required architecture remains M; making a choice mandatory does not turn it into a runtime result.
- E defines how to check them.
- D defines their storage or delivery.

R can specify functional requirements about business/domain logic or non-functional requirements about speed, performance and other runtime outcomes. A non-functional R can have an Engineering Subject; R is not restricted to Domain.

For example, exactly-once delivery behavior is R; the architecture and retry rules used to achieve it are M. The check is E; a measured result is evidence, not the required target. Hardware and deployment environment belong in D under the Operator's chosen convention.

Subject still names the topic. Eng Policy and Eng Decision are Types, not new Subject branches. Do not classify from the owning Scope Unit or the words used in a filename.

Operations selects and uses the applicable RMED in a sequence of actions. A compiled M/E guidance document is a derived Projection, not another authoritative Subject root.

## Keep the structural distinctions

Subject branches organize topics. They do not replace object kinds or their relations.

- Node remains the logical abstraction, with Continuant and Occurrent kinds.
- Atom, Governing Configuration, Scope Unit, Project, Actor, History, Projection, Selection and Term retain their existing meanings.
- Actual runs and events are Occurrents. Their records are not the occurrences themselves.
- Journal contains event records. Versioned Atoms preserve prior states; do not restore a separate Revision entity.
- Carrier represents content in files, directories, databases or another admitted form. It is not the represented content.
- Artifact remains a Term, not another branch.

### IDs belong to their bearers

Atom, Governing Configuration, Scope Unit, Projection and Journal each have their own ID. Use the specific property:

```text
Atom.ID
Governing Configuration.ID
Scope Unit.ID
Projection.ID
Journal.ID
```

These are short display names; canonical Subjects retain the full path. `projection.id` is the pseudocode spelling of Projection.ID, not a generic Entity.Identity property. Exact carrier fields and ID formats remain defined by D for the corresponding kind; do not apply the Atom ID format to every ID.

Map old generic identity Subjects to the actual governed bearer or an explicitly applicable cross-bearer Graph Rule. Preserve useful identity constraints without restoring an Entity root or adding an ID property to every Subject. A Projection's own ID is distinct from the IDs of things represented in it.

### Full Subject paths

Use the full path from `Subject`. No separate namespace delimiter or abbreviated-path resolution is needed.

| Notation | Meaning |
| --- | --- |
| `/` | Broader to narrower Subject, including kinds and classifiers |
| `.` | Bearer to dependent property |
| `:` | Property to allowed value, not assignment; also retained in qualified classifiers |
| `//` | Kind to a named instance |

Examples:

```text
Subject/Domain/Node/Continuant/Atom.Status
Subject/Domain/Node/Continuant/Atom.Status: Active
Subject/Domain/Node/Continuant/Atom/Content Role: Plan
Subject/Engineering/Function Purity
Subject/Engineering/Carrier/File Carrier.Format
Subject/Graph/Relation
Subject/Graph/Rule
Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow
```

Full paths may use all four operators. The conditions under which `//` is mandatory are deferred; its availability does not force every named topic into an instance path.

Inheritance remains: broader-kind properties and rules apply to narrower kinds; allowed values may be extended where permitted. A topic's place in the Subject tree does not by itself make the topic an independently represented object.

Metadata fields and Markdown content sections remain Atom properties with different representations inside the carrier. The global property rules below describe their values, not a new carrier schema.

### Keep the later identity decisions

Atom ID is mandatory in every group. This supersedes both the old no-ID Draft rule and the later optional-ID Draft proposal:

| Group | Atom ID example |
| --- | --- |
| Current | `CA-P-123` |
| Draft | `CA-P-123@1-draft` |
| Archived | `CA-P-123@1` |

- A new Draft receives the numbered ID form too; an unnumbered marker such as `CA-R-draft` is no longer the target format.
- Creating a new Draft immediately reserves an unused base Atom number: `CA-R-123@1-draft` reserves `CA-R-123`, and promotion keeps that base. An edit Draft reuses the existing Atom's base number, such as `CA-R-123@4-draft` for its proposed next Version. Do not renumber a Draft on promotion merely to keep numbering dense.
- Draft, Current and Archived are three separate status groups. Current excludes Draft and Archived; it includes Active, Done, Canceled, Backlog and other admitted current Status values. Current source Atom IDs remain unique across that group. Archived versions share the base identity but use distinct version-qualified Atom IDs and filenames.
- When archiving, set Status to Archived, qualify the Atom ID and filename with the archived Version in every occurrence within that carrier, and move it to the correct archive folder. For example, Version 3 of CA-R-123 becomes CA-R-123@3 in both its carried ID and filename. Keep all Version occurrences consistent with that archived Version; archiving does not increment it. Leave Updated At and all other content unchanged. This replaces the exact-old-bytes archive requirement, not the version-qualified Archived ID rule. Keep Versions and history, not a separate Revision entity.
- Changing the Summary creates a new Atom identity; preserve the previous Atom in history.

For this one-time Candidate #7 migration, adding or correcting Type keeps the Atom ID when Summary and Substance stay unchanged. This is an approved migration exception to R1766's ordinary Type-change replacement rule, not a general removal of that rule. Real updates still advance Version and Updated At and preserve history.

### Relation targets

Relations between Atoms use the unsuffixed Current Atom ID by default, such as `CA-P-123`. The target is the Current Atom, not a particular historical Version. This also applies to Current Atoms whose Status is Done, Canceled or Backlog, subject to the relation's other rules.

No relation use case for Draft or Archived Atoms has been identified. Do not add such links, special relation types or resolution machinery for this migration. Exceptional historical or Draft relation targets remain deferred until a concrete need appears; this is not a universal prohibition inferred from the default.

Source/version pins in history or Projection provenance are not thereby Atom-to-Atom relations. Preserve them without converting them into live graph links.

### Tier and Scope Unit ordering for governing relations

Apply this common ordering constraint to the governing directions of R/M/E/D
Atom relations, including evaluation-for, method-for, delivery-for and applicable
hierarchy/dependency relations. It is not limited to child-of.
The source is a Current R/M/E/D Atom; the target may be any Current Atom
permitted by that Relation Type. Do not restrict targets to R/M/E/D merely to
express this ordering rule.

- Same Local Scope Unit: the target Atom's Tier must be strictly lower than the
  source Atom's Tier.
- Different Local Scope Units: the target's Local Scope Unit must be a strict
  ancestor of the source's. Do not compare their Tier numbers.
- A descendant or sibling Scope Unit is not an allowed target under this rule.

Examples:

| Source | Target | Ordering result |
| --- | --- | --- |
| E Tier 2 | R Tier 2, same Scope Unit | Forbidden |
| E Tier 1 | R Tier 2, same Scope Unit | Forbidden |
| E Tier 2 or higher | R Tier 1, same Scope Unit | Allowed |
| E Tier 1 in TOOLS | R Tier 1 in TOOLS/TOOL1 | Forbidden: descendant target |
| E Tier 1 in TOOLS/TOOL1 | R Tier 2 in TOOLS | Allowed: strict ancestor target |

This is an additional Graph Rule, not a replacement for each Relation Type's
allowed source/target kinds, cardinality or other constraints. Passing the
ordering rule does not by itself admit a relation. Resolve its exact registered
Relation Type when preparing the formal rule; do not invent aliases from these
readable examples.

The methodology is the source of truth. These approved conditions do not depend
on what the current code can parse or check. Define their formal representation
in the methodology; implementation support is separate work, not an approval
gate for the rule.

Apply the cycle constraint to the stored governing direction, not to a derived
inverse view. This does not forbid Scope Unit nesting, P containment or ordered
O substeps. A governing path can only move to an ancestor Scope Unit or to a
strictly lower Tier within one Scope Unit, so it cannot return to its starting
Atom. No Global Tier or stored Structural Level is needed for this ordering.

## Global Atom property rules

Minimum cardinality 1 means mandatory. Do not add a separate mandatory flag.

### Draft completeness

Draft Atoms may be incomplete while being prepared. Their Atom ID remains mandatory. Report missing required properties or content without blocking Draft creation merely because those fields are missing. Full validation of the applicable mandatory properties and content is required before promotion to Current; the specialized Type exceptions still apply.

### Exactly one

| Property | Value type |
| --- | --- |
| `content_role` | Allowed Content Role |
| `local_scope_unit` | Scope Unit reference |
| `type` | Allowed Type for the Content Role |
| `atom_id` | Identifier in the group's format above |
| `status` | Allowed Status for the Role/Type |
| `updated_at` | Date-time with timezone |
| `version_number` | Integer, at least 1 |
| `author` | Actor reference |
| `tier` | Integer within the Local Scope Unit's admitted range below |
| `label` | Exactly one effective Label: explicit Label, otherwise the Type name |
| `content.summary` | Non-empty text |
| `content.substance` | Content; subject to the Graph Rule exception below |

### One numeric Tier

An Atom has exactly one numeric Tier. `tier` replaces `local_tier` and
`global_tier`; do not keep a second stored global rank.

Tier is a graph-ordering level, not a semantic category of a Claim. Preserve
existing numbers where they satisfy the governing relations; use higher
numbers where needed to satisfy the same-Scope ordering rule. This does not
resolve cross-Scope conflicts, missing endpoints or cycles.

| Local Scope Unit / case | Admitted Tier |
| --- | --- |
| Project, ordinary Atom | Integer at least 0 |
| Non-Project Scope Unit | Integer at least 1 |
| Project Goal | Special Requirement Type; Operator-owned; target Project; Tier exactly -1 |

Store only the integer in Atom properties, for example `tier: 2`. Numbers need
no names and have no upper bound. The earlier Principle/Core/General/Standard
names do not impose semantic classifications or stored Tier values. Zero is
available only at Project scope.
Project Goal is a distinct Requirement Type identified by its Project target,
not by storage at Project scope. Its current/local owner is the Operator, an
Actor; this is the established exception to ordinary Local Scope Unit
ownership. It carries Tier exactly -1, not an omitted Tier or a separate
Global Tier. Other Goal Atoms target non-Project Scope Units and follow the
ordinary ownership rules. Do not invent an Operator Scope Unit. This decision
supersedes the earlier Project-owned wording.

An admitted Atom Type can be used at any Tier admitted for its Local Scope Unit;
do not infer Type-to-Tier restrictions. Role/Type-specific content and Relation
Type endpoint rules remain independent. The explicit Project Goal case above
still applies.

This candidate defines methodology, not implementation-schema support.
Applied Current-carrier changes are recorded in the completion progress;
implementation consumers remain separate. The four new Tool contracts below
remain Drafts using numeric `tier` until coordinated adoption.

### Label fallback

If an explicit Label is present, use it. Otherwise, use the Type name as the effective Label. Do not invent a separate Label or store a redundant copy of the Type name merely to satisfy this fallback.

This preserves exactly one effective Label while allowing the explicit Label field to be absent. When a filename or other presentation calls for the Label/Type name, use the effective Label: an explicit Label replaces the Type name there; without one, use the Type name. The Atom's actual Type does not change.

For example, Type Plan with Label Epic is displayed as Epic; Type Plan without an explicit Label is displayed as Plan. Existing explicit Labels take precedence over the fallback.

### Eng Policy and Eng Decision Types

For Method and Delivery Atoms:

- Use Type `Eng Policy` only when its Local Scope Unit has at least one actual,
  currently declared child and the rule automatically applies to every child,
  subject only to genuine topic/environment conditions.
- Use Type `Eng Decision` for a Scope-Unit-specific engineering choice that does
  not automatically become a rule for every child.

Both may be reused, and a Policy may select a named technology. Actual-child
eligibility and automatic child applicability distinguish Policy ownership;
being abstract or naming a concrete technology does not decide the Type.
Leaves may inherit ancestor Policies but cannot locally own Policies. A
hypothetical future child does not qualify. Do not create artificial children
solely to retain a Policy label. If an owner loses its last child, review and
relocate or reclassify its locally owned Policies; do not infer an automatic
runtime conversion.

These names replace `Policy` and `Engineering Decision` for Method and Delivery Atoms. Within PROGRAMMATIC and its descendants, M/D Atoms use only `Eng Policy` or `Eng Decision`. Classify legacy and missing M/D Types into those two; do not retain a third Type there. Evaluation's `Policy` and `Eval Case` names are unchanged. These Types describe the content, not its storage location. Do not classify an Atom merely from its owning folder or project-specific origin. Outside that PROGRAMMATIC M/D scope, retain an existing specific Type where it remains appropriate. Review older names such as Implementation Decision against Eng Decision rather than keeping a duplicate name for the same category.

Do not impose a Type-to-Tier restriction from this distinction. Do not extend
these Type assignments to other Content Roles without their own definition.
Type-classification-only changes in this migration retain IDs under the
exception above.

### Evaluation Types

For Evaluation Atoms:

- Use Type `Policy` for a reusable evaluation rule.
- Use Type `Eval Case` for a concrete check and its expected result.

An Eval Case specifies what to check, not how the check is implemented. Its implementation can use unit, functional, E2E or other tests, LLM evaluation prompts, or both. Do not equate an Eval Case with one executable test or one prompt. Use Eval Case instead of the older QA Case name; Test Case is too narrow.

### Zero or one

| Property | Value type |
| --- | --- |
| `target_scope_unit` | Scope Unit reference |
| `relations` | Collection of typed direct links |
| `subjects` | Collection of GOVERNS and DEPENDS_ON links |
| `content.substance_scope` | Content describing exact applicability |
| `content.details` | Supporting content |
| `content.semantics` | Meaning-specific content |

The collection itself occurs at most once; it can hold many links. An Atom has at most one GOVERNS Subject and any number of DEPENDS_ON Subjects. The Subjects collection remains optional. Express these entry cardinalities and the other link endpoint constraints as separate Graph Rules.

### Local and target Scope Units

Use **Local Scope Unit**, not Owning Scope Unit, as the property name. It identifies the Atom's local placement. An ancestor Scope Unit can include descendant Atoms through the hierarchy; do not repeat every ancestor in this property. Target Scope Unit remains a separate reference, not a second local placement.

Scope Unit parent/child inclusion is sufficient hierarchy authority. Do not
author `structural_level` as an additional governing property in Project
Structure. Parent traversal supplies ancestry; no persisted depth or replacement
global Atom rank is required. Project Structure's authored Structural Level
fields were removed in the recorded configuration increment. Old implementation
consumers may still need migration; that work does not restore structural depth
as methodology authority.

### Specialized content

These are global base rules, refined where a Role or Type needs a different structure. An R/Type: Graph Rule Atom uses one operative YAML block instead of `content.substance`; it has no Substance section. Its Summary remains required. Semantics and Details remain optional. Do not add empty Substance just to satisfy the base rule.

The table names logical properties, not their final YAML keys or Markdown headings. Their carrier mapping belongs in D. Inheritance and the specialized exceptions must be explicit when the formal rules are authored.

## Core and project-specific content

Core defines the abstract, reusable model.
Project Configuration defines the project's concrete choices and procedures.

For this project's migration, fill missing Author values with the Operator, Anatoly Maslennikov, as confirmed by him. Preserve existing Author values. This is a project-specific migration decision, not a general Author fallback or provenance-recovery rule.

This distinction is independent of Subject branch. A generic Workflow definition can be Core; a named CAPRMEDIO Workflow belongs in Project Configuration. Applicable Methodology and its project-specific rules remain project-specific. Engineering content is not automatically Core or automatically Project Configuration.

Do not copy the local Scope Unit tree into Subjects. Local placement states where an Atom belongs; Subject states what it concerns. A Subject name alone does not determine which Atoms belong in a guidance Projection.

For this migration, do not introduce a new Domain entity or property without the Operator's approval. A saved mapping proposal, a valid prefix or unchanged source bytes do not prove that a target preserves meaning. Review the governed thing. Do not route an unclear ontology topic to Engineering just because it has no accepted Domain mapping.

## PROGRAMMATIC Tool structure — declared; contract relocation in progress

Use one modular runtime with shared queue and run state, as recorded in Active
CA-M-432. Scope Units are responsibility/module boundaries, not microservices.
The accepted groups below are intended real Scope Units, with Feature Group as
an appropriate Label; they are not merely display folders.

```text
TOOLS
	Adapters
	Single Actions
		Atom
		Scope Unit
		Projection
		Journal
		Project
		Queue
	Schedulers
		Batch Scheduler
		Workflow Scheduler
	Workflows
	Action Engine
```

Single Actions are target-first, then operation. Find selects matches; Fetch
retrieves content; Check does not mutate; changes use the operation appropriate
to the target. A status change is part of Update, not a separate action group.
Journal supports Find, Fetch and Append. Projection supports Find, Fetch,
Create and Update/Rebuild. Queue has inspection, submission, pending-work
cancellation and pause/resume controls; queue controls use a direct path so a
paused queue can still resume. Pausing dispatch does not cancel running work.
Create only meaningful operation groups, not a uniform CRUD matrix.

Governing Configuration belongs to Adapters; operations on Project and Scope
Unit belong to their Single Action groups or to composed Workflows. There is no
Prompt Helper: use programmatic Find and Fetch for the correct prompt. Graph UI
and Graph Server belong under APPS, outside this Tool partition.

Actual Workflows define sequences and conditions in O. Workflow Scheduler
advances ordered Steps/Substeps. A Step containing Substeps calls no actions
itself; only its ordered Substeps do. Each leaf Step/Substep run starts exactly
one Batch Action Run containing at least one Single Action Run. Batch Scheduler
submits the work and collects results. Action Engine executes queued work and
records results. Results flow Engine → Batch Scheduler → Workflow Scheduler
through shared persistent run state. The caller can disconnect and later fetch
status/results by Run ID; queue and run state survive restart. No extra results
broker or service per Scope Unit is required.

MCP remains a thin interface to this runtime. Existing host-only release entry
points stay host-only. Redistribute the old PROJECT_TOOLS responsibilities by
their actual function; do not keep a special catch-all group just because work
is project-specific. Do not remove its declaration or the other legacy Tool
owners before their actual contracts and bindings have moved.

Four numeric-Tier Drafts record this design: CA-M-433@1-draft (Tool partition),
CA-M-434@1-draft (target-first Single Actions), CA-M-435@1-draft (scheduling), and
CA-M-436@1-draft (Action Engine). They are not Current authority or evidence of
implementation. On 2026-10-24, Project Structure gained the fifteen approved
group, target, scheduler and graph-App declarations. All twenty-nine existing
declarations remain during the transition. Contract relocation is separate;
implementation paths and runtime have not moved. Policy ownership follows the
actual declared child structure, not this display outline.

Current R2153 defines logical Property-targeted Find and Replace, including
Markdown sections, with conjunctive Role/Type/Scope/Property conditions. Local
means direct ownership; full means the selected Scope and declared descendants.
Find, Check and Change remain separate. Existing Update receives explicit full
old/new values; there is no new connector schema or per-Atom confirmation layer.
The contract's presence does not claim implementation support.

## What application still needs

Current preparation: [methodology-only application packet](candidate-7.methodology-application.md). Tool implementation, implementation schemas, MCP, tests and runtime are outside this continuation.

Actual result: [applied methodology increment](candidate-7.methodology-increment-2026-10-22.md), including the bounded Engine batch and remaining source-migration work.

Latest bounded result: [methodology alignment increment](candidate-7.methodology-alignment-2026-10-23.md). R/M and Subject definitions are updated; R2119–R2122 replace the four old Eng-Type definitions, R1665 is rebound, and Project Configuration rule R2123 limits PROGRAMMATIC M/D Types. Existing consumers and numeric-Tier data are not fully migrated.

1. Verify the source-definition alignment now being applied: CA-R-2004 and CA-R-2006 use the Subject root; the old separate Method-root definition CA-R-2005 is retired. Remaining definitions and source Subjects still require their own actual migration.
2. Map existing Subjects to the agreed branches. Preserve governed meaning, dependent properties, named instances and source identity; do not use a blanket prefix replacement.
3. Record literal target paths and their structural relations before migration. Keep uncertain placements visible rather than guessing or dropping them.
4. Apply the reviewed changes with the existing workflows, preserving history, then rebuild the views from the changed source Atoms.

The property and identity decisions also need their own rule/carrier alignment before application. In particular, align the archive contracts with the Status, version-qualified ID/filename and folder changes above; do not enforce the obsolete exact-old-bytes requirement.

Creating this candidate did not change sources. The later Operator-authorized methodology-only continuation is applying source changes recorded in the linked application packet. This candidate remains authored planning material, not a source-derived graph or a completion receipt. No code, Settings or runtime change is implied by that continuation.
