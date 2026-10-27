---
atom_id: CA-P-2667@3
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering
version: 3
updated_at: 2026-10-27 04:47:08 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2665
tier: 4
work_sequence_number: 2
---
# Summary

Settle Engineering Subject structure

## Objective

Record Candidate #9 and settle the approved Subject branches before applying their source migrations.

## Details

### Candidate #9 — approved Subject model

These latest Operator decisions override incompatible earlier candidates, Drafts and Current model text. This Task is the Candidate #9 decision record. The thin table records individual Subject changes; the proposed RMED lives in real Draft Atoms.

#### Branches

```text
Subject
	/Graph Node
		/Domain
			/Continuant
				/History
					/Journal
					/Release
						.ID — Version
			/Occurrent
		/Engineering
			/Architecture
				/Component Structure
				/Communication
					/API
			/Authoring
			/Verification
			/Delivery
			/Storage
			/Data Handling
			/Execution Control
			/Traceability
			/Observability
				/Logging
				/Monitoring
		/Implementation
			/Code
				/Function
				/Class
				/Module
				/Package
			/Prompts
			/Documentation
				/Document
				/Section
				/Paragraph
				/Sentence
				/List
				/Table
				/Code Block
				/Diagram
			/Resources
				/Configuration
				/Schema
				/Template
				/Test Fixture
		/Runtime
			/Container Run
			/Process Run
			/Session
		/Carrier
			/File
			/Directory
			/Database
			/Docker Image
			/Git Commit
			/Git Index
			/Git Branch
			/Git Repository
			/Pull Request
		/Product
		/UX
		/Documentation
	/Graph Relation
	/Graph Rule
```

The tree shows the changed branches and representative children. Existing Domain descendants, Product instances, UX topics and Documentation topics remain unless an approved decision changes their meaning. It is not an exhaustive enumeration.

#### Meaning and boundaries

- Engineering names aspects and practices: architecture, authoring, verification, delivery, storage, data handling, execution control, traceability and observability. Its old Continuant/Occurrent branches move to the appropriate new branches. Flatten Engineering/Aspect to Engineering.
- Implementation names the actual logical realization: Code, Prompts, Documentation and Resources. Content Role I and Subject classification remain independent.
- Code has logical units such as Function, Class, Module and Package. A physical folder is a Directory Carrier; a logical package groups code units.
- Documentation has logical content units. Document, Section, Paragraph, Sentence, List, Table, Code Block and Diagram are kinds; use containment for their actual whole/part structure, not subtype nesting. One file can represent many content units.
- JSON, TOML, Markdown and Mermaid describe format or syntax, not a new logical resource kind. Mermaid is a diagram syntax.
- Runtime names actual technical executions, including sessions and tool/app/service, process and container runs. Modeled business Action, Step and Workflow Runs stay in Domain/Occurrent.
- Carrier names representation and storage. For this model, Docker Image is a Carrier of packaged Implementation; container execution belongs to Runtime. Files, directories and databases remain Carriers. Git Commit, Git Branch and Pull Request are Carriers under the latest Operator decision.
- A Git Index represents the staged-file snapshot. A remote GitHub repository or branch is another Carrier; the legacy Git Remote Subject names the Git Repository Carrier, while connection details remain in Content Scope.
- Release belongs to Domain/Continuant/History/Release. Its ID is called Version. Release identifies what was delivered; a Journal entry records that a release happened. Do not merge the delivered version with the event record about it.
- Local Release and Public Release remain named Workflows. Their definitions and workflow-specific RMED belong in PROJECT_CONFIGURATION.
- API-specific transport contracts use Engineering/Architecture/Communication/API. This Subject decision does not remove runtime Host/Origin checks.
- Subject, Content Role, Type, Tier and Local Scope Unit remain independent. A moved Subject does not by itself change an Atom's ownership, role or meaning. Do not copy Scope Unit or Tool identities into topic branches.
- Existing notation remains: / broader-to-narrower kind; . bearer-to-dependent property; : allowed value; // named instance; > whole-to-part using containment. Keep full canonical Subject paths in source data.
- Do not invent a new Domain kind to force a mapping. Classify remaining technical kinds from their source meaning; ask the Operator when confidence is below 90%.

#### Application

1. Compare Current sources and their prepared correction Drafts with this model.
2. Record Governs changes first, then Depends On, in one thin table: Atom ID | old Subject | new Subject | status.
3. Preserve prior supported Draft corrections and unrelated work. Create or refine the next-version Draft of each affected Atom.
4. Reuse existing R/Definition Atoms with the same meaning. Create missing Definition Drafts. Keep technology-specific definitions in PROJECT_CONFIGURATION; update shared Core model rules in their existing Core scope.
5. Review the exact Draft batch. Apply accepted successors with normal predecessor archives; preserve identity unless Summary or Content Role changes.
6. Rebuild the Current Subject views from applied sources. Drafted and Applied are separate states; list unresolved mappings explicitly.

No code, Tool, runtime, release execution or general Scope Unit reorganization is part of this migration.


The thin progress table is [Candidate #9 Subject changes](../../_projection/core-entity-review/presentation/candidate-9.subjects.md).

## Definition of Done

- Candidate #9 reflects the latest Operator decisions and supersedes incompatible prior placements.
- Every affected Subject has a supported target or an explicit unresolved decision; no new Domain kind is invented.
- Required model changes and missing definitions have real RMED Drafts before promotion.
