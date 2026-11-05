---
atom_id: CA-A-1238
ref_id: CA-A-1238
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-A-1238-CAPRMEDIO-SPECIFICATION_PROPOSAL--subject-model-candidate-12.md
    path: .caprmedio_caprmedio/02_analysis
---
# Summary

Subject model Candidate #12

## Question

What is the primary Subject graph when its six base classifications are Continuant, Occurrent, Aspect, Carrier, Graph Relation and Graph Rule?

## Status and authority

Candidate #12 records the Operator's latest classification decision and constructs a proposed primary graph from existing definitions. It supersedes Candidate #11's Project Model classification wrapper. It is not the current-source Projection and does not claim a source migration, Draft promotion or runtime change.

Project Model may name an optional organizational view. It is not a seventh base classification. Graph and Node wrappers are omitted from this classification view; their concepts are not thereby retired. CAPRMEDIO and caprmedio remain vocabulary namespaces, not additional classifications or instances.

All six classifications sit under the shared CAPRMEDIO namespace. No cross-classification between these bases is inferred merely from their placement. Carrier remains its own base classification. Existing-kind references also make a contained Step a Continuant without declaring an independently existing Step.

## Notation

- `::` groups Subjects without inheritance.
- `/` specializes a kind with applicable inheritance.
- `>` declares structural containment; `>@(...)` uses an already declared part kind.
- `@(...)` refers to one existing kind, including forward references. It introduces no copy, alias or instance.
- `:` qualifies an allowed value, as in Atom/Content Role: Plan. The Content Role axis is not shown as a separate entity.
- Properties and `//` instances are excluded. Relation Types and Graph Rule instances belong to their separate view.

Indentation uses actual tabs. Defining references contain Atom IDs only, never copied Claims. This is a primary-kind outline, not the full catalog of allowed Types, properties, relation permissions or cardinalities.

## Primary Subject graph

```text
Subject [CA-R-1275]
	::CAPRMEDIO [CA-R-2206]
		::Continuant [CA-R-1967]
			/Actor [CA-R-2218]
				/AI Agent [CA-R-1959]
				/Operator [CA-R-1422]
			/Atom [CA-R-655]
				/Content Role: Analysis [CA-R-1337]
				/Content Role: Concern [CA-R-1336]
				/Content Role: Delivery [CA-R-1342]
				/Content Role: Evaluation [CA-R-1341]
				/Content Role: Method [CA-R-1340]
				/Content Role: Operations [CA-R-1530]
					/Type: Action [CA-R-1452]
					/Type: Workflow [CA-R-1508]
						>Step [CA-R-1509; successor Draft]
							>Substep [new Definition Draft; ID pending]
				/Content Role: Plan [CA-R-1338]
					>@(Subject::CAPRMEDIO::Continuant/Atom/Content Role: Plan)
				/Content Role: Requirement [CA-R-1339]
			/Code [CA-R-2174]
				/Class [CA-R-2176]
				/Function [CA-R-2175]
				/Module [CA-R-2177]
				/Package [CA-R-2178]
					>@(Module)
					>@(Package)
				/Tool [CA-R-2197]
			/Documentation [CA-R-2180]
				/Code Block [CA-R-2187]
				/Diagram [CA-R-2188]
				/Document [CA-R-2181]
					>Section [CA-R-2182]
						>@(Section)
				/List [CA-R-2185]
				/Paragraph [CA-R-2183]
				/@(Section)
				/Sentence [CA-R-2184]
				/Table [CA-R-2186]
			/Event Record [standalone Definition pending]
			/Governing Configuration [CA-R-1962]
			/History [CA-R-1961]
				/Journal [CA-R-1745]
					>@(Event Record)
				/Release [CA-R-2171]
			/Implementation [CA-R-2173]
				>@(Code)
				>@(Documentation)
				>@(Prompts)
				>@(Resources)
			/Project [CA-R-2220]
			/Projection [CA-R-1746]
			/Prompts [CA-R-2179]
			/Resources [CA-R-2189]
				/Configuration [CA-R-2190]
				/Schema [CA-R-2191]
				/Template [CA-R-2192]
				/Test Fixture [CA-R-2193]
			/Scope Unit [CA-R-1757]
				>@(Atom)
				>@(Projection)
				>@(Scope Unit)
			/Selection [CA-R-1966]
			/Term [CA-R-1318]
			/@(Step)
			/@(Substep)
		::Occurrent [CA-R-1972]
			/Event [CA-R-1968]
			/Execution [CA-R-1970]
				/Action Run [CA-R-1969]
				/Container Run [CA-R-2195]
				/Process Run [CA-R-2196]
				/Step Run [CA-R-1511]
				/Workflow Run [CA-R-1510]
			/Runtime [CA-R-2194]
			/Session [CA-R-1971]
		::Aspect [CA-R-2210]
			::Design [CA-R-2216]
			::Documentation Aspect [CA-R-2217]
				::@(Traceability)
			::Domain [CA-R-2213]
			::Engineering [CA-R-2214]
				::Architecture
					::Communication
					::Component Structure
				::Authoring
					::Code Authoring
						::Python Code Authoring
					::Controlled English
					::Prompt Authoring
				::Data Handling
					::Data Transformation
					::Data Validation
					::Output Publication
					::Parsing
					::Serialization
					::Source Retrieval
					::Source Selection
				::Delivery
					::Extension Lifecycle
					::Git Commits
				::Execution Control
					::Decision Confidence
					::Effect Authorization
					::Failure Handling
					::Recovery
				::Observability
					::Logging
					::Monitoring
				::Storage
					::Directory Layout
				::Traceability
				::Verification
					::Coverage
					::Dynamic Testing
					::Static Analysis
						::Python Static Analysis
					::Test Data
						::Golden Corpora
					::Test Design
			::Product [CA-R-2211]
			::Project Aspect [CA-R-2212]
			::UX [CA-R-2215]
				::Discovery and Navigation
				::Entry
				::Guidance
				::Interaction
					::Accessibility
					::Decision
				::Result and Status Presentation
		::Carrier [CA-R-1958]
			/Database [CA-R-1955]
			/Directory [CA-R-1956]
			/Docker Image [CA-R-2198]
			/File [CA-R-1957]
			/Git Branch [CA-R-2200]
			/Git Commit [CA-R-2199]
			/Git Index [CA-R-2202]
			/Git Repository [CA-R-2203]
				>@(Git Branch)
			/Pull Request [CA-R-2201]
		::Graph Relation [CA-R-1963]
		::Graph Rule [CA-R-1995]
	::caprmedio [CA-R-2207; project namespace, no instances expanded]
```

## Reading the structure

An Atom, Actor, Scope Unit, Implementation artifact or Journal record persists as a thing: Continuant. An actual Event, Execution, live Runtime or Session happens: Occurrent. Runtime follows the Operator's earlier ephemeral-runtime decision; being idle while alive does not turn it into a stored record. Container Run and Process Run are execution kinds, not Docker Image or File Carriers.

Code, Documentation, Prompts and Resources are Implementation parts. They also have their own Continuant classifications. Package may contain an existing Module, while Module remains independently declared. Workflow contains Step; Step contains the distinct Substep. Action stays reusable and is not inferred to be a contained part of every Step.

Scope Unit references child Scope Units, Atoms and Projections as structural parts. This does not infer property inheritance, change an Atom's local owner, or remove the Operator-owned Project Goal exception. Recursive kind references describe possible schemas, not self-containing individual instances.

Journal contains Event Records, not actual Events. Release is a historical delivery unit; a Journal record about releasing is a separate thing. Revision remains obsolete and is not reintroduced.

## Proposed label corrections

| Existing context | Candidate label | Reason |
|---|---|---|
| Aspect/Documentation | Documentation Aspect | Distinguish the topic from actual Documentation; reuse R2217's defined name. |
| Aspect/Project | Project Aspect | Distinguish the topic from the Project object; reuse R2212's defined name. |
| Code Authoring/Python Code | Python Code Authoring | Name writing in Python, without duplicating the static-analysis topic. |
| Static Analysis/Python Code | Python Static Analysis | Name Python-specific checks, distinct from authoring in Python. |
| Documentation/Traceability | Reference the existing Traceability topic | One declaration, reused by organizational reference. |

These are proposed source-name corrections, not applied renames. The Aspect topics without a bracketed R ID are retained from the existing primary view; this candidate does not invent dedicated Definition IDs or claim those topics all have standalone Definition Atoms.

## Definition and adoption gaps

- Substep has an existing Definition Draft but no assigned canonical numeric R ID. The graph marks that gap rather than inventing one. Further Substep nesting and inheritance are not inferred.
- Event Record is explicitly distinguished in R1968 and R1745; a standalone Definition Atom is still missing. Its classification is supported, but definition completeness is not claimed.
- Taxonomy paths and structural-containment paths must not accidentally grant independent existence to a kind merely because it is classified or displayed. The earlier declaration/standalone rule needs this distinction checked before migration. This candidate uses references for Step/Substep classification and does not waive their required containers.
- Section's defining text says subdivision of Document or Section. Its part edges are shown, but exact cardinality and independent-existence permissions need rule-level confirmation; projection indentation cannot decide them.
- Current selector paths, the older Project Model Draft and notation consumers still express earlier versions. This document does not update them. The migration must use this candidate plus the accepted notation decisions, not infer adoption from this graph.

## Sources and boundaries

The existing Current-RMEDO primary Projection (CA-PROJ-010) supplied the previous displayed vocabulary. Definitions were checked in the governing METHODOLOGY_SOURCES tree, excluding archived, Draft and derived replicas. CA-A-1236 holds the accepted notation decisions and successor Draft register. CA-A-1237's function proposals remain excluded.

No existing Current RMEDO, governing configuration, code, Draft or generated Projection was changed to create this candidate. The only new source artifact is this Specification Proposal, with its real creation event in the Journal.
