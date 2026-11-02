---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
version: 21
updated_at: 2026-10-31 19:27:10 +0400
relations: {}
atom_id: CA-R-1484@21-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 2
form: Rule
---
## Summary

Establish Scope Units through Project Structure declarations

## Claim scope

Scope Unit Declarations for each specific Scope Unit, including the root Project Scope Unit.

## Claim

**every** specific Scope Unit, including the root Project Scope Unit, **must** have exactly one external Requirement Atom using Form `Scope Unit Declaration` that declares that Scope Unit. The Declaration is external to the declared Scope Unit.

Every declared Scope Unit **must** have one or more separate external Goal Atoms outside the declared Scope Unit. Goal content is not copied into the Declaration; existing ordinary Goal parent-owner/child-target and Project Goal Operator-owner conventions remain unchanged.

A Scope Unit **may** have local Tier 0 Contract Atoms inside the Scope Unit, plural, for applicable RMEDO roles. This Draft adds no exact-one, minimum-count, or all-five-role requirement for those Contracts.

The external Declaration may supply the Scope Unit's ID, unique Name, Type (ordered or unordered), Label, applicable Local Order, existing connections, and existing authority/Implementation Folder carrier bindings. A non-root Scope Unit has a direct Parent; the root Project has none. Project Settings supplies the root identity until an authorized source migration; do not invent a duplicate child row, root Label, order or Carrier bindings. The Declaration establishes the unit independently of Goal coverage and Carrier materialization; these remain separately evaluated conditions.

The Declaration may include optional external Scope Constraints. “External” is relative to the governed Scope Unit; this does not create a new Scope or entity.

The Declaration plus local Contracts are sufficient; no additional Definition Atom is required for each actual Scope Unit. Generic shared structure belongs in the reusable Declaration model or template.

The external Declaration is the single authority for its declared structural and carrier-binding values. Name/Order Atoms and concrete binding Atoms **must not** be maintained as independent authorities for the same values.

No Scope Unit Navigation Number requirement is carried forward. This Draft adds no replacement numbering, format, cardinality, or default rule.

External Scope Unit Declarations replace `project_structure.toml` as the permanent governing source once separately authorized. Any compatibility TOML used during a separately authorized cutover is derived and not an independently maintained authority. Adoption and cutover remain pending; this Draft does not authorize promotion or Current-source changes.

## Details

The root Project Scope Unit's Declaration is externally Operator-owned, like the Project Goal. The Operator Actor is not a Scope Unit. Its final physical Carrier location and discovery remain for adoption; central Draft staging does not settle them.
