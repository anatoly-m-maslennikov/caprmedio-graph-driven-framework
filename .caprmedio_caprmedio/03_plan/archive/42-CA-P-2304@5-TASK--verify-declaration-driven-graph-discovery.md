---
atom_id: CA-P-2304@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 42
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Scope Unit
  - Projection
  - Plan
  - Project Structure
version: 5
updated_at: 2026-10-24 06:04:20 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2278
tier: 3
---
# Summary

Verify declaration driven graph discovery

## Objective

Prepare independent fixtures early, then verify the stable CA-P-2302/2303 implementation together. Cover legacy prefix 201 with declared level 3, folder ancestry/navigation disagreements, untyped and absent declarations, undeclared typed folders as observations only, exact TOML semantic attribution, safety refusals, deterministic output and unchanged authority. Reproduce the prior live read-only failure; do not publish graph outputs or claim runtime activation.

## Details

Estimated own work: 15 minutes. Split larger work before execution. Reopen R1070/M149/E295 and current Structure authority. Preserve the accepted Delivery-only implementation/receipt as a separate checkpoint. An author owns generator and focused tests; a different reviewer owns independent verification. Root owns Plans and Git.

CA-P-2303 may consume the stable first candidate within the same isolated implementation packet before final independent acceptance; no affected Tool use is admitted until CA-P-2304@5 accepts the complete resulting pins. Earlier source acceptance and tests are not current runtime readiness.

### Bounded acceptance and remaining gate

The [bounded independent graph receipt](../../../_projection/core-entity-review/stage2/tools-first/declaration-graph-acceptance.md) accepts the topology/observation implementation and exact pins: 30 tests passed and the current read-only declaration probe returned 29 Scope Units. The shared cross-Project path guard remains incomplete, so complete invalid-declaration refusal is not yet accepted and this Task stays Active. Settings revision resolution also blocks full graph/runtime readiness. No publication is authorized by the bounded receipt.

### Definition of Done

Not Done until the bounded outcome has exact code/source pins and actual focused checks; the combined repair requires independent CA-P-2304@5 acceptance. Invalid declarations must still refuse. No historical pin rebinding, live source effects, Subject changes or production graph output is authorized.

### Completed bounded outcome — 2026-10-13

Independent current-pin acceptance of P2302/P2303 is complete: all 49 graph tests passed, including three new integration tests with 173 subtests. Both serializers refuse newly introduced foreign markers; prior-output edits do not affect regeneration. The live read-only probe returned 29 declarations and 35 observations and preserved all 371 inspected source/Settings/Journal/output hashes. Both live Settings bindings remain unresolved; this is not full graph/runtime readiness.

Current evidence: [graph and direct release consumer completion](../../../_projection/core-entity-review/stage2/tools-first/graph-and-direct-release-completion.md). Earlier remaining-gate statements above are historical and superseded only for this verified bounded outcome.
