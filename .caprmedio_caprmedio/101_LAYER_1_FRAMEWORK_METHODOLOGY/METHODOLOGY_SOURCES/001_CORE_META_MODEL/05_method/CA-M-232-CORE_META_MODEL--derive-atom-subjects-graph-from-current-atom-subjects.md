---
subjects:
  active: 'Entity/Object/Continuant/Projection/(.Type: Subject Graph)'
  passive:
  - 'Entity/Object/Continuant/Projection/(.Type: Atom Subjects Graph)'
  - Atom.Subjects
  - Entity
  - Atom
  - CFEL <+ Relation//GOVERNS
  - CFEL <+ Relation//DEPENDS_ON
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-M-232
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Method
form: Implementation Method
---
## Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Claim scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Entity as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical Entity Target, Entity Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Entity object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. The Subject graph composes selected Entity-root targets according to the governing Entity Definition in CA-R-2462, including the proposed Term and Property branches. Render Package/Project Implementation as the parentless root Package, every Module as belonging to exactly one Package, and nested Packages as belonging to another Package. An unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details

For the readable Entity Graph hierarchy under CA-R-2150@15:

1. Compose the selected Current source Entity paths mechanically. Preserve source spelling and provenance; do not invent Subjects from filenames, module names or Scope Unit names.
2. Render primary kinds first. Omit INSTANCE_OF paths and all their descendants from this first section. Properties and admitted allowed-value branches appear in the second section, under their actual target Entity, not the first tree. An allowed-value target need not be a Property.
3. In primary-tree order, render each selected Entity with direct or inherited Properties and source-backed allowed values. Follow broader-to-narrower kind ancestry only for this inheritance; structural containment (`+>` or `<+`) and Depends On do not imply it. Show inherited origins explicitly. Combine source-backed allowed-value additions without removing inherited values. Preserve equal-name origins and report conflicts rather than choosing an override.
4. Render the selected named Relation Type instances separately from the primary-kind and property views. Use their governing R/Relation Definition sources; do not enumerate actual endpoint tuples or a retired Graph Rule catalogue. Constraints remain in their governing Entity Definitions.

5. Use tabs for tree depth and local labels without repeated full paths. Preserve declared sibling order, otherwise use alphabetical order. Keep source limitations visible and retain the complete Current Atom ID/Version provenance.

Render specialization with `/`, named instances with `//`, Properties with `.`, allowed values of any target Entity with `:`, and structural containment as `Part +> Whole` or `Whole <+ Part`. Render classification-axis applicability with `>|` or `|<`; its endpoint is an Entity serving the Classification role, not a separate Classification kind, and IS_CLASSIFIED_BY membership remains a different Relation. These are distinct meanings, not interchangeable indentation edges. Shortened labels and repeated occurrences preserve canonical target identity and source-backed constraints. Do not infer a changed containment requirement solely because filtering hides a standalone label. Exact optional/mandatory display and alternative-path rules remain pending in CA-A-1236.

### Containment alternatives

In the complete declared containment structure, each branch is an allowed option. `X <+ Y` requires a contained Y instance to belong to exactly one immediate whole instance of the permitted kind. Alternative container branches are choices, not simultaneous ownership obligations. An independent declaration can permit an uncontained instance; an existing-kind reference does not grant that permission. Part-to-whole cardinality is one; the number of Y parts per X remains separately constrained. CA-A-1253 records this latest cardinality decision. Every Module belongs to exactly one Package; Package/Project Implementation is the parentless root Package, and nested Packages belong to another Package.

In the governing declaration structure, an independent kind declaration outside structural containment permits that kind without that structural parent. An existing-kind reference `@(...)` does not make another independent declaration. Every Module belongs to exactly one Package; Step belongs to Workflow. A standalone source file is a Module of the root Package, not an independently declared Module. A derived display preserves these source meanings even when its selection omits a declaration or reference. This resolves Q02 in CA-A-1236; repeated display labels alone carry no new permission.
Render these alternatives from their governing source meaning, not from the number of repeated labels in a selected view.

### Existing-target reference marker

Render the `@` call to an already declared Entity separately from the base edge meaning, including when it follows `/` or `<+`. Preserve the referenced target's canonical identity and its defining-source provenance rather than duplicating its definition. Do not remove or add containment requirements from the marker alone.

### Reference boundary

Use `@` to call an already declared Entity. Parentheses provide logical grouping and delimit the intended expression before any outer continuation. A unique primary-kind name or its current canonical path remains an admitted payload for a reference to that kind. For example, the explanatory `Entity/Object/Continuant/@(Scope Unit).ID` calls Scope Unit first, then addresses its ID Property. Full ordinary Entity spelling remains in sources; a call does not declare another Entity or introduce a full-name alias.

### Canonical path changes

When a kind's canonical declaration path changes, migrate affected Current ordinary Entity paths and full-path references; @ references using an unchanged unique primary-kind name remain valid. A primary-kind rename requires migrating its name-based references as well. Keep no old-path aliases or alias registry for now. Preserve the distinction between Current reference maintenance and unchanged archived historical evidence; this Draft does not perform a migration.

### Confirmed independent and contained kinds

Require Module containment by Package and Step containment by Workflow. A source file directly under the implementation root belongs to its root Package. Keep Step and Substep distinct. Scope Unit <+@(Scope Unit), <+@(Atom) and <+@(Projection) are structural part links. These are abbreviated displays; the current full-reference spelling rule remains in force pending Q07.

### Unique primary-kind names

Distinct primary-kind declarations have unique names across the effective Entity model, not only the selected projection. Repeated references to the same kind do not declare duplicates. Properties may reuse names under different bearers. `@(Module)` is therefore an admitted existing-kind reference. A branch move preserves name-based references when the primary-kind name is unchanged; a rename requires their migration. Keep no aliases. This naming rule does not automatically rename conflicting Current kinds or waive the full structure of ordinary Entity paths.

### General named-relation notation

Render an admitted cross-link without a short operator as `Source ((RELATION_TYPE)) Target`. Use the source-declared type, direction and endpoints. A requested opposite view uses the declared derived inverse name, without persisting a duplicate inverse fact or multiplying counts. An unsupported type stays unresolved; do not fabricate its definition or infer extra inheritance from a generic named edge. The readable notation does not create a native relation from an illustrative example. See CA-A-1240.

The Property Relation view uses direct IS_PROPERTY_OF from Property to immediate bearer, and derived HAS_PROPERTY in the opposite display direction. It does not persist a second reverse fact or multiply the number of actual Relations. The direct Relation is binary. In `Source {forward-count}RELATION{reverse-count} Target`, the count before the Relation token constrains links per written Source and the count after it constrains reverse links per written Target; reversing the written direction swaps these positions. An omitted side remains unspecified. `Property {1}((IS_PROPERTY_OF)) Bearer` constrains exactly one outgoing bearer link per Property and leaves the reverse count unspecified. These counts concern Relation instances, not arity or direct Property values; direct values retain `Property[format]{count}`.

### Current source pin and pending adoption

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/CA-M-232-CORE_META_MODEL--derive-atom-subjects-graph-from-current-atom-subjects.md`, Version 31, SHA-256 `a91f896c0bd3f79a90ace9abc800a691e603847095b48638eaccdc9e0cae743e`. Current bytes remain unchanged. The new Relation names depend on the pending IS_PROPERTY_OF / HAS_PROPERTY Relation Definition Drafts; this source does not admit them through a renamed token alone. This preparation performs no runtime change, generated-view refresh or promotion.
