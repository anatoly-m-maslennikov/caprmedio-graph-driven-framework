---
atom_id: CA-A-1302@1-draft
ref_id: CA-A-1302@1-draft
container:
  scope_unit: CA-SU-00
role: Analysis
form: Specification Proposal
topics:
  main_subject: Entity
tier: 3
status: Draft
version: 1
updated_at: 2026-10-29 07:12:41 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Entity graph candidate with four root branches

## Root decision

Entity is the single root. Every primary graph node and every dependent property is an Entity. Object is narrower: Objects are the abstractions described by the framework, with Continuant and Occurrent specializations. Not every Entity is an Object.

Carrier is a sibling root branch, not a specialization of Object/Continuant. It describes how Objects or their information are represented/stored. A live Occurrent is not stored as the occurrence itself; a persistent record about it can have a Carrier. Do not conflate the occurrence with its record.

## Primary structure — three levels

```text
Entity
	/Object
		/Continuant
		/Occurrent
	/Aspect
		/Design
		/Documentation Aspect
		/Domain
		/Engineering
		/Product
		/Project Aspect
		/UX
	/Graph Syntax
		> Relation
		> Format
		> Cardinality
	/Carrier
		/Database
		/Directory
		/Docker Image
		/File
		/Git Branch
		/Git Commit
		/Git Index
		/Git Repository
		/Pull Request
```

This is the current classification skeleton, not a new namespace or project-scope hierarchy. Retain organizational/provenance views separately. The previous detailed candidate A1239 supplies the lower-level inventory pending remapping; do not treat its old Model root or bare Definition Type as the latest decision. Term and Selection placements remain explicit follow-up work rather than silently declaring that every Entity is an Object.

## Operations Types

```text
Atom/Content Role: Operations
	/Type: Workflow
		>{1+} Atom/Content Role: Operations/Type: Step
			>{0+} Atom/Content Role: Operations/Type: Sub-step
	/Type: Action
```

These are fully qualified Operations Atom Types. Repeat the Role/Type at each containment boundary rather than relying on inheritance through >. Step and Sub-step are declared only inside their required containers. Keep the settled leaf-call and recursion rules. A1304 defines the explicit presentation and operator spacing; relative-navigation syntax remains undecided.

## Relation Definition Type and notation

R/Type: Relation Definition defines named Relation Types. content.notation_for_subject is a fenced Markdown property under ## Notation for subject when a short Subject notation is defined. Retained short operators are :, >, /, // and .; their actual meaning/direction stays with the corresponding Relation Definition. The general named form remains ((RELATION_TYPE)). No organizational :: operator is needed in this candidate.

## Definition coverage

Every Entity, including a dependent property, needs R/Type: Entity Definition authority. Reuse existing Rs that already define it before creating missing Definitions. Each property's governing Entity Definition must state its cardinality and value format in the Formal claim. Preserve the settled direct-value semantics: counts are independent of child properties, subjects{0} allows declared children, an omitted count is undefined, and list/map/ref are not value Formats.

Do not invent a value Format for a zero-direct-value grouping property; record that remaining format-applicability detail for resolution. Simple formats/cardinalities and prose conditions remain the current scope; advanced formulas and conditions in [] remain separate proposals.

Rename the prepared Requirement Type Definition to Entity Definition. Reserve Term Definition as the distinct Requirement Type for defining a Term's meaning. Relation Definition separately defines the named instances of the Relation structure. This declares the Type boundary, not actual Term Definition Atoms or Terms Graph implementation. Entity Definition Type definitions are general, not limited to the old Model/Graph Rule use case.

## Representation policies

Every Object and property needs applicable D coverage explaining its representation, or the absence of direct storage for an Occurrent and the representation of its records. Use general reusable rules rather than enumerating one storage edge for every property instance.

Examples: ordinary metadata properties are carried in YAML; content.* is carried in Markdown sections. An allowed-value qualifier names a property and allowed value: Atom/Content Role: Concern corresponds to the content_role property; the supplied example serializes it as content_role: concern. D defines the concrete field/value representation; do not duplicate classification facts as extra entities.

D/Type: Policy is for reusable representation rules; D/Type: Decision is for an individual case. Its governing Subject is the represented Entity. Define the needed entity-to-Carrier relation and check existing uses/definitions before inventing another name. No new Carrier kind is needed just to name every YAML field or Markdown section.

The existing Carrier kinds above are retained. Add missing Carrier Definitions or kinds only when a concrete representation needs them; do not add speculative storage infrastructure.

## Prepared sources

New root/Object and Type Definition Drafts accompany this candidate. A1303 adds the qualified Operations Types and the Relation Definition Type with its notation field. Existing prepared Entity Definition headers have been renamed where authorized; full Subject and carrier-name reconciliation belongs to the planned migration/adoption stages. R2110's old bare-Definition-Type preparation is superseded, not promoted. Current sources are unchanged.

## Adoption boundary

This supersedes A1239 only for the root/classification and Definition-Type decisions stated here. A1239 and past reports remain historical/detail evidence. The Epic must migrate Subjects first, then adopt corrected Drafts, complete Definition coverage, rebuild from Current sources and review. This candidate alone is not a source migration or proof that all Definitions/properties/D policies are complete.

## Pending lower-level reconciliation

The previous detailed inventory and old operator Drafts still need the planned root/Type/operator Subject migration. Do not infer that their bare Step/Substep paths or :: usages have already been rewritten. Define the newly displayed Cardinality entity through the existing cardinality meaning during Definition coverage, rather than inventing a separate execution rule.

## Relation-token spacing

Write whitespace around the complete relation token, including its attached cardinality: Whole >{1+} Part. Tree indentation supplies left whitespace; a space follows the token. Keep internal /, // and . path separators compact. A1304 records this rule.

## Implementation Questions

[CA-A-1305](../CA-A-1305-SPECIFICATION_PROPOSAL--track-entity-candidate-implementation-questions.md) tracks every C/Question and the selected continuation during implementation, using the latest 48 hours of Operator input. Term/Selection placement and zero-direct-value Format applicability are explicit provisional choices there.
