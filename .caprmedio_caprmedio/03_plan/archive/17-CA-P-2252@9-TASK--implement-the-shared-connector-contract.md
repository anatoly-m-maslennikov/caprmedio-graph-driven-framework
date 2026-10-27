---
atom_id: CA-P-2252@9
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Action
  - Workflow
  - Configuration
  - Revision
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 9
updated_at: 2026-10-24 07:45:09 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2253
  - CA-P-2254
  - CA-P-2255
  - CA-P-2256
  - CA-P-2257
  - CA-P-2258
  - CA-P-2268
  - CA-P-2269
  - CA-P-2273
  - CA-P-2280
tier: 3
---
# Summary

Implement the shared connector contract

## Objective

The shared logical connector request/result contract is implemented with focused conformance checks.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. The Operator authorized this bounded implementation through the current Epic continuation. This Active Task covers only shared contract support; downstream adapters, placement and runtime admission remain separate.

Implement the accepted CA-D-625/CA-R-1936/CA-M-376/CA-E-628 boundary without a new server, transport or database backend. Enforce the closed logical request, supported operation subsets, exact preconditions and structured data/current_state/effects/errors result. Preserve stable error meanings, known/unknown effects, nonempty-errors failure and verified no-op behavior. Add focused positive and wrong-shape/error/effect controls; existing outer envelopes remain separate.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Current execution boundary

CA-P-2251's original review and affected Configuration Read follow-up have completed. The applicable common interface sources R1936 v1, M376 v1, E628 v1 and D625 v2 were independently rechecked against accepted pins before this implementation. No source conflict was found for the internal module separation.

Implement only private pure request/result validation support and focused conformance fixtures at the existing TOOLS support boundary. Do not replace legacy Atom runners, change public envelopes or materialize new executable bindings. Actual permission/source/schema resolution, backend currentness and observed postcondition/no-op verification remain the receiving adapters' obligations. A structural validator or supplied observation flag does not prove those runtime facts.

CA-P-2253–2258/2280 adopt the support in their bounded adapters. CA-P-2269 owns later placement and caller/export migration. Independent review must distinguish shared representation checks from unimplemented adapter behavior; this Task cannot declare the whole connector portfolio or live route ready.

### Approved internal separation

Apply CA-P-2167's latest shared-module decisions: separate parsing, reading, writing and CLI responsibilities without changing the public logical connector API or creating helper Tools. Keep lifecycle and sequencing policy in Workflows; retain connector checks of the supplied schema, permission and currentness. Reuse fitting existing modules rather than adding an umbrella facade.

Before implementation, check the applicable RMEDO against these decisions and resolve relevant effective source bindings (SG001). If a contract change is required, obtain its fresh independent acceptance and affected FPF review before dependent code. This Task does not silently rewrite RMEDO. Identify affected code, callers, exports, fixtures and checks; coordinate any placement/CLI ownership change with CA-P-2269. Legacy modules outside the bounded implementation stay unchanged.

### Accepted implementation result

The bounded private shared contract support is complete after [independent structural acceptance](../../../_projection/core-entity-review/stage2/tools-first/shared-connector-contract-acceptance.md). The earlier Active instructions above describe execution, not the current status.

The implementation is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/connector_contract.py`, SHA-256 `0ca555782e8e2cfe689d9d0a19c9c43d4440cc930c0a4a1e266c867eb6d4b591`; its focused test file is `tests/test_connector_contract.py` under that same TOOLS root, SHA-256 `9c2049c6f003c54417a8461803ff8cbb789d2f2e7ec13fdcaa9cd2188f97e5c0`. The independent receipt SHA-256 is `7db66989f9eb038d1f891583c691463b90f7eef5b47fa26e3f734cb667f29b97`.

The 15 focused tests passed under the repository-supported Python 3.14 through uv; an independent reviewer reran them and passed 140 additional assertions. The pure helpers check the closed request/result representation, supported subsets/kinds, required structural preconditions, stable errors and effect/verification/no-op consistency. They do not mutate supplied evidence or perform storage/CLI/lifecycle work. Existing public APIs and callers remain unchanged.

This completion releases only the shared-support prerequisite. Actual receiving-adapter schema/permission/currentness/preview checks and observed postconditions, the remaining independent connector portfolio, placement and runtime admission remain with the downstream Tasks. Private observation flags are not proof of actual effects or authority. No live route or migration is accepted.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
