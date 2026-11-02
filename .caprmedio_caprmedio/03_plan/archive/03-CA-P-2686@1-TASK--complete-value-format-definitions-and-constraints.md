---
atom_id: CA-P-2686@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:00:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Complete value Format definitions and constraints

## Objective

Complete value Format definitions and constraints.

## Details

After CA-P-2684.

Complete the Format branch for value types only. Define the needed primitive formats and their actual properties/cardinalities; do not treat Markdown, YAML, TOML or JSON as value types or erase Carrier representation-format policy. Include scoped unique(named selection), permitted values, ranges and defaults only where the model declares them.

Define the selection and binding behind the accepted Atom.id composition. Keep its exact formal Claim in the Atom properties view with its full subjects.governs. Resolve Project prefix, Content Role initial, integer number and the Current-original population without creating a second stored number or silently substituting the most-specific Type for the Content Role number space. Ask one concrete question if a binding cannot be established with 95% confidence.

Create/refine the missing R/M/E/D Drafts as needed, including the new Definition anchors. R defines the format, M its authoring, E its cases and D the binding. Formal constraints belong in Definition Claims rather than a new Graph Rule instance registry.

## Definition of Done

Each selected value format and ID component has a defining source and usable contract, with exact uniqueness scope or an explicit unresolved question. Syntax and Format work may run in parallel after the inventory.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.
