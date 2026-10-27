---
subjects:
  governs: Subject/Graph Relation
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Relation/Type
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Rule
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Source Unit Responsibility
version: 41
updated_at: 2026-10-26 17:20:40 +0400
relations:
  evaluation_for:
  - CA-R-806
  - CA-R-1246
  - CA-R-1437
  - CA-R-1472
  - CA-M-120
  - CA-R-1676
  - CA-R-1580
  - CA-R-807
  - CA-D-268
  - CA-R-1040
  - CA-D-483
  - CA-D-466
atom_id: CA-E-622@41
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
# Summary

Canonical relation validity

## Scope

- admit **`=1`** valid example of each selected known Relation Type under its defining Claim; evaluate any applicable Graph Rule constraints without inventing a default.
- reject an unknown Relation Type; report missing or conflicting Rule evidence as unresolved only when an existing source contract requires that evidence, without treating every known Type as requiring a new Rule.
- reject a Relation that violates endpoint or cardinality constraints in an applicable Graph Rule; do not choose default-allow/default-deny when such evidence is absent.
- resolve **every** target **to** **`=1`** addressable identity under its relation rules; reject missing **or** ambiguous targets.
- reject a non-Active RMED target of a direct Relation authored by an Active RMED Atom; read target Status from its own Markdown frontmatter under CA-D-483 **and** check lifecycle placement under CA-D-466. this Active-target restriction applies **only** **when** the source is Active **and** both source **and** target have Content Role **in** (Requirement, Method, Evaluation, Delivery). a source **or** target outside that boundary **must not** fail because of this restriction alone; its own applicable Relation constraints still apply.
- accept `A BLOCKS B` with Done Plan `A`; confirm that Backlog, Active, Canceled, **or** Archived blockers do **not** satisfy the Done start gate for `B`.
- confirm that an Archived target remains addressable as history **without** becoming Active authority.
- confirm that **every** independently authored direct Relation is persisted **only** **in** its registered declaration Carrier **and** that **every** inverse remains derived; validate a computed Relation against its admitted derivation authority **and** input facts **without** requiring an invented source declaration.
- confirm that replacement **and** absorption history uses explicit predecessor **and** successor identities **in** Journal events, **not** formal replacement relation payloads **in** active Atom frontmatter.
- accept valid uses of one shared Relation Type in multiple graph contexts while preserving each context's applicable Graph Rule evidence and existing admission semantics; do not invent a new per-context Rule.
- reject a missing or conflicting defining Relation Type Claim under CA-R-806; report missing or conflicting Graph Rule evidence only where an existing source contract requires it, without creating a new per-Type Rule gate.
- evaluate the same Relation Type in different graph contexts against any applicable Graph Rule evidence and existing admission semantics; an external endpoint or source reference does not itself create a native edge, and no default is invented when Rule evidence is absent.
- reject an invalid source class **and** an invalid target class independently while retaining the applicable Graph Rule context and other constraints.
- reject duplicate or conflicting definitions of one project-unique Relation Type name; resolve the shared Type by its canonical name and defining Claim rather than by a graph-qualified copy.
- reject instance-specific redefinitions of a project-shared Relation Type or of a Graph Rule's admission semantics.
- accept a source-traceable reference **or** derived graph view of a Relation fact; reject another independently maintained source declaration of the same fact **or** admission of a foreign Relation Type as native through that view.
- when a non-authoritative registry Projection is compiled, require it to preserve defining source traceability, canonical name, meaning and any declared direction/inverse/derivation/transitivity **without** inventing Type metadata or copying Graph Rule constraints into it.

- accept an admitted native Relation between nodes **in** the same secondary graph.
- accept an admitted typed reference **to** another secondary graph **or** its node while preserving endpoint identity **and** graph context.
- accept an admitted typed reference **to** a source Atom **without** making that Atom a native Term **or** other wrongly classified node.
- reject a cross-graph endpoint that violates an applicable Graph Rule's class **or** graph-context constraint, **even** **when** both endpoints exist; retain missing constraint evidence as unresolved without choosing default allow or default deny.
- reject loss of any applicable Graph Rule context, silent foreign-node import, **or** a projected Relation treated as independently authored authority; absence of a newly invented Rule is not itself a failure.
- accept a source-traceable derived Relation **without** its own direct source declaration **only** **when** the governing Relation authority admits that derivation; reject its use **to** bypass an explicit-declaration requirement.

## Claim

**every** known Relation Type accepts valid examples under its defining Claim; any applicable Graph Rule supplies additional source/target, cardinality, lifecycle, or other constraints. reject unknown Types and violations of explicit applicable constraints, while retaining missing or conflicting constraint evidence as unresolved without choosing default allow or default deny.

## Details

### Acceptance criteria

**all** valid fixtures pass **and** **every** invalid fixture fails with the exact Relation Type, Graph Rule context, metadata conflict, source declaration, endpoint, lifecycle restriction, **or** declaration Carrier identified.

### Failure disposition

record a Concern naming the affected Relation Type **and** violated authority **and** stop relation-schema readiness.
