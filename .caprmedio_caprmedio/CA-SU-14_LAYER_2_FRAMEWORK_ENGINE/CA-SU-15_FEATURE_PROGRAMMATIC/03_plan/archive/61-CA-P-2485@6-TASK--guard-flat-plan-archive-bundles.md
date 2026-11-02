---
atom_id: CA-P-2485@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 61
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 6
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Guard flat Plan archive bundles

## Objective

Prevent flat Plan archive from silently relocating independent current descendant Atoms.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2484 archive-root contract. Same publication owner files as P2484; no concurrent writes. Require separately admitted descendant actions under CA-R-1521, preserve current descendant placement and incoming references. Check optional matching directory and asset collisions. The latest Operator decision requires the calling Workflow to archive contained latest Atoms recursively, without an optional mode; this low-level refusal prevents silent child relocation, not the authorized recursive operation. Retained-history subtrees and non-Atom assets may move byte-for-byte with the matching directory, without rewriting old Revision metadata. Do not invent relation removal, link repair, transition or rollback policy. P2494 owns Workflow sequencing and the target-Done rule; P2495 owns its independent functional acceptance. No legacy migration. Add one focused synthetic behavior check at the existing public lifecycle boundary; split further if own work exceeds 15 minutes.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review

The Operator decision is saved first in project records, then original R1521@10/D461@16/E502@14 and Engine O029@10/E306@15. P2484/P2490 shared destinations and P2491 Draft routing are implemented. This Task now owns only the parent-Action no-silent-current-child-move guard and matching-directory collision safety; the always-recursive caller is separate P2494. Existing file-only, empty, asset-only and byte-identical retained-history bundles remain admitted. No blanket user-request refusal or additional authorization gate is introduced.

### Verified completion

The shared Status publisher rejects Plan Archive before effects when matching-directory relocation would silently move an independent current child. Empty/asset-only directories and retained Markdown history with older carried Active Status remain admitted and byte-identical. Final native71 and independent code review passed on the replacement freeze. The guard is singleton safety, not implementation of the required recursive user request; C551/P2494/P2495 remain open.
