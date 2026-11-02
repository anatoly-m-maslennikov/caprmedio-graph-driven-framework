---
atom_id: CA-P-2490@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2484
version: 4
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Resolve Plan retained history destinations

## Objective

Complete the remaining P2484 Update/Move/Subject predecessor-history owner without changing non-Plan history behavior.

## Details

At most 15 minutes own work; split before extending. P2484 source checkpoint supplies archive_revision_destination(root, atom, version), but preserve_atom_revision still unconditionally emits role-local archive/ and Subject predictions mirror it. Create/reuse one canonical preserved_revision_destination(root, atom) in atom_operations.py: Plans use the admitted owning-scope flat archive resolver at current predecessor Version N; non-Plans retain their existing native role/archive convention. preserve_atom_revision and later Subject adapters must use that same preservation owner. Own atom_operations.py only; preserve all current guards/error classes, exact byte reads, metadata, source/currentness, collisions, restoration and prior P2478 code. No cwd inference, new packet fields, generic fallback behavior changes, bundle/history-location policy or runtime effects. The parent Task remains Active as a roll-up; this additional child is created before extending its original 15-minute own-work budget. P2485 bundle policy and C549 history subtree move remain separate.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified bounded checkpoint

The canonical preserved_revision_destination(root, atom) helper now selects Plan current-N predecessor paths through the owning-scope archive resolver, while preserving the original non-Plan role/archive path and error boundaries. preserve_atom_revision delegates to it. Root independently reviewed the helper and caller: existing currentness/lifecycle admission, collision checks, exact raw byte write and legacy identity handling remain. Two focused frozen-fixture retention checks passed with source unchanged and byte-exact history, one Plan and one non-Plan. Atom operations SHA-256 66f9487934b7494ad8a74a1b3808c264ee06c7594fe1d5e0e084554a89e30e31; lifecycle 4bf3ab19b6079f38cfcff6af664dedc2904929ec54f2c258de9b5fe9f2d9017f. Configured C901 remains the same 12 per-function baseline values. Integrated acceptance and P2491 promotion fixes remain separate; this is not parent P2484 completion.
