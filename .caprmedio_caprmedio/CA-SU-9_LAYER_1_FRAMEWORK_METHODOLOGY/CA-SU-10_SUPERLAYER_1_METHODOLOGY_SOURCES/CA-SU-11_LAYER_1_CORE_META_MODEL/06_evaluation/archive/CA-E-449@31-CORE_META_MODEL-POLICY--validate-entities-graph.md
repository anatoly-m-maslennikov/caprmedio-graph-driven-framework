---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Entities Graph'
  depends_on:
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Term
  - 'Subject/Graph/Relation/Type: IS_BORNE_BY'
  - 'Subject/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
  - Subject/Graph/Relation
  - Subject/Graph/Relation/Type
  - Subject
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
version: 31
updated_at: 2026-10-25 03:48:37 +0400
relations:
  evaluation_for:
  - CA-R-2003
  - CA-R-2100
  - CA-R-1243
  - CA-R-1246
  - CA-R-1247
  - CA-R-1248
  - CA-R-1260
  - CA-R-1346
  - CA-R-1351
  - CA-R-1406
  - CA-R-1436
  - CA-R-1438
  - CA-R-1456
atom_id: CA-E-449@31
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 4
---
# Summary
Validate Entities Graph

## Scope
Entities Graphs **and** selected views, including source selection, display selection, **and** governing source constraints.

## Claim

the Evaluation **must** reject an Entities Graph **if** **any** of:

- a node is **not** an Entity under its governing authority, **or** a separate Entity identity is invented for an existing Action **or** Workflow Atom.
- a selected view includes a node **or** source Relation that fails its declared source selection **or** fails its declared display selection, omits an eligible node **or** source Relation under CA-R-1456-CORE_META_MODEL-GENERAL-REQUIREMENT--derive-entities-views-from-selected-authority, **or** silently imports outside authority **to** complete the view.
- a displayed node **or** edge lacks its exact governing source Claim **or** Artifact Revision for Entity **or** Relation admission, **or** a represented observed structural **or** recorded historical fact lacks its appropriate Scope Unit **or** Journal source under CA-R-1746-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form; derived inverse navigation lacks traceability **to** the original source Relation.
- display membership, repeated appearance, a reusable Term, **or** a shortened path substitutes for the existing canonical Entity identity **or** complete bearer-qualified Subject Path.
- multiple governing Atoms are treated as multiple identities for one Entity, **or** the at-most-one GOVERNS target per Atom is treated as permitting **only** one governing Atom per Entity.
- a tree display is treated as the full combined graph **without** satisfying its declared selection, **or** legitimate sharing is rejected, duplicated, **or** discarded **to** force a tree.
- a Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246-CORE_META_MODEL-RULE--keep-relation-vocabularies-graph-specific.
- an IS_BORNE_BY Relation has an invalid endpoint **or** direction under CA-R-1260-CORE_META_MODEL-DEFINITION--define-is-borne-by, **or** violates the applicable immediate-bearer cardinality under CA-R-2003-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence **or** CA-R-1351-CORE_META_MODEL-CORE-REQUIREMENT--give-primary-entity-occurrences-no-bearer.
- an IS_ALLOWED_VALUE_OF Relation admits a value **without** governing authority for its qualified Property context under CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of.
- admission **in** one Property context is used **to** justify admission **in** another context **without** its applicable authority.
- allowed-value admission is treated as assigning a value **to** a particular Property occurrence **or** determining that Property's cardinality.
- BEARS is independently authored as another primitive Relation Kind instead of being derived from IS_BORNE_BY under CA-R-1243-CORE_META_MODEL-RULE--derive-bears-as-the-inverse-of-is-borne-by.

the Evaluation **must not** reject the reuse of one Term as an allowed-value name **in** multiple qualified Property contexts **when** the value is separately admitted **in** **every** such context. the checks **must** cover valid **and** invalid bearer endpoints, applicable bearer cardinalities, independent value admission across Property contexts, derived inverse navigation, **and** a Relation Kind imported from another graph kind.

native endpoint **and** cardinality checks use the cited governing source facts; a filtered view does **not** establish absence of a bearer, change a qualified identity, **or** alter allowed-value admission. **if** selected evidence cannot establish an applicable source constraint, the Evaluation **must** retain the source-backed limitation as unresolved **without** inventing an edge **or** silently enlarging selection. a truthful limited view does **not** prove that the unexamined source model passes its checks.

the checks **must** also cover exact selected-source node **and** edge provenance, eligible omissions **and** outside-selection additions, repeated appearances of one identity, distinct qualified occurrences sharing a reusable Term, multiple governing Atoms for one Entity, Action **and** Workflow Atoms admitted under their existing Atom identities **when** selected, rejection of duplicate identities **and** type-only exclusion, a legitimate shared value admitted independently **in** two Property contexts, **and** explicit hierarchy filtering **without** a universal-tree assumption.

the Evaluation **must** reject a graph **or** filtered view **if**

- its rendered content is treated as independent model authority,
- a graph specification is used **to** grant source authority **to** its derived contents,
- an upstream Projection substitutes for the appropriate source facts,
- an observed Carrier **or** Journal occurrence is used **to** admit an Entity identity, define a Term, **or** admit a Relation Kind **without** the required governing source Claims,
- a Projection chain loses upstream identity **or** ultimate source traceability,
- **or** an arbitrary display filter is treated as another admitted Projection Type.

a source-faithful view derived through an upstream Entities Graph Projection **must** pass these Projection-specific checks **when** the remaining applicable source, display-selection **and** graph constraints pass.

## Details

### Readable tree-view acceptance

For the readable view specified by CA-R-1456 and delivered under CA-D-634, check that:

- the output is a Markdown file with YAML frontmatter identifying Projection form, Entities Graph Type, completed rebuild time and every contributing source Atom as ID plus Version;
- the Inherency view uses only its selected NARROWER_THAN, IS_BORNE_BY and IS_ALLOWED_VALUE_OF relations;
- the main Inherency tree excludes dependent entities; each primary entity with dependents has exactly one detail section, in first-appearance order, including qualified properties and their allowed values;
- a shared entity appears under every applicable parent without creating new identities or repeated detail sections;
- declared sibling order is preserved; unordered siblings are alphabetical with deterministic ties; tree indentation uses literal tabs in fenced text blocks, while YAML uses spaces;
- repeated generation from the same sources produces the same tree body and source list; updated_at records the actual completed rebuild;
- missing source facts and cycles are reported without invented facts or endless expansion.

These checks exercise the generator with controlled inputs. They do not add an unrelated whole-project Atom-validation gate.

### Structural and declaration-view acceptance

Use controlled runtime inputs to check the full structural view and the separately selected middle-level declaration view under CA-R-1456 and CA-D-634:

- The full structural view preserves eligible source-backed primary entities, properties, allowed values and structural Relations. Unmapped or unsupported material remains visible as unresolved coverage, not falsely admitted or silently removed to force a target tree.
- The declaration view includes the selected named Relation Types and concrete formal Graph Rule declarations, not actual Atom-to-Atom links. Inputs containing such links, illustrative YAML, generic Rule prose or model definitions must not turn them into selected declarations.
- A Relation Type keeps its graph kind and canonical name, descriptive metadata, declared direct/inverse direction and exact source provenance. Repeated references do not duplicate its identity; equal names in different graph kinds stay distinct. Missing, ambiguous or conflicting metadata remains unresolved, without an invented value or winner. Graph Rule permissions and cardinality are not copied into descriptive Type metadata.
- Each included formal Rule retains its source Atom identity/Version, governed Subject, Summary and operative YAML. Opaque values are preserved; unsupported forms or references remain explicit gaps. The generator does not evaluate conditions, apply defaults, merge rules or create instances.
- An empty Rule catalogue passes when the selected inputs contain no concrete formal Rule declarations. This neither requires live Rule creation nor proves completeness beyond the declared selection.
- Core and Project source boundaries remain separate. Source selection, display selection and ultimate source evidence stay explicit, including on partial results.
- Rebuilding the same Type, named selection and source of truth keeps its Projection ID and deterministic body/source list. A genuinely different selection keeps a distinct Projection identity under CA-R-1943. Check actual rebuild time, Markdown/YAML fields, alphabetical ordering where no order is declared, literal tabs in text trees and spaces in YAML.

These are generator tests with controlled inputs, not a whole-project Atom-health gate. They add no rule evaluator, source admission policy or construction/CONTAINS implementation.

Construction/CONTAINS projection is deferred to the adjacent `draft/` RMED. It is not required by this active readable-view specification.
