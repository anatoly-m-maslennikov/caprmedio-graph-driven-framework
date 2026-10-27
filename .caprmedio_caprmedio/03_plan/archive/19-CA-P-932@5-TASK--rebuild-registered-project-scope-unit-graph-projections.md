---
atom_id: CA-P-932@5
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
    - Project Scope Unit Graph Projections
    occurrent:
    - Project Scope Unit Graph Projection Rebuild
  depends_on:
    occurrent:
    - CA-P-935
version: 5
updated_at: 2026-10-24 06:04:25 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Rebuild Registered Project Scope Unit Graph Projections

**when** CA-P-935 is Done, **then** the Assignee **must** rebuild both registered persistent Project Scope Unit Graph Projections from the completed generator and exact current source frontier.

## Scope

`((.caprmedio_caprmedio/project_scope_unit_graph.projection.toml) union (.caprmedio_caprmedio/project_scope_unit_graph_sources.projection.toml) union (their active registration authority) union (the completed generator and exact declared sources))`

## Definition of Done

the Task is **not done if** (**either** Projection retains a retired source path, generator path, topology row, Project identity, **or** digest **or** the two Projections disagree about their source frontier **or** **any** row value required by current authority is absent **or** **any** source binding lacks its exact applicable revision, digest, **or** Work Journal record **or** output lacks generation procedure, updated-at value, generator identity and digest, exact source digest, **or** deterministic output digest **or** deleting both Projections prevents byte-identical regeneration **or** a Projection gains independent authority).

## Details

rebuild **only** the two registered persistent Scope Unit Graph Projections. preserve on-demand Entity Graphs and Subject indexes as non-persistent views.

## Completion Evidence

The selected hook-free installed `GENERATE_PROJECT_GRAPH_STATE` Tool rebuilt exactly the two registered persistent Projections. All 13 Scope Unit rows carry the active CA-R-626 fields, source binding validation resolves 13 exact Directory Carrier receipts, 13 active Delivery Atom bindings, and 250 field-level bindings with exact revisions, digests, and Work Journal records. The outputs retain lowercase `caprmedio`, current typed-parent topology, generator identity/digests, and non-authoritative status. Deleting both carriers and regenerating produced the same deterministic output-set digest; a repeated regeneration reported no change. Full falsifiable evidence is stored in `execution_evidence/CA-P-932@5-project-scope-unit-graph-projection-rebuild.projection.json`.
