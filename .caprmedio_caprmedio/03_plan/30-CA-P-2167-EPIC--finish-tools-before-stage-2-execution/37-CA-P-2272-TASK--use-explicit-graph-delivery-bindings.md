---
atom_id: CA-P-2272
content_role: Plan
type: Plan
label: Task
work_sequence_number: 37
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2278
tier: 3
---
# Summary

Use explicit graph Delivery bindings

## Objective

Graph delivery paths derive from declared bindings rather than reconstructed folder names.

## Details

Initial bounded implementation: up to 15 minutes, authorized by the Operator's continuation after accepted source review. Any larger remaining work requires bounded decomposition before execution.

Use actual Project Structure Implementation Folder/Delivery bindings for both new FEATURE groups and unchanged legacy units. Remove the affected derivation assumption only; verify different authority/delivery naming and preserved old rows. This does not remap Subjects, generate migration outputs or infer native relations/runtime readiness.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Earlier Delivery-only checkpoint

Explicit Delivery binding and terminal-slash compatibility passed bounded independent checks (20 focused tests plus independent invalid/alias controls). At that checkpoint, live graph discovery still inferred topology from folder names and failed on the legacy 201 prefix. CA-P-2302–2304 separately repair and verify that existing R1070/M149/E295 obligation; the delivery-only receipt does not accept the broader repair.

### Bounded acceptance and remaining gate

The [bounded independent graph receipt](../../_projection/core-entity-review/stage2/tools-first/declaration-graph-acceptance.md) accepts the topology/observation implementation and exact pins: 30 tests passed and the current read-only declaration probe returned 29 Scope Units. The shared cross-Project path guard remains incomplete, so complete invalid-declaration refusal is not yet accepted and this Task stays Active. Settings revision resolution also blocks full graph/runtime readiness. No publication is authorized by the bounded receipt.

### Bounded Project boundary continuation

The Operator chose caprmedio_project_settings.toml as the canonical Settings filename; align the conflicting rules without renaming current Settings. Separate foreign-boundary refusal from graph Settings revision evidence. No synthetic receipts, broad legacy migration or installed activation.

- [CA-P-2320 — Align canonical Settings filename](37-CA-P-2272-TASK--use-explicit-graph-delivery-bindings/done/01-CA-P-2320-TASK--align-canonical-settings-filename.md)
- [CA-P-2321 — Verify declaration path Project boundaries](37-CA-P-2272-TASK--use-explicit-graph-delivery-bindings/done/02-CA-P-2321-TASK--verify-declaration-path-project-boundaries.md)
- [CA-P-2322 — Bind declaration boundary consumers](37-CA-P-2272-TASK--use-explicit-graph-delivery-bindings/done/03-CA-P-2322-TASK--bind-declaration-boundary-consumers.md)
- [CA-P-2323 — Verify Project boundary refusal](37-CA-P-2272-TASK--use-explicit-graph-delivery-bindings/done/04-CA-P-2323-TASK--verify-project-boundary-refusal.md)

### Private boundary implementation checkpoint

P2320 is Done after independent source acceptance and the completed affected FPF review. P2321 and P2323 are Active: implement the existing private shared boundary check and prepare independent fixtures. P2322 waits for the stable helper contract. Exact marker bytes and absence observations prove boundary/currentness only; they are not synthetic logical Settings revision evidence. Settings revision resolution, complete graph readiness and public activation remain separate gates.

### Boundary helper checkpoint

The private P2321 helper passed ten author tests, eight independent tests and separate code review. P2322 is now Active to retain the proof at Selection time and wire actual consumers, including operation-scoped revalidation for long-lived selections without recapturing original pins. P2323 continues actual caller tests. See declaration-boundary-helper-acceptance.md for the bounded checkpoint; no complete caller/runtime acceptance is claimed yet.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.

### Boundary consumer acceptance — 2026-10-13

P2321, P2322 and P2323 are Done after final-pin independent review, 22 independent boundary tests, Graph 36, Structure 23, Scope 12 and full Atom validation 344 passed. Both declaration paths retain original Settings marker hashes and absence evidence through Selection, Graph, Scope, Structure and complete-carrier validation; drift and late proof reconstruction refuse. The normal Structure fixture executes the shared service, mutation and Journal path. This closes the foreign-boundary refusal gap, not the missing Settings logical Revision evidence. The parent remains Active until its remaining graph requirements are met. MCP registration still lacks an offline dependency; no installed activation is claimed.
