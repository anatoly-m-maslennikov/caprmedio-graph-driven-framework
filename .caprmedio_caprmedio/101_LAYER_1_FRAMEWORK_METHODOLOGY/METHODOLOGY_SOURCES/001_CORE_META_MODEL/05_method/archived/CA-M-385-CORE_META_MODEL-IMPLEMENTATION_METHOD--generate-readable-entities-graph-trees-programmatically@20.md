---
atom_id: CA-M-385
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Entities Graph'
  depends_on:
  - Entity
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Projection
version: 20
updated_at: 2026-10-29 09:31:44 +0400
relations:
  method_for:
  - CA-R-1456
tier: 4
type: Implementation Method
---
## Summary

Generate readable Entities Graph trees programmatically

## Claim scope

The readable structural Inherency and named declaration views of an Entities Graph.

## Claim

Generate the structural Inherency and selected named declaration views with deterministic code from their selected sources and explicit governing evidence. **Do not** use an LLM to choose nodes, classify edges, invent relations or arrange the output.

## Details

1. Read the selected source Atoms and their Versions. Retain qualified identities and relation evidence; collect every contributing Atom, including reused governing definitions, in the source list.
2. Select the admitted Inherency relation facts: NARROWER_THAN, INSTANCE_OF, IS_BORNE_BY and IS_ALLOWED_VALUE_OF. Atom Subjects depends_on is not IS_BORNE_BY. Traverse an explicit INSTANCE_OF fact from kind to its named instance for display, using `//`; retain the fact's instance-to-kind direction and existing target identity. Do not enumerate instances from syntax or classify an instance name as a Term.
3. Render the primary-entity hierarchy first, broader before narrower and kind before its selected named instance, excluding dependent entities. `/` and `//` remain distinct; specialization alone does not prove independent identity. Record first-appearance order while retaining every shared-parent placement.
4. In that order, render one detail section for each primary entity with dependents. Traverse bearer to dependent and property to allowed value, retaining qualifications and relation distinctions. Reuse inherited facts only where source rules admit inheritance; do not author new source facts.
5. Use source-declared sibling order where available; otherwise sort alphabetically by display name, breaking equal-name ties by qualified identity. Use the same ordering for roots. Track the current traversal path so a cycle is reported once at that placement rather than expanded forever; shared nodes on different paths are not cycles.
6. Serialize through CA-D-634. Report unavailable source facts without guessing. The source list and tree body depend only on the selected source data and declared rules; updated_at is the completed rebuild time.

### Named declaration view

Select named Relation Types declared by the selected governing R/Relation Definition Atoms. Keep their canonical names, defining Atom IDs/Versions, meaning and explicitly declared direction, inverse, derivation or transitivity. Equal canonical names identify the shared Type; report incompatible meanings without choosing a winner. Do not enumerate actual endpoint tuples from Atom relations as Type declarations.

Constraints are part of the relevant Entity Definitions, not separate Graph Rule instances or YAML-only Claims. They remain in the structural/property view. Use admitted compact notation and explicit relation labels, including structural containment; inherited properties cross specialization only, not containment. Use source-declared order, otherwise alphabetical order, and serialize through CA-D-634. Do not evaluate expressions, infer missing links or edit sources while rendering.

## Outcome

A reader can see what kinds exist, their dependent entities and allowed values, without mixing these meanings.

Preserve declared containment alongside specialization in the model tree; their different operators retain their different meanings.
