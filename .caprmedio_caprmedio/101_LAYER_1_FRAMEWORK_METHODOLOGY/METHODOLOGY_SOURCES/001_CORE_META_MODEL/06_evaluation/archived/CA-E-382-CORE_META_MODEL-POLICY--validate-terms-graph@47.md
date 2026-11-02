---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Terms Graph'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
  - Entity/Object/Continuant/Term
  - Entity/Graph Syntax > Relation//NARROWER_THAN
  - Entity/Graph Syntax > Relation
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Projection
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Entity Definition'
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Continuant/Governing Objects/Atom
version: 47
updated_at: 2026-10-29 14:12:43 +0400
relations:
  evaluation_for:
  - CA-R-1335
  - CA-R-1246
  - CA-R-1435
  - CA-R-1244
  - CA-R-1345
  - CA-R-1347
  - CA-R-1319
  - CA-R-1454
  - CA-R-1437
  - CA-R-1472
atom_id: CA-E-382
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eval Policy
tier: 3
---
## Summary

Validate Terms Graph

## Claim scope

Terms Graph validity **and** Terms Graph Projections **when** that native graph Evaluation is separately selected. This graph-specific Evaluation is optional **and** is **not** a prerequisite for directly checking Term Definitions **and** authored occurrences under CA-E-444.

## Claim

The selected native Terms Graph Evaluation **must** preserve the following graph-validity, source-authority **and** Projection-fidelity boundaries.

### Graph validity

the Evaluation **must** reject a Terms Graph **if** **any** of:

- a native node is **not** a Term under its governing explicit authoritative R/Type: Term Definition.
- source evidence binds two distinct complete canonical entity names to the same entity **or** one complete canonical entity name to two distinct entities, including synonymous full names registered in different qualified contexts.
- a native Relation Type has no defining source Claim under CA-R-1246, **or** an external reference violates its selected governing Entity Definition endpoint classes **or** graph contexts.
- a NARROWER_THAN Relation lacks an explicit authoritative source declaration **or** its governing Term definitions do **not** establish the implication under CA-R-1435. absence of Entity instances does **not** establish this implication.
- the NARROWER_THAN hierarchy **contains** a directed cycle, including a self-loop.
- a Root Term classification differs from the **`=0`** direct NARROWER_THAN-parent criterion under CA-R-1347.

the Evaluation **must** accept an acyclic hierarchy with multiple direct parents **or** an isolated Root Term **when** the remaining applicable authority is satisfied. A Relation Type's applicable Entity Definition constraints, when selected, **must not** change Root Term classification **when** the Terms Graph hierarchy is unchanged. the checks **must** distinguish an unknown Type from missing or unresolved governing constraint evidence without inventing a default or treating the known Type as unregistered.

for a governed-only view under CA-R-1454, the Evaluation **must** reject graph validity **if** a displayed native Term node lacks **`=1`** active dedicated Term Definition under CA-R-1319. missing **or** conflicting definitions **and** uncertain Relation or constraint evidence **must** be reported with their affected source references **without** inventing a definition **or** an edge.

filtering out a parent **must not** establish **or** change canonical Root Term classification. **if** the available source evidence is insufficient **to** establish the CA-R-1347 criterion, the classification **must** remain unresolved **without** silently importing source nodes **or** edges from outside the requested selection.

the same NARROWER_THAN implication check applies **when** the Terms name Actions **or** Workflows. those operational Atoms already are Entities; the Evaluation **must not** require **or** create separate Entity identities for them **or** infer a Terms Graph edge merely from their classification. an empty set of observed instances does **not** prove a hierarchy Relation; acceptance requires the governing Term definitions **and** explicit Relation authority.

### Projection fidelity and source traceability

an admitted source-Atom **or** cross-graph reference under CA-R-1472 **must not** fail **only** because its external endpoint is **not** a Term; that endpoint is **not** a native Terms Graph node. reject a view that imports that endpoint as a Term, erases its graph context, uses an unregistered Relation Type, **or** lets the external reference alter NARROWER_THAN hierarchy **or** Root Term classification.

for a governed-only view under CA-R-1454, the Evaluation **must** reject the view **if** an eligible Term **or** Relation required by CA-R-1454 is omitted, an ineligible node **or** edge is displayed, a displayed native Term node's Term Definition Atom **or** a displayed internal edge's source declaration is outside the requested source selection, a displayed native Term node **or** internal edge lacks exact source Claim **and** Artifact Revision traceability, **or** an internal Term Relation edge is inferred **only** from spelling, capitalization, shared Subject use, **or** compatible endpoints.

the Evaluation **must** reject a graph **or** governed-only view **if** its rendered content is treated as independent vocabulary authority, an upstream Projection substitutes for exact defining **or** Relation-source authority, a Projection chain loses its upstream identity **or** ultimate source traceability, **or** an arbitrary filter is treated as another admitted Projection Type. a source-faithful view derived through an upstream Terms Graph Projection **must** pass these Projection-specific checks **when** the applicable fidelity, selection **and** source-traceability requirements are satisfied; graph validity is assessed separately.

### Optional source-bound naming checks

the Evaluation **must** check complete canonical entity name-to-entity **and** entity-to-complete-name uniqueness using exact source-backed identity evidence. Repeated references to one established full-name binding are **not** duplicate entities. A valid one-to-one complete-name mapping satisfies only the naming check; the existing hierarchy, authority **and** reference checks still apply. Unknown identity, incomplete required entity-population **or** naming-source coverage, **or** ambiguous target binding **must** remain unresolved, **not** be accepted through spelling, graph position **or** qualification alone. The view **must** preserve **and** expose conflicting bindings with their source Claims **and** Revisions; silently merging entities **or** accepting alternate full names as synonyms fails fidelity. A faithful display of a naming collision **may** pass fidelity while the source graph fails naming validity. A known entity with zero complete canonical entity names under complete evidenced coverage fails missing naming; absence of a required active Definition is a separate defining-authority failure. The Evaluation **must not** invent an entity distinction, equivalence, full name **or** Term to produce a pass.

component Terms are reusable words **or** phrases whose meaning is owned by an explicit dedicated R/Type: Term Definition, **not** inferred from agreement between Semantics sections. They are **not** unique names for **every** entity **in** which they occur. Consistent use of `Package` in `Package`, `Eval Package` **and** `Runtime Package`, **and** `Unit` in `Scope Unit` **and** `Code Unit`, passes the component-meaning check. A different complete name identifies each separately defined entity. Conflicting component meanings fail; unknown component meaning **or** segmentation remains unresolved. No Unit entity **or** synthetic Term node is created merely by splitting an entity's name.

the complete-name check covers **every** named canonical Subject-graph entity: names in admitted `/`, `//`, `.`, `:`, **and** `>` constructs, existing-kind references `@(...)`, plus exact declared Relation Type names inside `((...))`. The reference marker refers to an existing kind **without** declaring another target; parsing alone admits no target **or** Relation. `Package > Module > Code Unit` connects three entities with three complete canonical names; name strings **and** the complete chain **must not** be introduced as additional entity nodes. Operators, delimiters **and** selector syntax are **not** Terms. Under CA-R-1325, a complete composite Subject Expression is **not** one lexical Term; parsing arbitrary composite syntax **does not** automatically establish a complete entity name **or** another entity. Explicitly source-admitted qualified property names such as `atom.id` **and** `projection.id` remain valid complete names. The three-target chain introduces no fourth entity **or** fourth complete name. Check **all** authored mentions against those full-name bindings: `component` used as a stylistic substitute for the same Module fails naming, while a separately defined Component entity remains distinct. Repeated references to the same entity are **not** collisions; distinct property, value **or** bearer-qualified entities using the same complete canonical name are collisions despite their context. A parsed Relation Type name **must not** become an admitted Relation **without** its governing authority **and** endpoint permissions. Preserve existing separation of source naming, native Terms Graph membership **and** Projection fidelity.

### Result boundary

the Evaluation **must** distinguish Projection fidelity from graph validity **and** keep the two outcomes visible, including **any** unresolved source conditions **and** checked-coverage limits. a graph that faithfully represents a source conflict **may** pass fidelity while failing an applicable graph-validity condition **or** leaving that condition unresolved. a composite acceptance result **must not** pass **if** an applicable check fails **or** remains unresolved; faithful reproduction alone does **not** establish a valid source model.

connectivity **and** cycle checks apply **only** as required by the governing graph authority; the NARROWER_THAN cycle prohibition **and** the admitted isolated Root Term cases above remain distinct. passing graph-structure checks does **not** establish Project-specific meaning **or** consistency of source use **without** the required governing definitions **and** source context.

## Details

Qualified property names `atom.id` **and** `projection.id` reuse the explicitly defined `id`; the dot remains syntax **and** the complete names remain distinct. Apply ID uniqueness **only** within matching prefixes; `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` introduce no version-identity **or** case-folding rules. Source consistency, well-formedness, checked coverage **and** optional Projection fidelity remain separate.

