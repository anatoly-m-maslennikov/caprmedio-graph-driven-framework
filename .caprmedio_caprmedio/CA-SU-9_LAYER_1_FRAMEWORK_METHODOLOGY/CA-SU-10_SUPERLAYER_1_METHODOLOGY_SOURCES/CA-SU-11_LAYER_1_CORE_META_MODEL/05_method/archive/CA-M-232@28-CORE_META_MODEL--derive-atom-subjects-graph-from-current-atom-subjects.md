---
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Entity Graph'
  depends_on:
  - 'Entity/Object/Continuant/Projection/Type: Atom Entitys Graph'
  - Entity/Object/Continuant/Governing Objects/Atom.Entitys
  - Entity
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
version: 28
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-M-232@28
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Implementation Method
---
## Summary

Derive Atom Entitys Graph from Current Atom Entitys

## Claim scope

Atom Entitys Graph derivation from current Atom Entitys.

## Claim

**to** derive an Atom Entitys Graph, the Generator **must** reproduce **every** selected Entity as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical Entity Target, Entity Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Entitys, **or** creating a separately identified Entity object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Entitys metadata. an Atom Entitys Graph may include Entity-root and Method-root Entity Targets. an Entities Graph view must include only Entity-root targets unless its own Spec explicitly admits a distinguishable external reference. Render Package/Project Implementation as the parentless root Package, every Module as belonging to exactly one Package, and nested Packages as belonging to another Package. An unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details

For the readable Entity Graph hierarchy under CA-R-2150:

1. Compose the selected Current source Entity paths mechanically. Preserve source spelling and provenance; do not invent Entitys from filenames, module names or Scope Unit names.
2. Render primary kinds first. Omit INSTANCE_OF paths and all their descendants from this first section. Dependent properties and their values appear in the second section, not the first tree.
3. In primary-tree order, render each primary with direct or inherited properties. Follow broader-to-narrower kind ancestry only for this inheritance; structural containment (`>`) and Depends On do not imply it. Show inherited origins explicitly. Combine source-backed allowed-value additions without removing inherited values. Preserve equal-name origins and report conflicts rather than choosing an override.
4. Render named instances separately. Reuse selected named Entity instances, selected source-backed Relation Type declarations, and Current Requirement/Type Graph Rule declarations with their actual YAML `claim.*` mappings. Defining schemas and examples are not concrete Graph Rules. Do not substitute actual Atom-to-Atom Relation tuples for the requested Relation Type instances.
5. Use tabs for tree depth and local labels without repeated full paths. Preserve declared sibling order, otherwise use alphabetical order. Keep source limitations visible and retain the complete Current Atom ID/Version provenance.

Render specialization with `/`, named instances with `//`, dependents with `.`, allowed values with `:`, and structural containment with `>`. These are distinct meanings, not interchangeable indentation edges. Shortened labels and repeated occurrences preserve canonical target identity and source-backed constraints. Do not infer a changed containment requirement solely because filtering hides a standalone label. Exact optional/mandatory display and alternative-path rules remain pending in CA-A-1236.

### Containment alternatives

In the complete declared containment structure, each branch is an allowed option. `X > Y` requires a contained Y instance to belong to exactly one immediate whole instance of the permitted kind. Alternative container branches are choices, not simultaneous ownership obligations. An independent declaration can permit an uncontained instance; an existing-kind reference does not grant that permission. Part-to-whole cardinality is one; the number of Y parts per X remains separately constrained. CA-A-1253 records this latest cardinality decision. Every Module belongs to exactly one Package; Package/Project Implementation is the parentless root Package, and nested Packages belong to another Package.

In the governing declaration structure, an independent kind declaration outside structural containment permits that kind without that structural parent. An existing-kind reference `@(...)` does not make another independent declaration. Every Module belongs to exactly one Package; Step belongs to Workflow. A standalone source file is a Module of the root Package, not an independently declared Module. A derived display preserves these source meanings even when its selection omits a declaration or reference. This resolves Q02 in CA-A-1236; repeated display labels alone carry no new permission.
Render these alternatives from their governing source meaning, not from the number of repeated labels in a selected view.

### Existing-target reference marker

Render the `@` existing-kind modifier separately from the base edge meaning for `/@` and `>@`. Preserve the referenced target's canonical identity and its defining-source provenance rather than duplicating its definition. Do not remove or add containment requirements from the marker alone.

### Reference boundary

Use `@(...)` for an existing-kind reference after `/` or `>`, with a unique primary-kind name or its current canonical path. Keep the matching closing parenthesis before any outer continuation. For example, the explanatory `Entity/Object/Continuant/@(Scope Unit).ID` references Scope Unit first, then addresses its ID property. Full ordinary Entity spelling remains in sources; a unique primary-kind name is now an admitted @ reference payload, not merely a shortened display.

### Canonical path changes

When a kind's canonical declaration path changes, migrate affected Current ordinary Entity paths and full-path references; @ references using an unchanged unique primary-kind name remain valid. A primary-kind rename requires migrating its name-based references as well. Keep no old-path aliases or alias registry for now. Preserve the distinction between Current reference maintenance and unchanged archived historical evidence; this Draft does not perform a migration.

### Confirmed independent and contained kinds

Require Module containment by Package and Step containment by Workflow. A source file directly under the implementation root belongs to its root Package. Keep Step and Substep distinct. Scope Unit >@(Scope Unit), >@(Atom) and >@(Projection) are structural part links. These are abbreviated displays; the current full-reference spelling rule remains in force pending Q07.

### Unique primary-kind names

Distinct primary-kind declarations have unique names across the effective Entity model, not only the selected projection. Repeated references to the same kind do not declare duplicates. Properties may reuse names under different bearers. `@(Module)` is therefore an admitted existing-kind reference. A branch move preserves name-based references when the primary-kind name is unchanged; a rename requires their migration. Keep no aliases. This naming rule does not automatically rename conflicting Current kinds or waive the full structure of ordinary Entity paths.

### General named-relation notation

Render an admitted cross-link without a short operator as `Source ((RELATION_TYPE)) Target`. Use the source-declared type, direction and endpoints. A requested opposite view uses the declared derived inverse name, without persisting a duplicate inverse fact or multiplying counts. An unsupported type stays unresolved; do not fabricate its definition or infer extra inheritance from a generic named edge. The readable notation does not create a native relation from an illustrative example. See CA-A-1240.
