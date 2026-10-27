---
atom_id: CA-P-2273@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Scope Unit
  - Action
  - Workflow
  - Configuration
  - Revision
  - Journal
  - Plan
  - Operator
version: 3
updated_at: 2026-10-24 06:04:04 +0400
relations:
  is_decomposition_of:
  - CA-P-2174
  blocks:
  - CA-P-2278
tier: 3
---
# Summary

Verify connector API and Query and Read fixtures

## Objective

Independent fixtures verify the shared connector API and Atom/Scope Unit Query and Read.

## Details

Estimated own work: 15 minutes. Independent verification work. Split concrete work larger than this bound into actual bounded children before execution. This Backlog Task is current pending work, not a future-Version Scope or authorization to execute now.

Use actual current accepted source/API/code pins and independently authored expected requests/results. Cover valid empty/singular/multiple and explicit unpinned/pinned/history Reads, scope/field/exact/start/end/contains filters, structured errors/effect-free results, malformed/stale/ambiguous cases and deliberate wrong-output controls. The verifier does not derive its oracle from producer code.

Assignee: AI Agent independent of implementation authors. Read-only fixture preparation may precede code readiness; actual acceptance waits for applicable current accepted contracts, CA-P-2251 review and stable implemented code pins. Author the oracle independently and record actual cases, pins, effects and limitations.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Approved internal separation checks

Independently verify the internal parsing/reading/writing/CLI boundary in the affected rebuilt connectors while keeping the public request/result API unchanged. Parsing supplied content has no filesystem effects; Read is mutation-free; Write changes only admitted supplied state; CLI dispatch adds no parsing, storage or lifecycle policy. Test invalid input, truthful no-op and error/effect evidence as well as valid requests.

Reuse the existing operation-specific verification owners: CA-P-2274 covers affected carrier/property/section effects and CA-P-2275 covers TOML/configuration behavior. Helpers must not become public Tools, and the test oracle must not accept Workflow policy hidden in a connector. Verify only actual changed implementation pins; no new capability is admitted by these Plan instructions.

### Definition of Done

The Plan is **not** Done if expected results are producer-derived, any required valid/refusal/wrong-output check is absent or fails, actual bytes/effects/pins or limits are unproven, or a passing subset is claimed as full live/runtime readiness. Own work must not exceed 15 minutes without prior decomposition.
