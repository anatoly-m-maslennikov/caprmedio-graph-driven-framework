---
atom_id: CA-P-2467
content_role: Plan
type: Plan
label: Task
work_sequence_number: 56
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-20T19:11:21.413Z"
---
# Summary

Promote existing Atom Draft to the same identity

## Objective

Implement the Operator decision: CA-R-123@4-draft promotes to canonical CA-R-123 version 4, archiving the exact Current predecessor.

## Details

At most 15 minutes own work; split before extending. Preserve ID-free fresh allocation and existing canonical uniqueness. Bind exact Current target and proposed next Version; reject mismatches, collision or stale sources before effects. No retained Draft-history or Journal admission prerequisite. Reuse the existing safe revision owner rather than another executor.

### Definition of Done

Focused synthetic functional evidence proves same-ID version advancement, byte-exact predecessor archive, no duplicate Current, stale/version mismatch denial and no collateral writes. Independent review required. No deployment, live migration or held-batch replay.

### Bounded decomposition

The remaining generic promotion work is split before extending own work: CA-P-2468 binds the exact Draft and canonical predecessor; CA-P-2469 reuses safe publication and recovery after that preflight; CA-P-2470 verifies both native entry points after publication. Each child has at most 15 minutes own work. This parent is a roll-up, not another implementation budget. Review the dependent child after each completion.

### Verified execution checkpoint

Published marker promotion behavior is implemented and independently accepted: P2468, P2469/P2472/P2475, P2470 and P2474 passed exact binding, shared publication/recovery, all Current-status placement, native/lifecycle and fresh-Status checks. Exact no-op is mutation-free. This rollup remains Active only because P2477 retains explicit complexity follow-up C546/P2478; no runtime adoption or broader Epic completion is claimed.
