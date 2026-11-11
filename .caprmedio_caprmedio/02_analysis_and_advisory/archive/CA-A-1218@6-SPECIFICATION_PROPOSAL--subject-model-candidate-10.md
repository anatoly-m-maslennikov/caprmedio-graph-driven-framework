---
atom_id: CA-A-1218@6
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 6
updated_at: 2026-10-27 18:12:00 +0400
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

This is a Specification Proposal, not adopted RMED or a rebuilt Subject Graph. New and revised R Atoms remain Drafts. Existing definitions are reused; a node with a newly drafted definition is not yet defined by Current RMED.

```text
Subject  [CA-R-1275]
	/CAPRMEDIO  [CA-R-2206]
		/Graph  [CA-R-2208]
			/Node  [CA-R-1994]
				/Project Model  [CA-R-2209]
					/Actor  [CA-R-2218]
					/Atom  [CA-R-655]
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
					/Project  [CA-R-2220]
					/Projection  [CA-R-1746]
					/Runtime  [CA-R-2194]
					/Scope Unit  [CA-R-1757]
					/Selection  [CA-R-1966]
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
	/<Project Name>  [CA-R-2207]
```

`<Project Name>` describes a namespace pattern; it is not an instantiated project Subject. CAPRMEDIO is the shared framework vocabulary namespace. Projects use that vocabulary and add their own Subjects without copying it. Namespace, Graph and Project Model headings organize the vocabulary; they do not assert that every child is a subtype of a new real-world entity.

Event and Execution retain existing meanings rather than disappearing during regrouping. History/Journal/Release describe preserved material, while Event, Execution and Runtime describe actual occurrences or contexts. Implementation is directly edited and is not a Projection.

## Defining R Atoms

Current means the currently governing definition; Draft means the proposed successor or a missing-definition proposal. Definitions below summarize those sources; the linked R Atom remains the authority after any approved promotion.

| Main Subject | Defining R Atom | Definition | State |
|---|---|---|---|
| Subject | [CA-R-1275@25](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL--define-subject.md) → [CA-R-1275@26-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1275@26-draft-CORE_META_MODEL--define-subject.md) | a Subject names the thing or topic an Atom governs or depends on. | Current + prepared Draft |
| CAPRMEDIO | [CA-R-2206@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2206@1-draft-CORE_META_MODEL-DEFINITION--define-caprmedio-subject-namespace.md) | The CAPRMEDIO Subject namespace qualifies the shared vocabulary supplied by the CAPRMEDIO framework. It separates that vocabulary from a project’s own subjects. | New Definition Draft |
| Graph | [CA-R-2208@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2208@1-draft-CORE_META_MODEL-DEFINITION--define-graph.md) | Graph is the Subject grouping for Node, Relation and Rule: the things or topics represented, their typed connections and the constraints on Nodes, Relations and their properties. | New Definition Draft |
| Node | [CA-R-1994@10](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md) → [CA-R-1994@11-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1994@11-draft-CORE_META_MODEL--define-entity-node.md) | A Node identifies a thing or topic addressed by the graph. Its description and Carrier are separate. | Current + prepared Draft |
| Project Model | [CA-R-2209@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2209@1-draft-CORE_META_MODEL-DEFINITION--define-project-model.md) | Project Model groups Subjects for what exists in a project: its Atoms, governing configurations, Scope Units, Actors, history, Projections, Selections, Implementation and actual execution contexts. | New Definition Draft |
| Actor | [CA-R-2218@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2218@1-draft-CORE_META_MODEL-DEFINITION--define-actor.md) | An Actor is a participant that performs work, provides input or exercises authority in the project. | New Definition Draft |
| Atom | [CA-R-655@33](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL--define-atom-artifact-form.md) → [CA-R-655@34-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-655@34-draft-CORE_META_MODEL--define-atom-artifact-form.md) | an Atom means the smallest independently governed Artifact. | Current + prepared Draft |
| Event | [CA-R-1968@7](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1968-CORE_META_MODEL-DEFINITION--define-entity-occurrent-event.md) → [CA-R-1968@8-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1968@8-draft-CORE_META_MODEL-DEFINITION--define-entity-occurrent-event.md) | an Event means an actual occurrence. a record describing the Event is not the Event itself. | Current + prepared Draft |
| Execution | [CA-R-1970@7](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1970-CORE_META_MODEL-DEFINITION--define-entity-occurrent-execution.md) → [CA-R-1970@8-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1970@8-draft-CORE_META_MODEL-DEFINITION--define-entity-occurrent-execution.md) | an Execution means the actual performance of work. it is distinct from its reusable definition and from records describing what happened. | Current + prepared Draft |
| Governing Configuration | [CA-R-1962@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1962-CORE_META_MODEL--define-entity-continuant-object-governing-configuration.md) → [CA-R-1962@9-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1962@9-draft-CORE_META_MODEL--define-entity-continuant-object-governing-configuration.md) | Governing Configuration means authoritative non-Atom content that supplies declared structural facts or selected configuration values for a Project. it is not a derived Projection. | Current + prepared Draft |
| History | [CA-R-1961@9](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1961-CORE_META_MODEL--define-entity-continuant-history.md) → [CA-R-1961@10-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1961@10-draft-CORE_META_MODEL--define-entity-continuant-history.md) | History means preserved earlier state or records of what happened. Preserved earlier versions and Journals belong to History; the events or executions they record do not. | Current + prepared Draft |
| Journal | [CA-R-1745@30](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1745-CORE_META_MODEL--define-journal-artifact-form.md) → [CA-R-1745@31-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1745@31-draft-CORE_META_MODEL--define-journal-artifact-form.md) | a Journal, also called an Event Log, means an authoritative Artifact whose recorded history forms `=1` logically ordered table of admitted records about events. technical and business runtime logs are Journals. a record describes an event and its recorded evidence; the record is not the event itself or automatic proof of its asserted outcome. accepted records must… | Current + prepared Draft |
| Release | [CA-R-2171@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2171-CORE_META_MODEL-DEFINITION--define-release.md) → [CA-R-2171@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2171@2-draft-CORE_META_MODEL-DEFINITION--define-release.md) | A Release means a historical delivery unit of Implementation. | Current + prepared Draft |
| Implementation | [CA-R-2173@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2173-CORE_META_MODEL-DEFINITION--define-implementation.md) → [CA-R-2173@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2173@2-draft-CORE_META_MODEL-DEFINITION--define-implementation.md) | Implementation means the actual Code, Prompts, Documentation and Resources that realize RMED for a Project. Directly edited Implementation can be authoritative for what is actually implemented. | Current + prepared Draft |
| Code | [CA-R-2174@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2174-CORE_META_MODEL-DEFINITION--define-code.md) → [CA-R-2174@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2174@2-draft-CORE_META_MODEL-DEFINITION--define-code.md) | Code means program instructions and definitions that realize behavior. | Current + prepared Draft |
| Implementation/Documentation | [CA-R-2180@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2180-CORE_META_MODEL-DEFINITION--define-documentation.md) → [CA-R-2180@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2180@2-draft-CORE_META_MODEL-DEFINITION--define-documentation.md) | Documentation means Implementation content used for explanation, instruction or reference. | Current + prepared Draft |
| Prompts | [CA-R-2179@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2179-CORE_META_MODEL-DEFINITION--define-prompts.md) → [CA-R-2179@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2179@2-draft-CORE_META_MODEL-DEFINITION--define-prompts.md) | Prompts mean Implementation instructions or requests addressed to an Actor. | Current + prepared Draft |
| Resources | [CA-R-2189@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2189-CORE_META_MODEL-DEFINITION--define-resources.md) → [CA-R-2189@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2189@2-draft-CORE_META_MODEL-DEFINITION--define-resources.md) | Resources mean Implementation data, apart from Code, Prompts and Documentation, used to construct, configure, evaluate or render a result. | Current + prepared Draft |
| Project Model/Project | [CA-R-2220@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2220@1-draft-CORE_META_MODEL-DEFINITION--define-project.md) | Project means the whole project as one entity, distinct from any particular part such as an Atom or Implementation. | New Definition Draft |
| Projection | [CA-R-1746@35](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1746-CORE_META_MODEL--define-projection-artifact-form.md) → [CA-R-1746@36-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1746@36-draft-CORE_META_MODEL--define-projection-artifact-form.md) | A Projection is a non-authoritative output produced from a declared selection of sources through a Workflow: source of truth → Workflow → Projection. A Projection is not edited directly. Changes are made in its authoritative sources, then the Projection is rebuilt through its Workflow. Its sources may include other Projections; represented facts remain traceable… | Current + prepared Draft |
| Runtime | [CA-R-2194@1](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2194-CORE_META_MODEL-DEFINITION--define-runtime.md) → [CA-R-2194@2-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2194@2-draft-CORE_META_MODEL-DEFINITION--define-runtime.md) | Runtime means an actual technical execution context for Implementation. | Current + prepared Draft |
| Scope Unit | [CA-R-1757@27](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1757-CORE_META_MODEL--define-scope-unit.md) → [CA-R-1757@28-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1757@28-draft-CORE_META_MODEL--define-scope-unit.md) | a Scope Unit means a Continuant Node that provides an ownership boundary for Atoms and may contain child Scope Units. | Current + prepared Draft |
| Selection | [CA-R-1966@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1966-CORE_META_MODEL--define-entity-continuant-selection.md) → [CA-R-1966@9-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1966@9-draft-CORE_META_MODEL--define-entity-continuant-selection.md) | a Selection means criteria for choosing members. a named Selection gives those criteria a name; it does not create another Object or independent copies of the selected members. | Current + prepared Draft |
| Aspect | [CA-R-2210@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2210@1-draft-CORE_META_MODEL-DEFINITION--define-aspect.md) | An Aspect is a topic through which an Atom addresses a thing, rather than another copy of that thing. | New Definition Draft |
| Design | [CA-R-2216@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2216@1-draft-CORE_META_MODEL-DEFINITION--define-design-aspect.md) | The Design Aspect addresses the form, presentation and arrangement of an interface or other delivered material. | New Definition Draft |
| Aspect/Documentation | [CA-R-2217@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2217@1-draft-CORE_META_MODEL-DEFINITION--define-documentation-aspect.md) | The Documentation Aspect addresses how explanatory, instructional and reference material is organized and written. | New Definition Draft |
| Domain | [CA-R-2213@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2213@1-draft-CORE_META_MODEL-DEFINITION--define-domain-aspect.md) | The Domain Aspect addresses the meanings and behavior specific to the project’s problem domain. | New Definition Draft |
| Engineering | [CA-R-2214@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2214@1-draft-CORE_META_MODEL-DEFINITION--define-engineering-aspect.md) | The Engineering Aspect addresses technical architecture, authoring, verification, delivery, storage, data handling, execution control, traceability and observability. | New Definition Draft |
| Product | [CA-R-2211@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2211@1-draft-CORE_META_MODEL-DEFINITION--define-product-aspect.md) | The Product Aspect addresses what a project produces or offers and the outcomes or capabilities expected from it. | New Definition Draft |
| Aspect/Project | [CA-R-2212@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2212@1-draft-CORE_META_MODEL-DEFINITION--define-project-aspect.md) | The Project Aspect addresses how project work is organized and governed. | New Definition Draft |
| UX | [CA-R-2215@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2215@1-draft-CORE_META_MODEL-DEFINITION--define-ux-aspect.md) | The UX Aspect addresses how an Actor discovers, understands and uses an interface and receives its results. | New Definition Draft |
| Relation | [CA-R-1963@9](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1963-CORE_META_MODEL--define-entity-continuant-object-relation.md) → [CA-R-1963@10-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1963@10-draft-CORE_META_MODEL--define-entity-continuant-object-relation.md) | a Relation means a typed connection between identified endpoints. its shared Relation Type and defining authority determine the connection's meaning and declared direction; any applicable Graph Rules supply endpoint, graph-context, and cardinality constraints. | Current + prepared Draft |
| Rule | [CA-R-1995@10](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1995-CORE_META_MODEL--define-entity-graph-rule.md) → [CA-R-1995@11-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1995@11-draft-CORE_META_MODEL--define-entity-graph-rule.md) | a Graph Rule means a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality. | Current + prepared Draft |
| Carrier | [CA-R-1958@8](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1958-CORE_META_MODEL--define-entity-carrier.md) → [CA-R-1958@9-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1958@9-draft-CORE_META_MODEL--define-entity-carrier.md) | A Carrier means a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, not the Occurrent itself. | Current + prepared Draft |
| <Project Name> | [CA-R-2207@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2207@1-draft-CORE_META_MODEL-DEFINITION--define-project-subject-namespace.md) | A Project Subject namespace qualifies the project-specific things and topics named under Subject/<Project Name>. | New Definition Draft |

## Definition boundaries

- Project Model names project things, including Implementation. Aspects name topics addressing those things. CAPRMEDO Atoms and I Implementation are different structures inside the model; not every Project Model item is an Atom.
- Content Role is a classification axis and remains a valid Subject; it is not another primary entity between Atom and role-qualified Atom kinds. The R1531 Draft defines this distinction. No role values or instances are expanded in this main tree.
- A Carrier is distinct from what it represents. A graph can represent a Carrier as a node without merging representation with represented content.
- Documentation under Implementation is actual content; Documentation under Aspect is the topic governing its organization and authoring.
- Subject, Content Role and owning Scope Unit stay independent. A shared Subject does not become project-specific because its governing Atom lives in Project Configuration.
- This proposal does not reintroduce Revision, property entities, generic Graph Node.Type, or Terms-Graph work. Existing Continuant/Occurrent definitions remain available, but their temporal classifications are not mandatory path layers in this proposed main outline.

## Review boundaries and open points

The proposed graph and namespace groupings are organizational levels, not automatically NARROWER_THAN edges. The completed bounded review found no concern from the outline alone; it did not establish complete grammar admission. The project-name placeholder does not choose name normalization or collision/rename handling. These are unresolved proposal details, not new runtime requirements. Current generic Entity terminology and deferred Term dependencies are preserved for review rather than silently retired.

## Work and decisions

[Subject refinement stage 3 Epic](../03_plan/done/CA-P-2673-EPIC--subject-refinement-stage-3.md) holds the Tasks, thin Draft table and links to decision proposals. Candidate #9 remains historical context; Candidate #10 proposes its replacement structure and is not yet applied. The new Analysis Type is defined by [CA-R-2219@1-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2219@1-draft-CORE_META_MODEL-DEFINITION--define-specification-proposal-analysis-type.md).

## Preparation state

42 real Drafts are prepared: 15 new Definition Drafts, 19 existing primary-Definition successors and 8 related anchor Drafts. All displayed main Subjects have a linked defining Current R Atom and/or real Definition Draft. Current originals were not promoted or migrated. Legacy Term dependency destinations remain explicitly unresolved; this does not create Term instances in the Candidate. The FPF design challenge and independent validation are complete. Its two findings are tracked in P2677; C10-I01 is resolved by the Operator-approved clarification and refined Drafts. C10-I02 is resolved by the Operator’s whole-project entity definition, reflected in R2220@1-draft. The review’s undertaking-based C10-F02 wording is superseded. No Draft has been promoted.

## Decision proposals

- [A1219 — Clarify mixed Subject targets](CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md): Operator-accepted resolution of C10-I01; reflected in the R1994 and R2209 Drafts.

- [A1220 — Define Project as a whole entity](CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md): Operator resolution of C10-I02; reflected in R2220@1-draft.

Each accepted review decision has its own Specification Proposal file. Work and progress remain in P Atoms, with links to those proposals.
