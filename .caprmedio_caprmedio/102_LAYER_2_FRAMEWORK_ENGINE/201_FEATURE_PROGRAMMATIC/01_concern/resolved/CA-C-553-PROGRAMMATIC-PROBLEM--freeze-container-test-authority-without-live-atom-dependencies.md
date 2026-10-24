---
atom_id: CA-C-553
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2498, CA-P-2495]
version: 3
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Freeze container test authority without live Atom dependencies

## Concern

The first container fixture revision reads live repository authority carriers and the live selected projection while preparing tests. Hash-pinning those mutable inputs does not make them a golden corpus: an unrelated real Atom revision would break the suite.

## Evidences

Read-only review of tests/container_lifecycle_fixture.py found REPOSITORY/.caprmedio carrier scanning in _locate_source and a live PROJECTION input. This is a fixture design defect, not a production incident. No container-caller acceptance is claimed from that initial self-check.

## Blast radius

P2498 must retain the selected authority bytes and closed route shape in its dedicated frozen fixture corpus. Runtime tests must read only that corpus and disposable Project data, with source-pin integrity checks; authoring-time harvesting is separate. P2495 acceptance waits for this correction. Do not alter live Atoms or the existing legacy corpus to make tests pass.

### Resolution evidence

P2498 and P2504 are Done after frozen-source correction. Runtime fixture reads only its dedicated checked-in corpus and the existing frozen workflow corpus; all seven pinned original byte hashes verified. Full source_context_from_project admits38 sources and the real seal selects one nested child. Independent read-only review PASS; fixture SHA-256 eca3d27d63dc454ea2169e574ea78b99aa17f51ce5c8360ccfaaf66be678d97d. No live authority carrier or production MCP was changed. Recursive effect acceptance remains separate under P2495/C551.
