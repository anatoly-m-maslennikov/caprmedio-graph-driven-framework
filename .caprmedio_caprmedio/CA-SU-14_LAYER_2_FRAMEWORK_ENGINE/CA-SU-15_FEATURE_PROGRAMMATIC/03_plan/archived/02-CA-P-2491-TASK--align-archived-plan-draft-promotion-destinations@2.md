---
atom_id: CA-P-2491
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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
  is_decomposition_of: [CA-P-2484]
version: 2
updated_at: "2026-10-20T20:37:01.929Z"
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
