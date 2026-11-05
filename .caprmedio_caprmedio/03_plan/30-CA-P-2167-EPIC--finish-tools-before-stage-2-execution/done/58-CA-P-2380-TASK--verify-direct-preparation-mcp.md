---
atom_id: CA-P-2380
ref_id: CA-P-2380
container:
  atom: CA-P-2167
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2167
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 58-CA-P-2380-TASK--verify-direct-preparation-mcp.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done
work_sequence_number: 58
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Verify direct preparation MCP

## Objective

Verify actual registered MCP preview and scratch staging on isolated fixtures, independently of the implementation author.

## Details

Prepare tests from the accepted public contract; final execution waits for CA-P-2379. Use the actual registry, schema and MCP transport, not mocked provider invocation. Check zero-write preview, unchanged source bytes, candidate/manifest readback, stale-source refusal, path and invalid-request rejection, and truthful partial scratch effects. No live publication, Journal fiction, installed activation or production Core migration.

Estimated own work: up to 15 minutes; split if necessary. Root owns Plans, integration and Git. Preserve unrelated work. Stage-specific gates are not whole-Task start blockers or Artifact depends_on Relations.

### Definition of Done

Real local MCP success/refusal tests pass against current source pins, and a different reviewer accepts the evidence. Clearly separate local protocol acceptance from installed runtime activation.

### Acceptance — 2026-10-14

The final eight-case suite passed in 25.700 seconds against the actual registered MCP server and client: seven transport cases plus one native CLI compatibility regression. Independent source-pinned fixtures exercise actual complete validation, lookup/binding and scratch writes; fault mocks inject failures only. Root inspected the test harness and accepted its evidence. Tests cover both review fixes, exact seals/readback, no-write refusals and partial/final-boundary evidence. Suite SHA-256: 532c3ac05111847e7b85679745f60783fa82fd4b5cc51be1e4c22ce19857d1a6. This is local protocol acceptance; the actual connected MCP still reports the tool unresolved.
