---
atom_id: CA-P-2470@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2467
version: 6
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Verify both existing Draft promotion entry points

## Objective

After CA-P-2469 passes, verify change_status and native ATOM_PROMOTE for qualified and compatible markers, exact predecessor bytes, stale pins, version mismatch, collisions, and failure preservation in synthetic Projects.

## Details

At most 15 minutes own work; split before extending. Follow PROGRAMMATIC M projection and latest Operator same-ID promotion decision. Preserve exact history; no Journal/retained-Draft-history admission gate. No live test traffic, deployment, Methodology map repin or held-batch replay.

### Definition of Done

After CA-P-2469 passes, verify change_status and native ATOM_PROMOTE for qualified and compatible markers, exact predecessor bytes, stale pins, version mismatch, collisions, and failure preservation in synthetic Projects. Observable focused evidence and independent review are required. Review dependent next Task before execution.

### Dependency review checkpoint

Correct Backlog placement under D461. Independent test preparation may proceed against the settled API, but acceptance execution waits for P2469 publication evidence and dependency review.

### Verified execution checkpoint

P2472 passed Done Plan to Active placement with child preservation, exact archived predecessor, and injected moved-publication/native-postwrite rollback. P2474 now owns the independently diagnosed fresh native Status normalization. Test preparation and frozen authority closure are reviewed; execute final native/golden/model matrix only once P2474 production files are stable, retaining mutation-free exact-no-op assertions. No production port or held batch.

### Verified execution checkpoint

Independent final acceptance passed native promotion 8/8 (74.345s), marker formats 6/6 (27.659s), model lifecycle 20/20 (144.517s), and exact frozen pins 1/1. Production hashes were unchanged before/after: atom_operations 11ee8dfe2452876791293bf3fd750dfdd760f56d129aa5d0a1c40254cba2bd7b, lifecycle_intents 64cb5347504978382931d8fd79f20d60b9ceb3f7debdbe16346ea26aee75a86c. Independent full-promotion suite also passed 22. Ruff for owned tests and diff checks passed; no live port was used. P2479 separately corrects the older parser cohort fixture.
