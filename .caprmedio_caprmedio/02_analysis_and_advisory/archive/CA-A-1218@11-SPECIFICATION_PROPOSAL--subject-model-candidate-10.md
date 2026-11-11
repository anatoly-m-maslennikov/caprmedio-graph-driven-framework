---
atom_id: CA-A-1218@11
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 11
updated_at: 2026-10-27 20:03:46 +0400
relations: {}
tier: 3
---
# Summary

Subject model Candidate #10

## Question

What is the proposed main Subject structure, and which R Atom defines each primary entity or topic?

## Content Scope

Main structure and definitions only. No instances, property lists, instance names, actual Relation Type or Graph Rule instances, source migration or implementation. Namespace and topic headings are explicitly distinguished from independently modeled things.

## Proposal

This Specification Proposal records the accepted design and decisions. Its reviewed definitions and Subject mappings are now adopted in Current RMED. Those source Atoms remain authoritative; this Analysis is not their replacement or the rebuilt Projection.

```text
Subject  [CA-R-1275]
	/CAPRMEDIO  [CA-R-2206]
		/Graph  [CA-R-2208]
			/Node  [CA-R-1994]
				/Project Model  [CA-R-2209]
					/Actor  [CA-R-2218]
					/Atom  [CA-R-655]
					/Continuant  [CA-R-1967]
					/Event  [CA-R-1968]
					/Execution  [CA-R-1970]
					/Governing Configuration  [CA-R-1962]
					/History  [CA-R-1961]
						/Journal  [CA-R-1745]
						/Release  [CA-R-2171]
					/Implementation  [CA-R-2173]
						/Code  [CA-R-2174]
						/Documentation  [CA-R-2180]
						/Prompts  [CA-R-2179]
						/Resources  [CA-R-2189]
					/Occurrent  [CA-R-1972]
					/Project  [CA-R-2220]
					/Projection  [CA-R-1746]
					/Runtime  [CA-R-2194]
					/Scope Unit  [CA-R-1757]
					/Selection  [CA-R-1966]
					/Term  [CA-R-1318]
				/Aspect  [CA-R-2210]
					/Design  [CA-R-2216]
					/Documentation  [CA-R-2217]
					/Domain  [CA-R-2213]
					/Engineering  [CA-R-2214]
					/Product  [CA-R-2211]
					/Project  [CA-R-2212]
					/UX  [CA-R-2215]
			/Relation  [CA-R-1963]
			/Rule  [CA-R-1995]
		/Carrier  [CA-R-1958]
	/<Project Name>  [namespace pattern; CA-R-2207 governs Subject]
```

`<Project Name>` describes a namespace pattern; it is not an instantiated project Subject. CAPRMEDIO is the shared framework vocabulary namespace. Projects use that vocabulary and add their own Subjects without copying it. Namespace, Graph and Project Model headings organize the vocabulary; they do not assert that every child is a subtype of a new real-world entity.

Event and Execution retain existing meanings rather than disappearing during regrouping. History/Journal/Release describe preserved material, while Event, Execution and Runtime describe actual occurrences or contexts. Implementation is directly edited and is not a Projection.

## Defining R Atoms

The table records adopted Current definitions. The linked R Atoms supply authority. Namespace patterns are conventions, not additional Subject instances.

| Main Subject | Defining R Atom | Definition | State |
|---|---|---|---|
| Subject | [CA-R-1275@26](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL--define-subject.md) | a Subject names the thing or topic an Atom governs or depends on. | Current |
| Subject/CAPRMEDIO | [CA-R-2206@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2206-CORE_META_MODEL-DEFINITION--define-caprmedio-subject-namespace.md) | The CAPRMEDIO Subject namespace qualifies the shared vocabulary supplied by the CAPRMEDIO framework. It separates that vocabulary from a project’s own subjects. | Current |
| Subject/CAPRMEDIO/Graph | [CA-R-2208@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2208-CORE_META_MODEL-DEFINITION--define-graph.md) | Graph is the Subject grouping for Node, Relation and Rule: the things or topics represented, their typed connections and the constraints on Nodes, Relations and their properties. | Current |
| Subject/CAPRMEDIO/Graph/Node | [CA-R-1994@11](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md) | A Node identifies a thing or topic addressed by the graph. Its description and Carrier are separate. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model | [CA-R-2209@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2209-CORE_META_MODEL-DEFINITION--define-project-model.md) | Project Model groups Subjects for what exists in a project: its Atoms, governing configurations, Scope Units, Actors, history, Projections, Selections, Implementation and actual execution contexts. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Actor | [CA-R-2218@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2218-CORE_META_MODEL-DEFINITION--define-actor.md) | An Actor is a participant that performs work, provides input or exercises authority in the project. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Atom | [CA-R-655@34](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL--define-atom-artifact-form.md) | an Atom **means** the smallest independently governed Artifact. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Continuant | [CA-R-1967@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1967-CORE_META_MODEL--define-entity-continuant.md) | a Continuant **means** an Entity that persists as an identifiable thing, rather than an actual occurrence unfolding in time. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Occurrent | [CA-R-1972@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1972-CORE_META_MODEL--define-entity-occurrent.md) | an Occurrent **means** an actual occurrence, such as an Event, Execution or Session. a stored record describes the occurrence; it is **not** the occurrence itself. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Event | [CA-R-1968@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1968-CORE_META_MODEL-DEFINITION--define-entity-occurrent-event.md) | an Event **means** an actual occurrence. a record describing the Event is **not** the Event itself. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Execution | [CA-R-1970@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1970-CORE_META_MODEL-DEFINITION--define-entity-occurrent-execution.md) | an Execution **means** the actual performance of work. it is distinct from its reusable definition **and** from records describing what happened. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration | [CA-R-1962@9](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1962-CORE_META_MODEL--define-entity-continuant-object-governing-configuration.md) | Governing Configuration **means** authoritative non-Atom content that supplies declared structural facts or selected configuration values for a Project. it is **not** a derived Projection. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/History | [CA-R-1961@10](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1961-CORE_META_MODEL--define-entity-continuant-history.md) | History **means** preserved earlier state or records of what happened. Preserved earlier versions and Journals belong to History; the events or executions they record do **not**. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal | [CA-R-1745@31](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1745-CORE_META_MODEL--define-journal-artifact-form.md) | a Journal, also called an Event Log, **means** an authoritative Artifact whose recorded history forms **`=1`** logically ordered table of admitted records about events. technical **and** business runtime logs **are** Journals. a record describes an event **and** its recorded evidence; the record is **not** the event itself **or** automatic proof of its asserted outcome. accepted records **must not** be edited, reordered, **or** removed; corrections append new traceable records **without** rewriting accepted history. Journal authority concerns recorded history **and** does **not** independently redefine governing Atom Claims. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release | [CA-R-2171@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2171-CORE_META_MODEL-DEFINITION--define-release.md) | A Release **means** a historical delivery unit of Implementation. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation | [CA-R-2173@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2173-CORE_META_MODEL-DEFINITION--define-implementation.md) | Implementation **means** the actual Code, Prompts, Documentation and Resources that realize RMED for a Project. Directly edited Implementation can be authoritative for what is actually implemented. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code | [CA-R-2174@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2174-CORE_META_MODEL-DEFINITION--define-code.md) | Code **means** program instructions and definitions that realize behavior. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Documentation | [CA-R-2180@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2180-CORE_META_MODEL-DEFINITION--define-documentation.md) | Documentation **means** Implementation content used for explanation, instruction or reference. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Prompts | [CA-R-2179@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2179-CORE_META_MODEL-DEFINITION--define-prompts.md) | Prompts **mean** Implementation instructions or requests addressed to an Actor. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Resources | [CA-R-2189@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2189-CORE_META_MODEL-DEFINITION--define-resources.md) | Resources **mean** Implementation data, apart from Code, Prompts and Documentation, used to construct, configure, evaluate or render a result. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Project | [CA-R-2220@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2220-CORE_META_MODEL-DEFINITION--define-project.md) | Project means the whole project as one entity, distinct from any particular part such as an Atom or Implementation. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Projection | [CA-R-1746@36](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1746-CORE_META_MODEL--define-projection-artifact-form.md) | A Projection is a non-authoritative output produced from a declared selection of sources through a Workflow: | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime | [CA-R-2194@2](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2194-CORE_META_MODEL-DEFINITION--define-runtime.md) | Runtime **means** an actual technical execution context for Implementation. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit | [CA-R-1757@28](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1757-CORE_META_MODEL--define-scope-unit.md) | a Scope Unit **means** a Continuant Node that provides an ownership boundary for Atoms **and** **may** contain child Scope Units. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Selection | [CA-R-1966@9](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1966-CORE_META_MODEL--define-entity-continuant-selection.md) | a Selection **means** criteria for choosing members. a named Selection gives those criteria a name; it does **not** create another Object or independent copies of the selected members. | Current |
| Subject/CAPRMEDIO/Graph/Node/Project Model/Term | [CA-R-1318@23](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1318-CORE_META_MODEL-DEFINITION--define-term.md) | a Term **means** a word **or** phrase with a Project-specific meaning that remains consistent across **all** its uses **in** the same applicable context. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect | [CA-R-2210@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2210-CORE_META_MODEL-DEFINITION--define-aspect.md) | An Aspect is a topic through which an Atom addresses a thing, rather than another copy of that thing. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Design | [CA-R-2216@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2216-CORE_META_MODEL-DEFINITION--define-design-aspect.md) | The Design Aspect addresses the form, presentation and arrangement of an interface or other delivered material. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation | [CA-R-2217@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2217-CORE_META_MODEL-DEFINITION--define-documentation-aspect.md) | The Documentation Aspect addresses how explanatory, instructional and reference material is organized and written. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Domain | [CA-R-2213@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2213-CORE_META_MODEL-DEFINITION--define-domain-aspect.md) | The Domain Aspect addresses the meanings and behavior specific to the project’s problem domain. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering | [CA-R-2214@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2214-CORE_META_MODEL-DEFINITION--define-engineering-aspect.md) | The Engineering Aspect addresses technical architecture, authoring, verification, delivery, storage, data handling, execution control, traceability and observability. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Product | [CA-R-2211@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2211-CORE_META_MODEL-DEFINITION--define-product-aspect.md) | The Product Aspect addresses what a project produces or offers and the outcomes or capabilities expected from it. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/Project | [CA-R-2212@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2212-CORE_META_MODEL-DEFINITION--define-project-aspect.md) | The Project Aspect addresses how project work is organized and governed. | Current |
| Subject/CAPRMEDIO/Graph/Node/Aspect/UX | [CA-R-2215@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2215-CORE_META_MODEL-DEFINITION--define-ux-aspect.md) | The UX Aspect addresses how an Actor discovers, understands and uses an interface and receives its results. | Current |
| Subject/CAPRMEDIO/Graph/Relation | [CA-R-1963@10](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1963-CORE_META_MODEL--define-entity-continuant-object-relation.md) | a Relation **means** a typed connection between identified endpoints. its shared Relation Type and defining authority determine the connection's meaning and declared direction; any applicable Graph Rules supply endpoint, graph-context, **and** cardinality constraints. | Current |
| Subject/CAPRMEDIO/Graph/Rule | [CA-R-1995@11](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1995-CORE_META_MODEL--define-entity-graph-rule.md) | a Graph Rule **means** a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality. | Current |
| Subject/CAPRMEDIO/Carrier | [CA-R-1958@9](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1958-CORE_META_MODEL--define-entity-carrier.md) | A Carrier **means** a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, **not** the Occurrent itself. | Current |
| Project namespace convention (not an instance) | [CA-R-2207@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2207-CORE_META_MODEL-DEFINITION--define-project-subject-namespace.md) | A Project Subject namespace qualifies the project-specific things and topics named under Subject/<Project Name>. | Current |

## Definition boundaries

- Project Model names project things, including Implementation. Aspects name topics addressing those things. CAPRMEDO Atoms and I Implementation are different structures inside the model; not every Project Model item is an Atom.
- Content Role is a classification axis and remains a valid Subject; it is not another primary entity between Atom and role-qualified Atom kinds. The R1531 Draft defines this distinction. No role values or instances are expanded in this main tree.
- A Carrier is distinct from what it represents. A graph can represent a Carrier as a node without merging representation with represented content.
- Documentation under Implementation is actual content; Documentation under Aspect is the topic governing its organization and authoring.
- Subject, Content Role and owning Scope Unit stay independent. A shared Subject does not become project-specific because its governing Atom lives in Project Configuration.
- This proposal does not reintroduce Revision, property entities, generic Graph Node.Type, or Terms-Graph work. Existing Continuant/Occurrent definitions remain available, but their temporal classifications are not mandatory path layers in this proposed main outline.

## Review boundaries and open points

The proposed graph and namespace groupings are organizational levels, not automatically NARROWER_THAN edges. The completed bounded review found no concern from the outline alone; it did not establish complete grammar admission. The project-name placeholder does not choose name normalization or collision/rename handling. These are unresolved proposal details, not new runtime requirements. Existing Entity terminology is preserved rather than silently retired. Existing Term paths are relocated under Project Model/Term; Terms Graph work stays deferred.

## Work and decisions

[Subject refinement stage 3 Epic](../03_plan/CA-P-2673-EPIC--subject-refinement-stage-3.md) holds the Tasks, thin Draft table and links to decision proposals. Candidate #9 remains historical context; Candidate #10 proposes its replacement structure and is not yet applied. The new Analysis Type is defined by [CA-R-2219@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2219@1-draft-CORE_META_MODEL-DEFINITION--define-specification-proposal-analysis-type.md).

## Adoption state

The original 42-definition/anchor preparation and FPF review are complete. All accepted findings have separate Specification Proposals. Governs mapping, Depends On mapping and independent concrete-batch reviews passed before adoption. The applied batch updated 2,252 existing sources, preserved their predecessors, and added 15 new Current definitions. The rebuilt main view uses 2,273 actual Current RMEDO sources and 38 defining R references; it contains no old Subject roots. Terms Graph work, property and instance inventories, general content migration, code and runtime work remain outside this completed pass.

## Decision proposals

- [A1219 — Clarify mixed Subject targets](CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md): Operator-accepted resolution of C10-I01; reflected in the R1994 and R2209 Drafts.

- [A1220 — Define Project as a whole entity](CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md): Operator resolution of C10-I02; reflected in R2220@1-draft.

Each accepted review decision has its own Specification Proposal file. Work and progress remain in P Atoms, with links to those proposals.

## Retained classification Subjects

[A1221 — Retain Continuant and Occurrent Subjects](CA-A-1221-SPECIFICATION_PROPOSAL--retain-continuant-and-occurrent-subjects.md) records the Operator decision. Their existing meanings remain; neither is a compulsory path layer. The project-name placeholder describes a namespace convention governed at Subject by R2207; it is not an instantiated entity or a literal governing target.

## Additional migration decisions

- [CA-A-1222](CA-A-1222-SPECIFICATION_PROPOSAL--update-formal-subject-references.md).
- [CA-A-1223](CA-A-1223-SPECIFICATION_PROPOSAL--govern-nodes-with-generic-type-rules.md).

## Existing Term paths

[A1224](CA-A-1224-SPECIFICATION_PROPOSAL--move-existing-term-subject-paths.md) retains the existing Term Subject and defining R1318. Only the paths migrate; Terms Graph work remains deferred.

## Current result

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md) and [completed Epic P2673](../03_plan/CA-P-2673-EPIC--subject-refinement-stage-3.md).
