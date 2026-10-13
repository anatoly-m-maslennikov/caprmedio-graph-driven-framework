---
atom_id: CA-P-2256
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 4
updated_at: "2026-10-13 20:30:21 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2266, CA-P-2267, CA-P-2269, CA-P-2275]
---
# Summary

Implement TOML item and full-set edits

## Objective

The shared TOML connector performs accepted add, replace and remove edits with truthful results.

## Details

Initial bounded implementation: up to 15 minutes. The Operator authorized continuation after accepted RMEDO/FPF prerequisites. Remaining work is decomposed below before the next bounded phase; the parent remains Active until its complete original Definition of Done is met.

Implement one shared connector for item/value and full-set add/replace/remove, explicit target/current-state and exact no-op. Preserve unrelated TOML meanings and reject malformed or ambiguous input safely. Do not substitute this connector for Project Structure or Project Settings Workflow schema checks; those adapters remain distinct.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Bounded continuation

The initial private mechanics are implemented or in progress; this is not accepted receiving/runtime capability. Continue through [CA-P-2297 — Bind TOML modifications to receiving schemas](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/01-CA-P-2297-TASK--bind-toml-modifications-to-receiving-schemas.md). This child is limited to 15 minutes and must be split again before larger work. Remaining publication, receiving Workflow and independent portfolio gates are unchanged.

### TOML text preservation

The Operator approved a narrowly scoped TOMLKit dependency, its M/D/E selection and the private connector implementation. It does not enable live writes or migration. Complete the bounded work through:

- [CA-P-2307 — Select TOMLKit for preserving configuration text](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text.md)
- [CA-P-2308 — Preserve TOML text during pure edits](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/03-CA-P-2308-TASK--preserve-toml-text-during-pure-edits.md)
- [CA-P-2309 — Verify TOML text preservation independently](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/04-CA-P-2309-TASK--verify-toml-text-preservation-independently.md)
- [CA-P-2310 — Integrate preserving TOML materialization](21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/001_backlog/05-CA-P-2310-TASK--integrate-preserving-toml-materialization.md)

The existing receiving-schema Task CA-P-2297 remains separate. The additional Markdown/YAML library question is assessment-only, not dependency approval.

### Current source gate

The typed source repair passed independent semantic and exact-history review, followed by real finite PRMEDO admission for M383 v3, D632 v3, E635 v2 and P2307 v8. Each passed 13 checks with zero findings/gaps; no relation bypass. P2308 and P2309 are now Active for the private pure materializer and independent literal-byte tests. The prior affected FPF selection review remains accepted; this metadata-only repair introduced no new behavior. P2310 waits for accepted implementation. Receiving schemas, writes and runtime activation remain separate.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.
