---
atom_id: CA-P-2491@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2484
version: 5
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Align Archived Plan Draft promotion destinations

## Objective

Complete shared flat destinations and exact history for existing-ID and ID-free Plan Draft promotion directly to Archived.

## Details

At most 15 minutes own work; split before extending. Depends on P2490 shared preserved-revision owner and reviewed P2484 resolver. Existing-ID promotion still uses local destination/history helpers, causing a mismatch with newly flat Plan publication. ID-free promotion constructs a canonical filename but the new Archived Plan branch ignores that filename and derives the Draft stem. Reuse the canonical archive/preservation owners with the already-bound prospective canonical filename and proposed/current Versions; do not create another business rule, discard pins or alter fresh identity semantics. Own atom_operations.py and lifecycle_intents.py, serialized after P2490. Add focused functional regression through existing native/lifecycle entry points; external test worker owns new archive test file. Preserve non-Plan paths, exact no-op/currentness/collision/recovery and previous uncommitted work. No bundle-policy, C549 history relocation decision, new approval/Journal gate, deployment or migration.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review and execution admission

P2490 is complete and root-reviewed; preserved_revision_destination is the canonical history API, with non-Plan legacy spelling unchanged. Execute only P2491 promotion branch repair in the existing atom_operations/lifecycle owners. Bind the already-constructed prospective canonical filename for fresh Draft Archived placement and the exact proposed/resulting Version for existing-ID destination/history; do not derive the final filename from an ID-free Draft stem or bypass history verification. Preserve no-op, byte pins, collision refusal and exact N predecessor. Coordinate promotion predicate additions with P2492 test owner after the public contract is stable. No P2485 history subtree or current-descendant policy implementation in this Task.

### Generic lifecycle Status adjudication and source alignment

Independent source adjudication resolved the apparent Active-only restriction at 98 percent confidence: General R1521@9 and D569 Claim already require generic explicit change_status to admit any qualified model value, while D569 Standard literal Active binding conflicts with that higher rule. R869 native ATOM_PROMOTE remains Active-only as a distinct capability. D569 is now Version 9, clarifying requested qualified model-admitted non-Draft Status and preserving every existing exact Draft/canonical target, Version/digest, permission and collision/currentness pin. No Plan-only exception, new enumeration, intermediate state or new approval gate is admitted. Ordinary same-Draft-Status no-op behavior remains unchanged.

Resume only the remaining generic lifecycle admission branch within the P2491 own-work budget; model resolution already occurs upstream and cannot be bypassed. Bind the same canonical target/proposed Version and reuse the mechanical shared destination/history helpers. Add a non-Plan or non-Archived model-admitted regression so tests do not merely validate a Plan-Archived special case. If more than the remaining own-work budget is needed, return a checkpoint and split before extending. C549 is the sole outstanding Operator question and is unrelated to this resolved source conflict.

### Verified completion

Existing/fresh Plan Draft archive routing and generic model-admitted existing-marker Change Status are implemented. P2496 completes the shared predecessor-path correction discovered during review. Independent replacement-freeze native acceptance passed flat archive14, selected lifecycle48 and version history9; code review APPROVE at atom_operations 537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284 and lifecycle 9e8f56400d8141f1e190f19dd499f2a39dd6346330e383d46ea7be1067107f0d. Exact no-op, source/canonical pins, previous bytes and cleanup recovery are retained. Native Promote remains Active-only. C549 is now answered; recursive callerP2494 remains separate unimplemented work.
