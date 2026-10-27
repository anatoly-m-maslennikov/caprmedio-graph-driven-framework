# Candidate #8 — Subject migration

Reviewed Engine Governs promotion and the Core notation update are applied.
Tools, schemas and runtime are unchanged.
Latest Operator decisions override earlier proposals.

## Completed Core cleanup

The six remaining unrooted Subject occurrences in four Current Core RMEDO Atoms
are corrected: Root Term → Term, Definition Atom → Requirement/Type: Definition,
and CAPRMEDIO Graph → Projection. Duplicate dependencies are merged. Content is
unchanged; predecessor versions are archived. All 800 Current Core RMEDO Atoms
now have rooted Subjects, and CA-PROJ-006 is rebuilt from those Current sources.
This checks rooted paths, not all Subject meanings. Terms Graph implementation
remains deferred. See the [thin Core map](candidate-8.core-subjects.md).

## Work order

1. Map `subjects.governs` for Current Engine RMEDO Atoms.
2. Map `subjects.depends_on` afterward.
3. Promote reviewed Governs Drafts and rebuild the full Current RMEDO Subject Graph (completed).

Use one thin file: [Governs mapping](candidate-8.governs.md).
Its columns are Atom ID, old Governs → new Governs, Status. All 811 reviewed Engine proposals are Applied, including 24 retained No Change proposals. The other 216 Engine Atoms were not updated.
Drafted means the file exists; it does not imply Operator confirmation.
Status may be Candidate, Confirmed, Planned, Drafted, Applied, Blocked or No Change when needed. No Change means the retained Draft needs no Governs change relative to Current.
Do not add body copies, hashes or analysis reports to the mapping file.
When a new or updated definition is needed, create its Atom Draft directly.
Previous working reports are retained only in disposable scratch.

## Subject model

```text
Subject
	/Graph Node
		/Domain
			/Continuant
			/Occurrent
		/Engineering
			/Continuant
			/Occurrent
			/Aspect
				/Architecture
					/Component Structure
					/Communication
				/Authoring
					/Code Authoring
						/Python Code
					/Prompt Authoring
				/Verification
					/Static Analysis
					/Dynamic Testing
					/Coverage
					/Test Design
					/Test Data
						/Golden Corpora
				/Data Handling
					/Source Selection
					/Source Retrieval
					/Parsing
					/Serialization
					/Data Validation
					/Output Publication
				/Execution Control
				/Storage
					/Directory Layout
				/Delivery
		/Documentation
			/Traceability
		/Product: CAPRMEDIO Framework
		/UX
	/Graph Relation
	/Graph Rule
```

Domain Occurrents include modeled Action, Step and Workflow Runs. Technical
sessions and app/tool runtimes belong to Engineering. UX covers the MCP interface
and health-page appearance, not their backend. Abstract Engineering topics need
not be represented as independently carried objects.

The Operator approved the seven Aspect families above after the FPF review.
They classify reusable engineering concerns, not a third temporal entity kind.
Architecture covers Component Structure and Communication; Execution Control
covers queues, scheduling, cancellation and recovery. Authoring covers reusable
code and prompt rules. Verification covers Static Analysis, Dynamic Testing,
Coverage, Test Design and Test Data. Do not duplicate Python authoring policies
under tests. Python-specific checks can narrow the relevant Verification topic;
application behavior keeps its actual Domain Subject regardless of language.
Corpus content belongs under Test Data; physical placement belongs under Storage.
Data Validation checks formats, schemas, types and values; defining valid Atoms
belongs under Domain/Atom. Content Roles and Types do not choose these branches.
Choose the primary governed obligation; keep exact applicability in Content Scope
and retain only actual dependencies. The reviewed grouping is now applied to Current Governs. Engine content and Depends On are unchanged; prior Draft preparation refined 512 existing Drafts and created 190 new Drafts.

Subject, Content Role and Local Scope Unit are independent. Use shared governed
aspects rather than repeat Tool/Scope Unit identities. Existing Domain Subjects
stay where the content really governs them. Do not invent new Domain entities.
Keep precise applicability in Content Scope. Do not revive Revision,
Atom.Property, generic Atom.Substance or Global Tier.

## Tool boundary

- Adapters/connectors: technical carrier create/write/update/move/rename.
- Single Actions: Select and domain Create/Update/Archive.
- Batch Tools: compositions of Single Actions, including Find & Replace.

Any Select can return many results with the requested fields. One Atom Update
includes its property and content changes through this flow:

```text
Copy Current to the next-version Draft → edit Draft → archive Current → promote Draft
```

Keep the ID unless Summary changes; a changed Summary gets a new ID in Draft.
Existing Content Role identity rules remain. Editable aspects include Type,
Local/Target Scope Unit, Status, Subjects, Relations, Tier, Label and content.
Schemas are governing configuration, not Atoms. Atom operations apply them,
not implicitly modify them. A batch Atom-count limit is possible; its value
is not decided here. Getting fresh Actor context through MCP is a separate Step.

## Subject notation

- `/`: broader → narrower kind.
- `.`: bearer → dependent property.
- `:`: allowed value.
- `//`: named instance.
- `>`: whole → part, reusing containment.

```text
…/Workflow//Subject Migration > Step//Update Atoms > Step//Create Draft
```

The example uses compact display labels. Source proposals use full canonical
selectors on both sides of `>`. The terminal Part is the one governed target.
Store Part IS_CONTAINED_BY Whole; derive Whole CONTAINS Part. This is not Step
order, subtype or property qualification. Use actual defining names and evidenced
membership; calling a reusable Tool does not make its definition a contained Step.

## Applied promotion

812 reviewed Drafts promoted: 811 Engine Governs proposals and Core CA-R-1931@10.
812 predecessors archived with their previous Versions. The 78 older or unrelated
Drafts are unchanged. All Engine bodies and Depends On are unchanged.
CA-R-1931 adds only the approved `>` notation paragraph.

R1194 already admits qualified canonical paths; D269 already carries one scalar
Governs path. No extra Drafts were needed for those two rules.

## Rebuilt graph

[Full Current RMEDO Subject Graph](../../CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md) includes 2238 Current source Atoms.
The Core, Project Methodology and Engine partition views are also rebuilt.
Sources and their Versions come from the post-promotion files. Older Depends On
Subjects remain visible; 69 noncanonical occurrences are reported explicitly rather than silently remapped.

## Not applied

Depends On migration, further content rewriting, parser implementation, runtime
updates and release remain outside this pass. The Terms Graph is not implemented.
Only the 812 exact reviewed Drafts were consumed; unrelated Drafts and existing
archives were not changed.

## Three-section projection follow-up

Applied the Operator's display correction. Primary Subjects exclude instances and
properties. The second section shows each primary with direct or inherited
properties, in primary-tree order, with inherited origins marked. The third shows
named instances, Relation Type declarations and concrete Graph Rule declarations;
it does not substitute actual Atom-to-Atom Relation tuples.

Documentation Subjects describe reusable topics, not README modules or named
review reports. Nine Current sources were corrected: broad release-documentation
references use Documentation, and review-evidence references use Traceability.
This follow-up changes four Governs fields and five Documentation-specific Depends On references; the general Depends On migration remains deferred.
The proposed Information Structure, Clarity, Terminology, Navigation and Examples
topics have no selected source evidence yet, so the graph does not invent them.
Core R2150, M232 and D653 carry the new projection contract. Predecessors are
archived; unrelated Drafts, tool code and runtime remain unchanged.
