---
atom_id: CA-P-937@3
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - CA-P-936
  - CA Deterministic Routing Runtime Tool Implementation
version: 3
updated_at: 2026-10-24 07:12:55 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Implement CA Deterministic Routing Runtime Tools

**when** CA-P-936 is Done, **then** the Assignee **must** implement the deterministic provider-neutral Tools that load the accepted CA authority, normalize an invocation, resolve the active Project, select the canonical route, and admit or reject the requested effect.

## Scope

`((accepted CA Main Skill Authority Bundle) union (canonical Tool source, schemas, tests, structured results, and failure contracts for CA authority loading, normalization, Project resolution, routing, effect classification, approval gating, and authority-snapshot pinning))`

## Definition of Done

the Task is **not done if** (identical authority and invocation inputs can produce different route results **or** any Tool invents authority, embeds host-specific Skill procedure, bypasses an effect or approval gate, accepts an unresolved Project or route, widens scope implicitly, or fails open **or** results omit the selected authority revision and digest, normalized request, exact route, effect class, approval decision, and explicit failure meaning **or** focused positive, negative, stale-snapshot, ambiguity, and determinism tests fail).

## Details

keep Tool mechanics independent from MCP transport and Skill prose. pin one accepted authority snapshot for each invocation and reject a mid-run authority change until an explicit reload creates a new admitted snapshot.
