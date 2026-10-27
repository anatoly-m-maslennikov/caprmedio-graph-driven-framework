---
atom_id: CA-P-2270@9
content_role: Plan
type: Plan
label: Task
work_sequence_number: 35
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
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
updated_at: 2026-10-24 06:12:24 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2278
tier: 3
---
# Summary

Refresh authority consumers and release admission

## Objective

Affected authority consumers and release/admission bindings use actual current rebuilt source pins.

## Details

Initial bounded implementation: up to 15 minutes, authorized by the Operator's continuation after accepted source review. Any larger remaining work requires bounded decomposition before execution.

Replace affected hardcoded authority assumptions with actual declared source ownership/delivery evidence. Refresh only approved release/admission bindings after complete independently accepted contracts and FPF review; preserve historical receipts and unrelated authority. Prove stale/old source pins fail safely and source acceptance is not runtime activation.

Start only after CA-P-2251's actual accepted FPF review and independently accepted applicable current contracts, not a Plan-validation result or historical pins. Bind actual contract/API/code pins and permissions. Require separately accepted applicable Core alignment under CA-P-1970 where rules conflict; no Core/content work is included here. Source authoring or this pending Task grants no runtime/live authority.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Current checkpoint

The registered-owner resolver passed bounded independent checks (11 focused tests and 11 independent assertions). Full Release admission remains unproven: CA-D-572 was deliberately archived without a current successor. Do not restore it or use historical/installed bytes as current authority. Source/consumer disposition remains separate from the accepted resolver change.

### Bounded continuation — 2026-10-13

[CA-P-2315 — Resolve graph authority from declared sources](35-CA-P-2270@9-TASK--refresh-authority-consumers-and-release-admission/done/01-CA-P-2315-TASK--resolve-graph-authority-from-declared-sources.md) is Done after independent acceptance and commit 92261be4e. The finite source-ID set, exact source checks and stale-pin refusal remain intact. Later PRMEDO-only cleanup is separately approved under CA-P-2325; C/A remains deferred. Missing current CA-D-572 still blocks complete Release admission. This parent stays Active.

### Definition of Done

The Plan is **not** Done if applicable accepted contracts/FPF gates or current pins are missing; focused valid, refusal and no-op/error/effect checks fail or lack actual results; unrelated behavior regresses; implementation is claimed from preparation; or deferred/unauthorized capability is enabled. Own work must not exceed 15 minutes without prior decomposition.

### Superseded release gate — 2026-10-13

The earlier missing-D572 statements above are historical, not a current release prerequisite. The Operator's completed P1848 v12 direct happy path explicitly supersedes release admission/snapshot/seal gates; current M332 v6 and O164 v14 define that path. The registered release_version route dispatches directly to PROJECT_TOOLS/RELEASE_VERSION/local_release.py rather than the legacy D572 admission flow. Do not restore D572, invent a successor or revive the old ten-Step gate. Verify affected current direct-route behavior and current rebuilt consumers; preserve fail-closed legacy code/history separately. Active references in R1847/D521/R1882/D589 remain explicit reconciliation debt, not evidence that D572 is current. This correction does not authorize a release, folder relocation or runtime activation and does not complete the parent.

### Completed bounded outcome — 2026-10-13

Current declared-owner consumer checks and 23 direct-release tests passed independently. The latest direct-route policy retires the old admission/seal gate; it does not require a replacement for D572. Actual runner loading, pre-dispatch refusals and truthful temporary Journal outcomes are verified. P2315's finite source/currentness acceptance remains intact. Live release, runtime activation and legacy reference reconciliation are not claimed.

Current evidence: [graph and direct release consumer completion](../../../_projection/core-entity-review/stage2/tools-first/graph-and-direct-release-completion.md). Earlier remaining-gate statements above are historical and superseded only for this verified bounded outcome.
