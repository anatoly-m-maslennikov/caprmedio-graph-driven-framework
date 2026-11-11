---
atom_id: CA-P-2490
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
version: 1
updated_at: "2026-10-20T20:31:49.879Z"
---
# Summary

Resolve Plan retained history destinations

## Objective

Complete the remaining P2484 Update/Move/Subject predecessor-history owner without changing non-Plan history behavior.

## Details

At most 15 minutes own work; split before extending. P2484 source checkpoint supplies archive_revision_destination(root, atom, version), but preserve_atom_revision still unconditionally emits role-local archive/ and Subject predictions mirror it. Create/reuse one canonical preserved_revision_destination(root, atom) in atom_operations.py: Plans use the admitted owning-scope flat archive resolver at current predecessor Version N; non-Plans retain their existing native role/archive convention. preserve_atom_revision and later Subject adapters must use that same preservation owner. Own atom_operations.py only; preserve all current guards/error classes, exact byte reads, metadata, source/currentness, collisions, restoration and prior P2478 code. No cwd inference, new packet fields, generic fallback behavior changes, bundle/history-location policy or runtime effects. The parent Task remains Active as a roll-up; this additional child is created before extending its original 15-minute own-work budget. P2485 bundle policy and C549 history subtree move remain separate.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
