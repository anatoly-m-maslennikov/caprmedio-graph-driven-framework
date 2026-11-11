---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/(.Type: Entities Graph)'
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Subjects
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_PROPERTY
  - CAPRMEDIO <+ MODEL <+ CFEL<+Operator//AllowedValue
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Term
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 39
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-1438@25
  - CA-R-2462
  - CA-R-1406
  - CA-R-1437
atom_id: CA-R-1456
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Derive Entities views from selected authority

## Claim scope

Entities Graph views for a requested source selection.

## Claim

a derived Entities Graph view **must** declare its requested source selection **and** **any** narrower display selection, including a hierarchy view. it **must** include **all** **and** **only** Entity identities admitted under CA-R-2462-CORE_META_MODEL-DEFINITION--define-entity by the selected source Claims that satisfy the declared display selection, **and** Relations explicitly declared by selected source Atoms whose endpoints are included, whose Relation Type has a defining source Claim, with any applicable Entity Definition constraints preserved, **and** that satisfy the declared display selection. a narrower view **must not** silently enlarge the source selection **or** be represented as the full combined graph. A declaration-only display selection excludes link instances. The presence of endpoints does not override that filter or require importing actual Relation tuples into the declaration view.

**every** displayed node **and** edge **must** retain its existing canonical identity **and** traceability **to** its exact governing source Claim **and** Artifact Revision for Entity **or** Relation admission; **any** represented observed structural **or** recorded historical facts additionally retain their appropriate Scope Unit **or** Journal sources under CA-R-2535-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form. Property occurrences retain their complete bearer-qualified Subject Paths under CA-R-1247-CORE_META_MODEL-CORE-REQUIREMENT--identify-dependent-entity-occurrences-by-complete-subject-path; reuse of a Term, appearance **in** multiple views, **or** multiple governing Atoms for one Entity **must not** duplicate **or** merge source identities. source Relation facts retain their Type identity, direction, qualified endpoints, **and** source declaration; derived HAS_PROPERTY navigation retains traceability **to** its original IS_PROPERTY_OF fact under the pending [HAS_PROPERTY Relation Definition](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md) **without** becoming another primitive Relation fact.

this selection reuses the Entities Graph under CA-R-1438@25-CORE_META_MODEL--define-entities-graph **without** another graph kind **or** independent model authority. a hierarchy display **must not** impose a tree constraint on the full graph, discard legitimate sharing, **or** introduce a global ordinal-position rule. display filtering **must not** change source bearer cardinalities, qualified identities, **or** allowed-value admission; IS_PROPERTY_OF **and** allowed-value qualifications retain their distinct governing authority.

the view **may** be derived from an upstream Entities Graph Projection **when** the upstream selection **and** source evidence support the requested view. the view **must** retain the upstream Projection identity **and** Revision together with traceability **to** the ultimate authoritative sources; the upstream Projection **must not** replace source authority **or** establish source completeness beyond its evidenced coverage. an observed Carrier **or** Journal occurrence alone **must not** admit an Entity identity, define a Term, **or** admit a Relation Type **without** the required governing source Claims. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Entities Graph Type and project-shared Relation Type definitions; any graph-specific admission or constraints remain governed by selected Entity Definition constraints where present; a display filter alone does **not** admit another Type or create a graph-specific Type copy.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472-CORE_META_MODEL--admit-typed-secondary-graph-connections, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their endpoint identity, Relation Type identity, any applicable governing constraint context and its established endpoint classes, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.

## Details

### Pending relation authorities

The operative IS_PROPERTY_OF and HAS_PROPERTY view rules depend on the pending [IS_PROPERTY_OF Relation Definition](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of.md), [HAS_PROPERTY Relation Definition](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md), and [Property kind and Formal Constraint](CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md). These Draft links are pending dependencies, not Current admission.

CA-R-1260@34-CORE_META_MODEL-DEFINITION--define-is-borne-by and CA-R-1243@27-CORE_META_MODEL-RULE--derive-bears-as-the-inverse-of-is-borne-by remain historical provenance for the superseded names only; neither authorizes IS_PROPERTY_OF or HAS_PROPERTY.

### Readable tree view

The full structural Entities Graph view **must** present the Inherency tree:

**Inherency tree:** use NARROWER_THAN, INSTANCE_OF and IS_PROPERTY_OF Relations, and show source-backed allowed-value qualifications as value annotations rather than graph Relations. Show a selected explicitly named instance under its kind using `//`, retaining the instance's existing identity; INSTANCE_OF is directed from instance to kind and is distinct from narrower-kind classification. The name is not automatically a Term. First show the primary-entity tree without Properties. Then show one detail tree for each primary entity with one or more Properties, including its Properties and further Properties. Show every source-backed allowed value as an annotation beneath the Entity to which its qualification applies, including a non-Property target; preserve that target's identity, do not reclassify it as a Property, and do not create a graph Node or Relation for the literal value. Detail sections follow the primary entities' first-appearance order in the main tree.

An entity with multiple broader parents **must** appear under every applicable parent, with the same identity at every placement. Its Property detail section appears once at its first-appearance position. The view **must** preserve relation meaning and any declared cardinality; repeated display does not create another entity.

The Inherency view **must** be generated programmatically. Use declared sibling order when available; otherwise use alphabetical order. Keep shared identities, dependent qualification and the declared source selection. This is a readable view of the graph, not a replacement for the source model or a claim that the entire graph is a tree.

### Structural and middle-level declaration views

The full structural view shows the selected model's primary entities, dependent properties, allowed values and admitted structural Relations. It is not a catalogue of every actual Atom, Actor, Execution or other project instance. A named instance explicitly selected by a source Subject may appear under its kind; do not enumerate unselected instances or turn instance names into new kinds. Keep Core Meta-model and Project Configuration source selections separate. Report unsupported or unmapped source material as unresolved coverage, not as admitted facts or proof that it does not exist.

The declaration view is a separately identified filtered view of the same Entities Graph Type. It selects the middle level: named Relation Types with their declared descriptive metadata, with their existing defining authority. It does not select actual source-type-target links instantiating those Types. Do not use an Atom's frontmatter relations map as this declaration catalogue.

Identify a Relation Type by its project-unique canonical name and defining source Claim. Retain its meaning and any explicitly declared direct direction, inverse, derivation, or transitivity semantics. Any selected governing constraint admission, endpoint permissions, endpoint graph contexts, cardinality and other constraints remain in those Entity Definitions under CA-R-1246 and CA-R-806; this definition introduces no new per-Type Rule or default. Do not invent missing metadata, treat a bare Subject as an already resolved qualified alias, or create graph-specific copies of an equal Type name.

Constraints belong to the governing Entity Definitions. The selected Relation Type declaration view contains named Type definitions, not a separate Graph Rule instance catalogue or actual endpoint tuples.

Both views retain exact governing source Claim and Revision evidence. Missing or ambiguous identity, metadata, schema or coverage stays visible as a limitation. Neither view admits new source facts, changes source Relation identity/storage, evaluates rules or claims unsupported semantic completeness.

Preserve declared containment in the model tree using `Part +> Whole` or `Whole <+ Part` and `@` references to already declared Entities, without propagating Properties through containment. Preserve each independent pre-token Source count and post-token Target reverse count; an omitted count stays unspecified.
