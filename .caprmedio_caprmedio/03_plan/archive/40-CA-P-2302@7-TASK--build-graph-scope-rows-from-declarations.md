---
atom_id: CA-P-2302@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 40
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Project Structure
version: 7
updated_at: 2026-10-24 07:45:09 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2303
tier: 3
---
# Summary

Build graph Scope rows from declarations

## Objective

Construct Scope Unit semantic rows from the complete validated Project Structure declarations, using declared parent, type, label, level, ordering/navigation and paths. Include declared untyped and absent authority folders; preserve established node IDs where their declarations match. Directory shape must not override declared topology. Reuse actual validation and preserve explicit Delivery binding. No source/Scope folder/Subject migration or graph output publication is included.

## Details

Estimated own work: 15 minutes. Split larger work before execution. Reopen R1070/M149/E295 and current Structure authority. Preserve the accepted Delivery-only implementation/receipt as a separate checkpoint. An author owns generator and focused tests; a different reviewer owns independent verification. Root owns Plans and Git.

CA-P-2303 may consume the stable first candidate within the same isolated implementation packet before final independent acceptance; no affected Tool use is admitted until CA-P-2304 accepts the complete resulting pins. Earlier source acceptance and tests are not current runtime readiness.

### Bounded acceptance and remaining gate

The [bounded independent graph receipt](../../../_projection/core-entity-review/stage2/tools-first/declaration-graph-acceptance.md) accepts the topology/observation implementation and exact pins: 30 tests passed and the current read-only declaration probe returned 29 Scope Units. The shared cross-Project path guard remains incomplete, so complete invalid-declaration refusal is not yet accepted and this Task stays Active. Settings revision resolution also blocks full graph/runtime readiness. No publication is authorized by the bounded receipt.

### Definition of Done

Not Done until the bounded outcome has exact code/source pins and actual focused checks; the combined repair requires independent CA-P-2304 acceptance. Invalid declarations must still refuse. No historical pin rebinding, live source effects, Subject changes or production graph output is authorized.

### Completed bounded outcome — 2026-10-13

Complete declaration-driven topology and invalid-declaration refusal passed independent P2304 verification on current pins. The previously open foreign-Project boundary gap is closed. The live read-only probe returned all 29 Scope Units without source changes. Full graph publication and live Settings registration remain with P2272, not this bounded implementation.

Current evidence: [graph and direct release consumer completion](../../../_projection/core-entity-review/stage2/tools-first/graph-and-direct-release-completion.md). Earlier remaining-gate statements above are historical and superseded only for this verified bounded outcome.
