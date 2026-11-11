---
atom_id: CA-P-2485
content_role: Plan
type: Plan
label: Task
work_sequence_number: 61
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T19:57:02.961Z"
---
# Summary

Guard flat Plan archive bundles

## Objective

Prevent flat Plan archive from silently relocating independent current descendant Atoms.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2484 archive-root contract. Same publication owner files as P2484; no concurrent writes. Require separately admitted descendant actions under CA-R-1521, preserve current descendant placement and incoming references. Check optional matching directory and asset collisions without inventing cascade, relation removal or link repair policy. No legacy migration. Add one focused synthetic behavior check at the existing public lifecycle boundary; split further if own work exceeds 15 minutes.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
