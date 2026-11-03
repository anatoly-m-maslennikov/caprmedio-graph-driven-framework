---
atom_id: CA-M-385
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/(.Type: Entities Graph)'
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Projection
version: 25
updated_at: 2026-11-02 19:46:47 +0400
relations:
  method_for:
  - CA-R-1456
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-385-CORE_META_MODEL-IMPLEMENTATION_METHOD--generate-readable-entities-graph-trees-programmatically.md
  source_atom_id: CA-M-385
  source_atom_revision: 25
  source_sha256: 49430b8501ce05abaa1827510a00097f5e3abc99a90b472918694b09cbfb39f7
  original_relations_sha256: 7733f3e3021e6be18516933e27e8835adbc33729eb63b7a4e716166b11e30c93
---
## Summary

Generate readable Entities Graph trees programmatically

## Claim scope

The readable structural Inherency and named declaration views of an Entities Graph.

## Claim

Generate the structural Inherency and selected named declaration views with deterministic code from their selected sources and explicit governing evidence. **Do not** use an LLM to choose nodes, classify edges, invent relations or arrange the output.

## Details

1. Read the selected source Atoms and their Versions. Retain qualified identities and relation evidence; collect every contributing Atom, including reused governing definitions, in the source list.
2. Select the admitted Inherency Relation facts NARROWER_THAN, INSTANCE_OF and IS_PROPERTY_OF, and preserve source-backed allowed-value qualifications as value annotations rather than graph Relations. Atom Subjects depends_on is not IS_PROPERTY_OF. Traverse an explicit INSTANCE_OF fact from kind to its named instance for display, using `//`; retain the fact's instance-to-kind direction and existing target identity. Do not enumerate instances from syntax or classify an instance name as a Term.
3. Render the primary-entity hierarchy first, broader before narrower and kind before its selected named instance, excluding Properties. `/` and `//` remain distinct; specialization alone does not prove independent identity. Record first-appearance order while retaining every shared-parent placement.
4. In that order, render one detail section for each selected Entity with Properties or admitted allowed values. Traverse bearer to Property and display each target Entity's allowed values as annotations, retaining qualifications and Relation distinctions. An allowed-value target need not be a Property; display its values under that actual Entity without inventing a Property, Classification kind, graph Node or Relation. Direct Property-value Format/cardinality remains separate from Relation counts. Reuse inherited facts only where source rules admit inheritance; do not author new source facts.
5. Use source-declared sibling order where available; otherwise sort alphabetically by display name, breaking equal-name ties by qualified identity. Use the same ordering for roots. Track the current traversal path so a cycle is reported once at that placement rather than expanded forever; shared nodes on different paths are not cycles.
6. Serialize through CA-D-634. Report unavailable source facts without guessing. The source list and tree body depend only on the selected source data and declared rules; updated_at is the completed rebuild time.

### Named declaration view

Select named Relation Types declared by the selected governing R/Relation Definition Atoms. Keep their canonical names, defining Atom IDs/Versions, meaning and explicitly declared direction, inverse, derivation or transitivity. Equal canonical names identify the shared Type; report incompatible meanings without choosing a winner. Do not enumerate actual endpoint tuples from Atom relations as Type declarations.

Constraints are part of the relevant Entity Definitions, not separate Graph Rule instances or YAML-only Claims. They remain in the structural/property view. Use admitted compact notation and explicit relation labels, including structural containment; inherited properties cross specialization only, not containment. Use source-declared order, otherwise alphabetical order, and serialize through CA-D-634. Do not evaluate expressions, infer missing links or edit sources while rendering.

### Outcome

A reader can see what kinds exist, their Properties and allowed values, without mixing these meanings.

Preserve declared containment alongside specialization in the model tree; their different operators retain their different meanings.

### Current source pin and pending adoption

Proposed N+1 successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-385-CORE_META_MODEL-IMPLEMENTATION_METHOD--generate-readable-entities-graph-trees-programmatically.md`, Version 20, SHA-256 `86690d15dde34b2d48d66002bfdf70e5eb4f11133d0590ac20d0911691ce3236`. Current bytes remain unchanged. The new Relation names depend on the pending IS_PROPERTY_OF / HAS_PROPERTY Relation Definition Drafts; this source does not admit them through a renamed token alone. This preparation performs no runtime change, generated-view refresh or promotion.
