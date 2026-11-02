---
atom_id: CA-P-2468@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2467
version: 3
updated_at: 2026-10-24 06:04:44 +0400
tier: 3
---
# Summary

Bind existing Draft promotion targets

## Objective

Seal the exact Draft descriptor, canonical predecessor descriptor, and proposed Version. Reuse typed carrier descriptors; require proposed Version=predecessor+1 and refuse stale, missing, ambiguous or colliding targets before effects.

## Details

At most 15 minutes own work; split before extending. Follow PROGRAMMATIC M projection and latest Operator same-ID promotion decision. Preserve exact history; no Journal/retained-Draft-history admission gate. No live test traffic, deployment, Methodology map repin or held-batch replay.

### Definition of Done

Seal the exact Draft descriptor, canonical predecessor descriptor, and proposed Version. Reuse typed carrier descriptors; require proposed Version=predecessor+1 and refuse stale, missing, ambiguous or colliding targets before effects. Observable focused evidence and independent review are required. Review dependent next Task before execution.

### Dependency review checkpoint

P2468 binding/preflight completed. Four frozen checks passed, including existing-marker creation, sealed-target rejection, Done-to-Active Version refusal and strict Boolean Version denial. Current uniqueness uses the shared bounded CurrentAtomLocator. API review accepts exact target and canonical_target descriptors plus explicit proposed_version; IDs/paths/Versions/digests must agree. P2469 was dependency-reviewed against these checks before activation; publication is not yet accepted.
