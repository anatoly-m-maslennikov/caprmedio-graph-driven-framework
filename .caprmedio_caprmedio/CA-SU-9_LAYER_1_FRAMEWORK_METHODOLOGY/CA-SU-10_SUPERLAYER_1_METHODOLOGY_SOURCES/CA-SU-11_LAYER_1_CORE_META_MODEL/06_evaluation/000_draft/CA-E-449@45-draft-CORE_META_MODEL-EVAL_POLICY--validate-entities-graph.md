---
atom_id: CA-E-449
ref_id: CA-E-449@45-draft
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Entities Graph)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Node.**
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_PROPERTY
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role: Operations)/(.Header.Context.Form: Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role: Operations)/(.Header.Context.Form: Workflow)'
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
tier: 4
relations:
  evaluation_for:
  - CA-R-2003
  - CA-R-2100
  - CA-R-1246
  - CA-R-1247
  - CA-R-2462
  - CA-R-1346
  - CA-R-1351
  - CA-R-1406
  - CA-R-1245
  - CA-R-1438@25
  - CA-R-1456
status: Draft
version: 45
updated_at: 2026-11-04 18:25:15 +0400
carrier_destination:
  file:
    name: CA-E-449@45-draft-EVAL_POLICY--validate-entities-graph.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/000_draft
---
## Summary
Validate Entities Graph

## Claim

### Prose Claim

Entities Graphs **and** selected views, including source selection, display selection, **and** governing source constraints.


the Evaluation **must** reject an Entities Graph **if** **any** of:

- a node is **not** an Entity under its governing authority, **or** a separate Entity identity is invented for an existing Action **or** Workflow Atom.
- a selected view includes a node **or** source Relation that fails its declared source selection **or** fails its declared display selection, omits an eligible node **or** source Relation under CA-R-1456-CORE_META_MODEL-GENERAL-REQUIREMENT--derive-entities-views-from-selected-authority, **or** silently imports outside authority **to** complete the view.
- a displayed node **or** edge lacks its exact governing source Claim **or** Artifact Revision for Entity **or** Relation admission, **or** a represented observed structural **or** recorded historical fact lacks its appropriate Scope Unit **or** Journal source under CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form; derived inverse navigation lacks traceability **to** the original source Relation.
- display membership, repeated appearance, a reusable Term, **or** a shortened path substitutes for the existing canonical Entity identity **or** complete bearer-qualified Subject Path.
- multiple governing Atoms are treated as multiple identities for one Entity, **or** the at-most-one GOVERNS target per Atom is treated as permitting **only** one governing Atom per Entity.
- a tree display is treated as the full combined graph **without** satisfying its declared selection, **or** legitimate sharing is rejected, duplicated, **or** discarded **to** force a tree.
- a Relation Type is unknown under CA-R-1246-CORE_META_MODEL-RULE--keep-relation-vocabularies-graph-specific.
- an IS_PROPERTY_OF Relation has an invalid endpoint **or** direction under current CA-R-2473, or violates the applicable Node/Node.** endpoint and cardinality constraints in CA-R-2462 **or** the no-outgoing-bearer rule for primary Entity occurrences in CA-R-1351.
- the direct IS_PROPERTY_OF Relations contain a directed cycle, including a self-loop, contrary to the acyclicity constraint in current CA-R-2473.
- an allowed-value qualification admits a value **without** governing authority for its qualified target Entity context under CA-R-1245-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.
- admission **in** one target Entity context is used **to** justify admission **in** another context **without** its applicable authority.
- allowed-value admission is treated as assigning a value **to** a particular occurrence **or** determining direct-value cardinality.
- HAS_PROPERTY is independently authored as another primitive Relation Type instead of being derived as the inverse of IS_PROPERTY_OF under current CA-R-2473 and CA-R-2621.

the Evaluation **must not** reject the reuse of one Term as an allowed-value name **in** multiple qualified target Entity contexts **when** the value is separately admitted **in** **every** such context. the checks **must** cover valid **and** invalid bearer endpoints, applicable bearer cardinalities, independent value admission across target Entity contexts, derived inverse navigation, **and** a Relation Type used under another governing constraint context.

native endpoint **and** cardinality checks use the cited governing source facts; a filtered view does **not** establish absence of a bearer, change a qualified identity, **or** alter allowed-value admission. **if** selected evidence cannot establish an applicable source constraint, the Evaluation **must** retain the source-backed limitation as unresolved **without** inventing an edge **or** silently enlarging selection. a truthful limited view does **not** prove that the unexamined source model passes its checks.

the checks **must** also cover exact selected-source node **and** edge provenance, eligible omissions **and** outside-selection additions, repeated appearances of one identity, distinct qualified occurrences sharing a reusable Term, multiple governing Atoms for one Entity, Action **and** Workflow Atoms admitted under their existing Atom identities **when** selected, rejection of duplicate identities **and** type-only exclusion, a legitimate shared value admitted independently **in** two target Entity contexts, **and** explicit hierarchy filtering **without** a universal-tree assumption.

the Evaluation **must** reject a graph **or** filtered view **if**

- its rendered content is treated as independent model authority,
- a graph specification is used **to** grant source authority **to** its derived contents,
- an upstream Projection substitutes for the appropriate source facts,
- an observed Carrier **or** Journal occurrence is used **to** admit an Entity identity, define a Term, **or** admit a Relation Type **without** the required governing source Claims,
- a Projection chain loses upstream identity **or** ultimate source traceability,
- **or** an arbitrary display filter is treated as another admitted Projection Type.

a source-faithful view derived through an upstream Entities Graph Projection **must** pass these Projection-specific checks **when** the remaining applicable source, display-selection **and** graph constraints pass.

## Details

### Allowed-value target cases

Include a source-admitted allowed-value expression whose target is not a Property, alongside the Property cases. Its target kind alone must not cause rejection. Each value still requires authority in its own qualified target Entity context; neither case assigns a value to an occurrence or determines direct-value cardinality.

### Property bearer-cycle checks

With the remaining applicable constraints satisfied, accept a Property borne
by a primary Entity and an acyclic nested Property chain. Reject a Property
borne by itself, two Properties borne by each other, and a longer directed
IS_PROPERTY_OF cycle. Repeated display of one Property is not a new node or
a cycle by itself. This constraint does not reject cycles made only from
value references or other Relation Types. Missing source facts remain an
unresolved limitation; they do not prove either a cycle or acyclicity.

### Readable tree-view acceptance

For the readable view specified by CA-R-1456 and delivered under CA-D-634, check that:

- the output is a Markdown file with YAML frontmatter identifying Projection form, Entities Graph Type, completed rebuild time and every contributing source Atom as ID plus Version;
- the Inherency view uses its selected NARROWER_THAN and IS_PROPERTY_OF Relations and source-backed allowed-value qualifications as value annotations, not graph Relations;
- the main Inherency tree excludes Properties; each primary entity with Properties has exactly one detail section, in first-appearance order, including qualified properties and their allowed values;
- a shared entity appears under every applicable parent without creating new identities or repeated detail sections;
- declared sibling order is preserved; unordered siblings are alphabetical with deterministic ties; tree indentation uses literal tabs in fenced text blocks, while YAML uses spaces;
- repeated generation from the same sources produces the same tree body and source list; updated_at records the actual completed rebuild;
- missing source facts and cycles are reported without invented facts or endless expansion.

These checks exercise the generator with controlled inputs. They do not add an unrelated whole-project Atom-validation gate.

### Structural and declaration-view acceptance

Use controlled runtime inputs to check the full structural view and the separately selected middle-level declaration view under CA-R-1456 and CA-D-634:

- The full structural view preserves eligible source-backed primary entities, properties, allowed values and structural Relations. Unmapped or unsupported material remains visible as unresolved coverage, not falsely admitted or silently removed to force a target tree.
- The declaration view includes selected named Relation Type definitions, not actual Atom-to-Atom links, Workflow instances or a separate Graph Rule catalogue. Model constraints remain in their Entity Definitions.
- A Relation Type keeps its project-unique canonical name, meaning and exact source provenance, plus any declared direct/inverse/derivation/transitivity semantics. Repeated references do not duplicate its identity; shared names resolve to one defining Claim. Missing, ambiguous or conflicting Type definitions remain unresolved, without an invented value or winner. Any applicable governing constraint admission, endpoint permissions and cardinality are not copied into descriptive Type metadata.
- Each included formal Rule retains its source Atom identity/Version, governed Subject, Summary and operative YAML. Opaque values are preserved; unsupported forms or references remain explicit gaps. The generator does not evaluate conditions, apply defaults, merge rules or create instances.
- An empty Rule catalogue passes when the selected inputs contain no concrete formal Rule declarations. This neither requires live Rule creation nor proves completeness beyond the declared selection.
- Core and Project source boundaries remain separate. Source selection, display selection and ultimate source evidence stay explicit, including on partial results.
- Rebuilding the same Type, named selection and source of truth keeps its Projection ID and deterministic body/source list. A genuinely different selection keeps a distinct Projection identity under CA-R-1943. Check actual rebuild time, Markdown/YAML fields, alphabetical ordering where no order is declared, literal tabs in text trees and spaces in YAML.

These are generator tests with controlled inputs, not a whole-project Atom-health gate. They add no rule evaluator, source admission policy or construction/CONTAINS implementation.

Construction/CONTAINS projection is deferred to the adjacent `draft/` RMED. It is not required by this active readable-view specification.
