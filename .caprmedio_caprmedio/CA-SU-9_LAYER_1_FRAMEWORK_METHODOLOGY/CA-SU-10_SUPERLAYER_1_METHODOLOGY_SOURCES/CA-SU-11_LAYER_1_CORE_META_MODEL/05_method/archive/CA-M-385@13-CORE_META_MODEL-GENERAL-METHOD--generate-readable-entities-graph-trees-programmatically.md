---
atom_id: CA-M-385@13
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Entities Graph'
  depends_on:
  - Subject/Domain/Node
  - Subject/Graph/Relation
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Projection
version: 13
updated_at: 2026-10-24 02:14:24 +0400
relations:
  method_for:
  - CA-R-1456
tier: 4
type: Implementation Method
---
# Summary

Generate readable Entities Graph trees programmatically

## Scope

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

Keep the full structural Inherency view and the middle-level declaration view separate, with explicit source and display selections. Keep Core and Project source boundaries separate in each selection. Steps 1–6 describe the Inherency rendering, not a requirement to turn declaration metadata into Inherency edges.

1. Collect admitted named Relation Type declarations from their selected governing sources. Retain graph-qualified identity, descriptive metadata and every contributing source ID/Version. Use only source-backed classifications and values; report missing, conflicting or unresolved metadata rather than guessing it. Do not classify declarations from actual Atom-to-Atom tuples or name spelling alone.
2. Collect concrete Requirement/Type Graph Rule declarations under CA-R-2001. Use bounded parsing and carrier validation under CA-D-637; reuse a suitable implementation where available. Unavailable parsing or schema support remains an explicit gap. This Method specifies the behavior; it does not itself implement a parser or prove runtime availability. Retain the source Atom identity, Version, governed Subject, readable Summary and exact operative YAML. Examples and ordinary defining Requirements are not Rule instances. Unsupported rule forms remain schema-coverage gaps; do not invent their schemas or treat them as absent.
3. Preserve opaque YAML values, including default_value, without normalization into another data format. A declared relation_type reference retains its literal source value; an unresolved reference is reported, not silently rewritten or used to import outside authority.
4. Group repeated references to the same graph-qualified Relation Type without merging equal names from different graph kinds. Retain all contributing source evidence and report conflicting values without choosing a winner. Use declared order where available; otherwise sort alphabetically with qualified identity as the tie-breaker. Concrete Graph Rule records retain their source Atom identities.
5. Serialize the selected declarations through CA-D-634 and preserve Projection identity under CA-R-1943. Generate with deterministic code, not an LLM. The result reports declarations and coverage; it does not evaluate conditions, apply defaults, combine rules, infer missing links, create instances or rewrite source Atoms.

## Outcome

A reader can see what kinds exist, their dependent entities and allowed values, without mixing these meanings.

Construction/CONTAINS projection is deferred to the adjacent `draft/` RMED. It is not required by this active readable-view specification.
