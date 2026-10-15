---
atom_id: CA-M-385
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Projection/Type: Entities Graph"
  depends_on: ["Entity", "Entity/Continuant/Object/Relation", "Entity/Continuant/Object/Atom", "Entity/Continuant/Projection"]
version: 3
updated_at: "2026-10-15 18:48:49 +0000"
relations:
  method_for: [CA-R-1456]
---
# Summary

Generate readable Entities Graph trees programmatically

## Scope

The readable Inherency view of an Entities Graph.

## Claim

Generate the Inherency view with deterministic code from the selected sources and their explicit typed relations. **Do not** use an LLM to choose nodes, classify edges, invent relations or arrange the output.

## Details

1. Read the selected source Atoms and their Versions. Retain qualified identities and relation evidence; collect every contributing Atom, including reused governing definitions, in the source list.
2. Select the admitted Inherency relation facts: NARROWER_THAN, IS_BORNE_BY and IS_ALLOWED_VALUE_OF. Atom Subjects depends_on is not IS_BORNE_BY.
3. Render the primary-entity hierarchy first, broader before narrower, excluding dependent entities. Record first-appearance order while retaining every shared-parent placement.
4. In that order, render one detail section for each primary entity with dependents. Traverse bearer to dependent and property to allowed value, retaining qualifications and relation distinctions. Reuse inherited facts only where source rules admit inheritance; do not author new source facts.
5. Use source-declared sibling order where available; otherwise sort alphabetically by display name, breaking equal-name ties by qualified identity. Use the same ordering for roots. Track the current traversal path so a cycle is reported once at that placement rather than expanded forever; shared nodes on different paths are not cycles.
6. Serialize through CA-D-634. Report unavailable source facts without guessing. The source list and tree body depend only on the selected source data and declared rules; updated_at is the completed rebuild time.

## Outcome

A reader can see what kinds exist, their dependent entities and allowed values, without mixing these meanings.

Construction/CONTAINS projection is deferred to the adjacent `draft/` RMED. It is not required by this active readable-view specification.
